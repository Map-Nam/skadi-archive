"""Build the Skadi fan-site visual assets.

Official character art is fetched from PRTS (https://prts.wiki) for a
non-commercial, educational fan project. Character and artwork copyright
Hypergryph / Studio Montagne. Background photography is from Unsplash and
used under the Unsplash License.
"""

from __future__ import annotations

import io
import math
import random
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "assets" / "img"
SKADI = IMG / "skadi"
BG = IMG / "bg"
GALLERY = IMG / "gallery"

SERIF = r"C:\Windows\Fonts\NotoSerifSC-VF.ttf"
SANS = r"C:\Windows\Fonts\NotoSansSC-VF.ttf"
MONO = r"C:\Windows\Fonts\consola.ttf"

OFFICIAL = {
    "e2": "https://media.prts.wiki/b/b8/%E7%AB%8B%E7%BB%98_%E6%96%AF%E5%8D%A1%E8%92%82_2.png",
    "e0": "https://media.prts.wiki/4/45/%E7%AB%8B%E7%BB%98_%E6%96%AF%E5%8D%A1%E8%92%82_1.png",
    "skin1": "https://media.prts.wiki/1/1b/%E7%AB%8B%E7%BB%98_%E6%96%AF%E5%8D%A1%E8%92%82_skin1.png",
    "skin2": "https://media.prts.wiki/3/3d/%E7%AB%8B%E7%BB%98_%E6%96%AF%E5%8D%A1%E8%92%82_skin2.png",
    "alter": "https://media.prts.wiki/2/26/%E7%AB%8B%E7%BB%98_%E6%B5%8A%E5%BF%83%E6%96%AF%E5%8D%A1%E8%92%82_1.png",
    "avatar": "https://media.prts.wiki/5/53/%E5%A4%B4%E5%83%8F_%E6%96%AF%E5%8D%A1%E8%92%82.png",
    "wallpaper": "https://media.prts.wiki/5/56/%E5%85%AC%E5%91%8Ahd_%E6%96%AF%E5%8D%A1%E8%92%82_skin1.jpg",
}

UNSPLASH = {
    "sea-dusk": "photo-1439405326854-014607f694d7",
    "aerial-coast": "photo-1505118380757-91f5f5632de0",
    "foggy-ridge": "photo-1470071459604-3b5ec3a7fe05",
    "night-range": "photo-1519681393784-d120267933ba",
    "desk": "photo-1499750310107-5fef28a66643",
}

OFFICIAL_CACHE = ROOT / "tmp" / "skadi-art"
OFFICIAL_CACHE.mkdir(parents=True, exist_ok=True)
UNSPLASH_CACHE = ROOT / "tmp" / "unsplash"
UNSPLASH_CACHE.mkdir(parents=True, exist_ok=True)


def fetch(url: str, cache: Path, headers: dict[str, str] | None = None) -> bytes:
    if cache.exists():
        return cache.read_bytes()
    request = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(request, timeout=120) as response:
        data = response.read()
    cache.write_bytes(data)
    return data


def official(key: str) -> Image.Image:
    ext = ".jpg" if key == "wallpaper" else ".png"
    path = OFFICIAL_CACHE / f"{key}{ext}"
    data = fetch(
        OFFICIAL[key],
        path,
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/131.0",
            "Referer": "https://prts.wiki/",
            "Accept": "image/avif,image/webp,image/png,image/*,*/*;q=0.8",
        },
    )
    return Image.open(io.BytesIO(data)).convert("RGBA")


def unsplash(key: str) -> Image.Image:
    path = UNSPLASH_CACHE / f"{key}.jpg"
    data = fetch(
        f"https://images.unsplash.com/{UNSPLASH[key]}?w=2600&q=92&auto=format&fit=crop",
        path,
        {"User-Agent": "Mozilla/5.0"},
    )
    return Image.open(io.BytesIO(data)).convert("RGB")


def cover(image: Image.Image, size: tuple[int, int], centering=(0.5, 0.5)) -> Image.Image:
    return ImageOps.fit(image, size, Image.Resampling.LANCZOS, centering=centering)


def tint(image: Image.Image, color: tuple[int, int, int], strength: float) -> Image.Image:
    return Image.blend(image.convert("RGB"), Image.new("RGB", image.size, color), strength)


def add_glow(image: Image.Image, center, radius, color, alpha=110) -> Image.Image:
    layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    cx, cy = center
    steps = 14
    for i in range(steps, 0, -1):
        r = int(radius * i / steps)
        a = int(alpha * (1 - i / steps) ** 1.7)
        draw.ellipse((cx - r, cy - r * 0.88, cx + r, cy + r * 0.88), fill=(*color, a))
    layer = layer.filter(ImageFilter.GaussianBlur(radius // 7 or 1))
    return Image.alpha_composite(image.convert("RGBA"), layer)


def add_grain(image: Image.Image, strength=0.05) -> Image.Image:
    noise = Image.effect_noise(image.size, 28).convert("RGB")
    return Image.blend(image.convert("RGB"), noise, strength)


def art_cropped(key: str, height: int) -> Image.Image:
    art = official(key)
    bbox = art.getbbox()
    art = art.crop(bbox)
    ratio = height / art.height
    return art.resize((round(art.width * ratio), height), Image.Resampling.LANCZOS)


def paste_art(
    canvas: Image.Image,
    art: Image.Image,
    *,
    center_x: int,
    bottom: int,
    glow_color: tuple[int, int, int] | None = None,
) -> Image.Image:
    x = round(center_x - art.width / 2)
    y = bottom - art.height
    if glow_color:
        alpha = art.getchannel("A").filter(ImageFilter.GaussianBlur(28))
        glow = Image.new("RGBA", art.size, (*glow_color, 0))
        glow.putalpha(alpha.point(lambda p: int(p * 0.55)))
        canvas.alpha_composite(glow, (x, y))
    canvas.alpha_composite(art, (x, y))
    return canvas


def background_plate(key: str, size=(1400, 1750), *, color, strength, centering=(0.5, 0.5)) -> Image.Image:
    base = cover(unsplash(key), size, centering)
    base = ImageEnhance.Brightness(base).enhance(0.72)
    base = tint(base, color, strength)
    return base.convert("RGBA")


def add_rings(image: Image.Image, cx, cy, radii, color, alpha=80, width=2) -> None:
    draw = ImageDraw.Draw(image)
    for radius in radii:
        draw.ellipse(
            (cx - radius, cy - radius, cx + radius, cy + radius),
            outline=(*color, alpha),
            width=width,
        )


def add_frame(image: Image.Image, inset=38, color=(220, 235, 235), alpha=55) -> None:
    draw = ImageDraw.Draw(image)
    draw.rectangle((inset, inset, image.width - inset, image.height - inset), outline=(*color, alpha), width=1)
    # corner ticks
    for x, y, dx, dy in (
        (inset, inset, 1, 1),
        (image.width - inset, inset, -1, 1),
        (inset, image.height - inset, 1, -1),
        (image.width - inset, image.height - inset, -1, -1),
    ):
        draw.line((x, y, x + 34 * dx, y), fill=(*color, alpha + 55), width=2)
        draw.line((x, y, x, y + 34 * dy), fill=(*color, alpha + 55), width=2)


def label(draw: ImageDraw.ImageDraw, xy, text, font, fill, spacing=0):
    if not spacing:
        draw.text(xy, text, font=font, fill=fill)
        return
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += spacing


def make_poster(
    *,
    key: str,
    bg_key: str,
    accent: tuple[int, int, int],
    title: str,
    english: str,
    code: str,
    art_height: int = 1460,
    center_x: int = 700,
    bottom: int = 1740,
    glow: bool = True,
    blurb: str = "",
) -> Image.Image:
    canvas = background_plate(bg_key, color=(4, 19, 26), strength=0.62, centering=(0.5, 0.5))
    canvas = add_glow(canvas, (center_x, 760), 560, accent, 74 if key != "alter" else 120)
    add_rings(canvas, center_x, 700, (390, 455, 520), accent, 65, 2)

    # huge low-contrast operator number behind the character
    draw = ImageDraw.Draw(canvas)
    number_font = ImageFont.truetype(MONO, 420)
    draw.text((930, 60), "06", font=number_font, fill=(220, 240, 240, 18), stroke_width=1, stroke_fill=(220, 240, 240, 34))
    label(draw, (78, 68), code, ImageFont.truetype(MONO, 22), (224, 235, 232, 220))

    art = art_cropped(key, art_height)
    paste_art(canvas, art, center_x=center_x, bottom=bottom, glow_color=accent if glow else None)

    # bottom gradient for legibility
    gradient = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(gradient)
    for y in range(1120, canvas.height):
        a = int(235 * ((y - 1120) / (canvas.height - 1120)) ** 1.3)
        gd.line((0, y, canvas.width, y), fill=(3, 11, 16, a))
    canvas = Image.alpha_composite(canvas, gradient)

    draw = ImageDraw.Draw(canvas)
    accent_line = (*accent, 255)
    draw.line((78, 112, 238, 112), fill=accent_line, width=3)
    label(draw, (78, 132), "ABYSSAL ARCHIVE  /  OPERATOR FILE", ImageFont.truetype(MONO, 18), (217, 229, 226, 210))
    title_font = ImageFont.truetype(SERIF, 104)
    draw.text((74, 1500), title, font=title_font, fill=(244, 241, 232, 255))
    draw.text((80, 1638), english, font=ImageFont.truetype(MONO, 22), fill=(*accent, 255))
    if blurb:
        draw.text((80, 1680), blurb, font=ImageFont.truetype(SANS, 21), fill=(207, 220, 216, 220))

    add_frame(canvas)
    canvas = add_grain(canvas, 0.055)
    return canvas.convert("RGB")


def make_hero_background() -> None:
    base = cover(unsplash("sea-dusk"), (2400, 1500), (0.5, 0.52))
    base = ImageEnhance.Brightness(base).enhance(0.45)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = tint(base, (2, 17, 25), 0.64)
    canvas = base.convert("RGBA")
    # soft cold light from the upper right
    canvas = add_glow(canvas, (1760, 250), 900, (91, 190, 201), 78)
    canvas = add_glow(canvas, (1150, 680), 700, (35, 100, 112), 46)
    # light shafts
    shafts = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shafts)
    for i in range(7):
        x = 1450 + i * 95
        sd.polygon(
            [(x, 0), (x + 70, 0), (x - 260, 1500), (x - 390, 1500)],
            fill=(120, 211, 215, 10),
        )
    shafts = shafts.filter(ImageFilter.GaussianBlur(18))
    canvas = Image.alpha_composite(canvas, shafts)
    # drifting particles
    random.seed(21)
    particles = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    pd = ImageDraw.Draw(particles)
    for _ in range(260):
        x = random.randint(0, canvas.width)
        y = random.randint(0, canvas.height)
        r = random.choice([1, 1, 1, 2, 2, 3])
        a = random.randint(12, 55)
        pd.ellipse((x, y, x + r, y + r), fill=(194, 232, 231, a))
    canvas = Image.alpha_composite(canvas, particles.filter(ImageFilter.GaussianBlur(0.5)))
    # vignette / darken left
    vignette = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    vd = ImageDraw.Draw(vignette)
    for x in range(canvas.width):
        a = int(165 * (1 - x / canvas.width) ** 1.5)
        vd.line((x, 0, x, canvas.height), fill=(2, 10, 15, a))
    for y in range(canvas.height):
        a = int(80 * (y / canvas.height) ** 2)
        vd.line((0, y, canvas.width, y), fill=(2, 10, 15, a))
    canvas = Image.alpha_composite(canvas, vignette)
    canvas = add_grain(canvas, 0.06)
    BG.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(BG / "abyss-hero.jpg", "JPEG", quality=84, optimize=True, progressive=True)
    print("hero background saved")


def make_mood_images() -> None:
    GALLERY.mkdir(parents=True, exist_ok=True)
    specs = [
        ("foggy-ridge", "mood-01.jpg", (8, 20, 26), 0.45, (0.5, 0.52)),
        ("night-range", "mood-02.jpg", (2, 11, 20), 0.55, (0.5, 0.45)),
        ("aerial-coast", "mood-03.jpg", (0, 36, 45), 0.28, (0.5, 0.5)),
    ]
    for key, name, color, strength, center in specs:
        image = cover(unsplash(key), (1600, 1067), center)
        image = ImageEnhance.Brightness(image).enhance(0.76)
        image = tint(image, color, strength)
        image = add_grain(image, 0.04)
        image.convert("RGB").save(GALLERY / name, "JPEG", quality=84, optimize=True, progressive=True)
        print("mood saved", name)

    wallpaper = official("wallpaper").convert("RGB")
    wallpaper = cover(wallpaper, (2000, 1125))
    wallpaper = ImageEnhance.Contrast(wallpaper).enhance(1.03)
    wallpaper.save(GALLERY / "official-wallpaper.jpg", "JPEG", quality=84, optimize=True, progressive=True)
    print("wallpaper saved")


def make_tide_poster() -> None:
    canvas = background_plate("foggy-ridge", color=(2, 20, 25), strength=0.55, centering=(0.5, 0.45))
    canvas = add_glow(canvas, (1030, 390), 450, (155, 212, 208), 55)
    add_rings(canvas, 1030, 390, (170, 230, 290, 350), (155, 212, 208), 55, 2)
    draw = ImageDraw.Draw(canvas)
    draw.line((78, 112, 238, 112), fill=(191, 232, 229, 255), width=3)
    label(draw, (78, 132), "IMPRESSION  /  TIDE WATCH", ImageFont.truetype(MONO, 18), (217, 229, 226, 210))
    draw.text((74, 470), "听潮", font=ImageFont.truetype(SERIF, 220), fill=(238, 241, 233, 245))
    draw.text((82, 760), "LISTEN TO THE TIDE", font=ImageFont.truetype(MONO, 30), fill=(191, 232, 229, 240))
    draw.text((82, 1510), "潮汐之下，仍有歌声。", font=ImageFont.truetype(SERIF, 58), fill=(238, 241, 233, 245))
    draw.text((82, 1600), "A SMALL TRIBUTE TO SKADI  /  2026", font=ImageFont.truetype(MONO, 18), fill=(191, 232, 229, 190))
    add_frame(canvas)
    canvas = add_grain(canvas, 0.055)
    final = canvas.convert("RGB")
    final.save(GALLERY / "poster-06.jpg", "JPEG", quality=85, optimize=True, progressive=True)
    thumb = final.copy()
    thumb.thumbnail((700, 875), Image.Resampling.LANCZOS)
    thumb.save(GALLERY / "poster-06-thumb.jpg", "JPEG", quality=78, optimize=True, progressive=True)
    print("tide poster saved")


def make_og() -> None:
    hero = Image.open(BG / "abyss-hero.jpg").convert("RGB")
    canvas = cover(hero, (1200, 630), (0.5, 0.5)).convert("RGBA")
    art = art_cropped("e2", 890)
    canvas = paste_art(canvas, art, center_x=940, bottom=830, glow_color=(86, 180, 191))
    # left readability
    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    for x in range(canvas.width):
        a = int(225 * (1 - x / canvas.width) ** 1.5)
        d.line((x, 0, x, canvas.height), fill=(2, 12, 17, a))
    canvas = Image.alpha_composite(canvas, overlay)
    d = ImageDraw.Draw(canvas)
    d.line([(70, 80), (160, 80)], fill=(199, 78, 76, 255), width=3)
    d.text((70, 100), "ABYSSAL ARCHIVE  /  FAN PROJECT", font=ImageFont.truetype(MONO, 17), fill=(222, 233, 230))
    d.text((64, 178), "斯卡蒂", font=ImageFont.truetype(SERIF, 132), fill=(244, 241, 232))
    d.text((70, 338), "深海猎人 · 罗德岛六星近卫", font=ImageFont.truetype(SANS, 28), fill=(221, 231, 226))
    d.text((70, 394), "潮汐之下，仍有歌声。", font=ImageFont.truetype(SERIF, 36), fill=(191, 224, 222))
    d.text((70, 548), "SKADI  /  AA01  /  NON-OFFICIAL CHARACTER TRIBUTE", font=ImageFont.truetype(MONO, 14), fill=(168, 190, 190))
    canvas.convert("RGB").save(IMG / "og-cover.jpg", "JPEG", quality=88, optimize=True, progressive=True)
    print("og saved")


def make_contour() -> None:
    def path(cx, cy, r, phase, amp):
        pts = []
        for i in range(181):
            t = 2 * math.pi * i / 180
            rr = r + amp * math.sin(3 * t + phase) + amp * 0.45 * math.sin(7 * t - phase * 1.7)
            pts.append((cx + rr * math.cos(t), cy + rr * 0.72 * math.sin(t)))
        return "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts)

    paths = []
    for i in range(12):
        paths.append(
            f'<path d="{path(600, 450, 60 + i * 34, 0.6 + i * 0.15, 10 + i * 1.4)}" '
            f'fill="none" stroke="#a9d8d6" stroke-opacity="{0.16 - i * 0.009:.3f}" stroke-width="1.1"/>'
        )
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" role="img" aria-label="等高线装饰">\n'
    svg += "\n".join(paths) + "\n</svg>\n"
    (IMG / "contour.svg").write_text(svg, encoding="utf-8")
    print("contour saved")


def make_avatar_feature() -> None:
    art = art_cropped("e2", 1600)
    crop = art.crop((640, 390, 1160, 910))
    size = 520
    canvas = Image.new("RGBA", (size, size), (5, 18, 24, 255))
    draw = ImageDraw.Draw(canvas)
    for y in range(size):
        draw.line(
            (0, y, size, y),
            fill=(5 + int(12 * y / size), 18 + int(28 * y / size), 24 + int(30 * y / size), 255),
        )
    canvas.alpha_composite(crop, (0, 0))
    vignette = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    vd = ImageDraw.Draw(vignette)
    for i in range(80):
        vd.rectangle((i, i, size - i, size - i), outline=(0, 0, 0, int(120 * (i / 80) ** 1.5)))
    canvas = Image.alpha_composite(canvas, vignette)
    canvas.convert("RGB").save(SKADI / "avatar-feature.jpg", "JPEG", quality=90, optimize=True, progressive=True)
    print("avatar feature saved")


def main() -> None:
    for directory in (SKADI, BG, GALLERY):
        directory.mkdir(parents=True, exist_ok=True)

    # transparent character art, WebP only (modern browsers; keeps the repo lean)
    for key, height in (("e2", 1600), ("e0", 1500), ("skin1", 1500), ("skin2", 1500), ("alter", 1600)):
        art = art_cropped(key, height)
        art.save(SKADI / f"{key}.webp", "WEBP", quality=91, method=6)
        print("art saved", key, art.size)

    make_avatar_feature()

    make_hero_background()
    make_mood_images()
    make_tide_poster()

    posters = [
        dict(
            key="e2", bg_key="sea-dusk", accent=(196, 77, 75), title="斯卡蒂",
            english="SKADI  /  ABYSSAL HUNTER", code="AA01  /  6★ GUARD",
            blurb="深海猎人 · 无畏者 / 非感染者",
        ),
        dict(
            key="e0", bg_key="night-range", accent=(150, 197, 206), title="潮汐来客",
            english="RHODES ISLAND  /  OPERATOR", code="AA01  /  ARCHIVE 01",
            blurb="从潮湿的地方来，到干燥的你身边。", art_height=1400, center_x=660,
        ),
        dict(
            key="skin1", bg_key="aerial-coast", accent=(236, 224, 180), title="驭浪",
            english="CORAL COAST  /  WR04", code="MARTHE  /  SUMMER 04",
            blurb="让海中精灵在沙滩上也能光彩夺目。", art_height=1430, center_x=700,
        ),
        dict(
            key="skin2", bg_key="desk", accent=(221, 164, 120), title="下一顿午茶",
            english="MARTHE  /  AFTERNOON TEA", code="MARTHE  /  V",
            blurb="为久居陆地的阿戈尔量身打造。", art_height=1430, center_x=700,
        ),
        dict(
            key="alter", bg_key="sea-dusk", accent=(196, 48, 54), title="浊心斯卡蒂",
            english="ALTER  /  CORRUPTING HEART", code="??  /  IF",
            blurb="另一种可能性，另一种潮声。", art_height=1470, center_x=700,
        ),
    ]
    for index, spec in enumerate(posters, start=1):
        key = spec.pop("key")
        image = make_poster(key=key, **spec)
        image.save(GALLERY / f"poster-{index:02d}.jpg", "JPEG", quality=84, optimize=True, progressive=True)
        thumb = image.copy()
        thumb.thumbnail((700, 875), Image.Resampling.LANCZOS)
        thumb.save(GALLERY / f"poster-{index:02d}-thumb.jpg", "JPEG", quality=78, optimize=True, progressive=True)
        print("poster saved", index)

    make_og()
    make_contour()


if __name__ == "__main__":
    main()
