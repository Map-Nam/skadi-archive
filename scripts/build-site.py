"""Generate the static HTML pages for the Skadi fan site."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NAV = [
    ("index.html", "首页", "HOME", "home"),
    ("profile.html", "档案", "FILE", "profile"),
    ("story.html", "故事", "STORY", "story"),
    ("combat.html", "战斗", "COMBAT", "combat"),
    ("gallery.html", "影像", "GALLERY", "gallery"),
    ("voices.html", "语音", "VOICE", "voices"),
]


def head(title: str, description: str, page: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#061219">
  <meta name="color-scheme" content="dark">
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/fonts/fonts.css">
  <link rel="stylesheet" href="assets/css/style.css">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="zh_CN">
  <meta property="og:site_name" content="深海档案 / ABYSSAL ARCHIVE">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="assets/img/og-cover.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="斯卡蒂 · 深海档案">
  <meta name="twitter:card" content="summary_large_image">
  <script>document.documentElement.classList.add('js');</script>
</head>
<body class="page-{page}">"""


def header(active: str) -> str:
    links = []
    for href, label, en, slug in NAV:
        current = ' aria-current="page"' if slug == active else ""
        links.append(
            f'<a class="nav-link" href="{href}"{current}><span>{label}</span><small>{en}</small></a>'
        )
    nav_html = "\n        ".join(links)
    return f"""
<a class="skip-link" href="#main">跳到主要内容</a>
<header class="site-header" data-header>
  <div class="shell header-inner">
    <a class="brand" href="index.html" aria-label="深海档案首页">
      <span class="brand-mark" aria-hidden="true"><span>AA</span></span>
      <span class="brand-copy"><strong>深海档案</strong><small>ABYSSAL ARCHIVE</small></span>
    </a>
    <nav class="nav" id="site-nav" aria-label="主导航">
        {nav_html}
    </nav>
    <div class="header-tools">
      <span class="signal" aria-hidden="true"><i></i> SIGNAL / 08</span>
      <button class="menu-toggle" type="button" data-menu-toggle aria-controls="site-nav" aria-expanded="false" aria-label="打开导航菜单">
        <span></span><span></span>
      </button>
    </div>
  </div>
</header>
<div class="nav-scrim" data-nav-close aria-hidden="true"></div>"""


def footer() -> str:
    return """
<footer class="site-footer">
  <div class="shell">
    <div class="footer-top">
      <p class="footer-cta">潮汐之下，<br>仍有<em>歌声</em>。</p>
      <a class="btn" href="voices.html">聆听她的声音</a>
    </div>
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="index.html" aria-label="返回首页">
          <span class="brand-mark" aria-hidden="true"><span>AA</span></span>
          <span class="brand-copy"><strong>深海档案</strong><small>ABYSSAL ARCHIVE</small></span>
        </a>
        <p>一个关于斯卡蒂的非官方角色介绍站。用 HTML、CSS 与原生 JavaScript 手工搭建，作为网页设计课程练习，不作商业用途。</p>
      </div>
      <div class="footer-col">
        <h3>Archive</h3>
        <ul>
          <li><a href="profile.html">干员档案</a></li>
          <li><a href="story.html">深海回响</a></li>
          <li><a href="combat.html">战斗手册</a></li>
          <li><a href="gallery.html">影像档案</a></li>
          <li><a href="voices.html">语音记录</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3>Credits</h3>
        <p>角色与官方立绘版权归鹰角网络 / Hypergryph 所有。资料参考 <a class="text-link" href="https://prts.wiki/w/%E6%96%AF%E5%8D%A1%E8%92%82" target="_blank" rel="noopener noreferrer">PRTS 明日方舟中文 Wiki</a>。背景摄影来自 <a class="text-link" href="https://unsplash.com/license" target="_blank" rel="noopener noreferrer">Unsplash</a>。</p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> ABYSSAL ARCHIVE · FAN PROJECT · 非官方粉丝企划</span>
      <button class="to-top" type="button" data-to-top>BACK TO SURFACE ↑</button>
    </div>
  </div>
</footer>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def page(title: str, description: str, active: str, body: str) -> str:
    return f"""{head(title, description, active)}
{header(active)}
<main id="main">
{body}
</main>
{footer()}"""


def ticker() -> str:
    items = [
        "ABYSSAL HUNTER",
        "6★ GUARD",
        "AEGIR",
        "NON-INFECTED",
        "DRE-X / DRE-Y",
        "SIGNAL FROM THE DEEP",
    ]
    spans = "\n      ".join(f"<span>{item}</span>" for item in items)
    return f"""
<div class="ticker" aria-hidden="true">
  <div class="ticker-track">
      {spans}
      {spans}
  </div>
</div>"""


HOME_BODY = f"""
<section class="hero" aria-labelledby="hero-title">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="shell hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">ABYSSAL ARCHIVE / OPERATOR AA01</p>
      <h1 class="hero-title" id="hero-title">
        <span>潮汐之下</span>
        <span class="accent">仍在歌唱</span>
      </h1>
      <p class="hero-sub">斯卡蒂，阿戈尔出身的深海猎人，罗德岛六星近卫。她习惯独行，也习惯把危险挡在别人之外；但在漫长的黑暗之后，她仍然记得，怎样为一束光停下脚步。</p>
      <div class="hero-actions">
        <a class="btn btn--solid" href="profile.html">读取干员档案</a>
        <a class="btn" href="voices.html">聆听她的声音</a>
      </div>
      <dl class="hero-meta">
        <div><dt>Codename</dt><dd>斯卡蒂 / Skadi</dd></div>
        <div><dt>Class</dt><dd>近卫 · 无畏者</dd></div>
        <div><dt>Faction</dt><dd>深海猎人</dd></div>
        <div><dt>Rarity</dt><dd>★★★★★★</dd></div>
      </dl>
    </div>
    <div class="hero-art">
      <div class="hero-orbit" aria-hidden="true"></div>
      <div class="hero-scan" aria-hidden="true"></div>
      <img class="hero-portrait" src="assets/img/skadi/e2.webp" alt="斯卡蒂精英二立绘：银白长发、红色眼睛，手持巨剑，身后翻涌着白色水浪" width="1740" height="1600" fetchpriority="high">
      <div class="hero-hud" aria-hidden="true"><span>DEPTH 02,140 M</span><span>HUNTER / ACTIVE</span><span>AA01 — 06</span></div>
      <div class="hero-tag"><span>ROLE</span><strong>深海猎人</strong><i aria-hidden="true"></i><span>AA01 / 6★ GUARD</span></div>
      <span class="hero-vertical" aria-hidden="true">ABYSSAL HUNTER · SKADI</span>
    </div>
  </div>
  <div class="shell hero-footer">
    <span class="scroll-cue">SCROLL TO DIVE</span>
    <span>NON-OFFICIAL CHARACTER TRIBUTE / 2026</span>
  </div>
</section>
{ticker()}

<section class="section" id="dossier">
  <div class="shell">
    <div class="section-head" data-reveal>
      <div>
        <p class="section-index">01 / DOSSIER</p>
        <h2 class="section-title">她不是传说，<br>只是习惯了<em>独自承担</em>。</h2>
      </div>
      <div class="section-head__aside">
        <p class="section-lead">在罗德岛的档案里，斯卡蒂是“赏金猎人”“深海猎人”“六星近卫”。在普通干员口中，她更像一场不能靠近的天灾。</p>
        <a class="section-link" href="profile.html">打开完整档案</a>
      </div>
    </div>
    <div class="summary-grid">
      <figure class="summary-art" data-reveal>
        <img src="assets/img/skadi/e0.webp" alt="斯卡蒂初始立绘：银白长发，黑色宽檐帽，手持巨剑" width="1083" height="1500" loading="lazy">
        <figcaption class="summary-art__label"><strong>斯卡蒂</strong><span>AA01 / ORIGINAL FILE</span></figcaption>
      </figure>
      <div class="summary-copy" data-reveal data-reveal-delay="1">
        <p>档案不会记录的是：她会坐在甲板边沿低声唱歌，会把家乡的歌谱留在信物里，也会在确认你足够执着之后，认真地说一句——“这样我不就只能老老实实保护你了吗。”</p>
        <p>她拒绝大多数合作请求的理由只有一条：不希望给他人带来危险。所谓冷漠，是她能想到的、最笨拙也最温柔的保护方式。</p>
        <dl class="fact-grid">
          <div><dt>Origin</dt><dd>阿戈尔</dd></div>
          <div><dt>Race</dt><dd>未公开</dd></div>
          <div><dt>Combat Exp.</dt><dd>十三年</dd></div>
          <div><dt>Infection</dt><dd>非感染者</dd></div>
          <div><dt>Birthday</dt><dd>3 月 7 日</dd></div>
          <div><dt>Height</dt><dd>166 cm</dd></div>
        </dl>
        <div class="summary-actions"><a class="btn" href="profile.html">查看数据与档案摘录</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="fragments">
  <div class="shell">
    <div class="section-head" data-reveal>
      <div>
        <p class="section-index">02 / THREE FRAGMENTS</p>
        <h2 class="section-title">猎人、歌者，<br>以及一条<em>归途</em>。</h2>
      </div>
      <div class="section-head__aside">
        <p class="section-lead">如果只用一个词形容斯卡蒂，很容易把她弄丢。她身上同时存在着锋利的巨剑、低沉的歌声，和一个不知该往哪里去的背影。</p>
      </div>
    </div>
    <div class="fragment-grid">
      <a class="fragment-card" href="profile.html" data-reveal>
        <span class="fragment-card__number">01 / HUNTER</span>
        <span class="fragment-card__kicker">The Hunter</span>
        <h3>猎人</h3>
        <p>她的战场从来不在人群中央。巨剑、单兵任务、深海猎人——这些词构成了她最容易被看见的一面，也遮住了她最不愿意解释的部分。</p>
        <span class="fragment-link">读她的档案</span>
      </a>
      <a class="fragment-card" href="voices.html" data-reveal data-reveal-delay="1">
        <span class="fragment-card__number">02 / SINGER</span>
        <span class="fragment-card__kicker">The Singer</span>
        <h3>歌者</h3>
        <p>有些歌不需要被听懂。她会在无人的甲板边低声哼唱，也会把用家乡语言写下的歌谱，当作一件认真准备送出的礼物。</p>
        <span class="fragment-link">听她说话</span>
      </a>
      <a class="fragment-card" href="story.html" data-reveal data-reveal-delay="2">
        <span class="fragment-card__number">03 / WAY HOME</span>
        <span class="fragment-card__kicker">The Way Back</span>
        <h3>归途</h3>
        <p>她一直在寻找一个可以停下来的地方，却又害怕靠近会带来新的失去。罗德岛没有承诺答案，只是给了她一条可以暂时同行的路。</p>
        <span class="fragment-link">进入深海回响</span>
      </a>
    </div>
  </div>
</section>

<section class="section" id="combat">
  <div class="shell">
    <div class="section-head" data-reveal>
      <div>
        <p class="section-index">03 / COMBAT SNAPSHOT</p>
        <h2 class="section-title">纯粹的强大，<br>也有它的<em>代价</em>。</h2>
      </div>
      <div class="section-head__aside">
        <p class="section-lead">高生命、高攻击、阻挡一人的无畏者。她不适合被放在每一条战线，却总能在最需要的地方，单独切开一个缺口。</p>
        <a class="section-link" href="combat.html">阅读战斗手册</a>
      </div>
    </div>
    <div class="combat-panel" data-reveal>
      <div class="combat-copy">
        <p class="eyebrow eyebrow--accent">E2 / LEVEL 90 / TRUST</p>
        <dl class="combat-stats">
          <div><dt>HP</dt><dd>3866</dd></div>
          <div><dt>ATK</dt><dd>1015<small>+80</small></dd></div>
          <div><dt>DEF</dt><dd>263<small>+40</small></dd></div>
          <div><dt>RES</dt><dd>0</dd></div>
        </dl>
        <p class="combat-note">精英二 90 级、满信赖、无潜能、无模组。详细数据与模组效果见战斗手册。</p>
      </div>
      <div class="combat-side">
        <ul class="skill-mini">
          <li><b>S1</b><strong>迅捷打击·γ型</strong><small>稳定输出</small></li>
          <li><b>S2</b><strong>跃浪击</strong><small>空降单切</small></li>
          <li><b>S3</b><strong>涌潮悲歌</strong><small>站场强化</small></li>
        </ul>
        <p class="combat-note">“不愿意和他人合作的人，往往是对自己的能力有所误判，但斯卡蒂显然不在此列。”</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="gallery-preview">
  <div class="shell">
    <div class="section-head" data-reveal>
      <div>
        <p class="section-index">04 / VISUAL ARCHIVE</p>
        <h2 class="section-title">每一帧，<br>都是潮水的<em>回声</em>。</h2>
      </div>
      <div class="section-head__aside">
        <p class="section-lead">官方立绘、衣装与氛围印象。画面里的她，有时是猎人，有时只是一个在海边发呆的人。</p>
        <a class="section-link" href="gallery.html">进入影像档案</a>
      </div>
    </div>
    <div class="rail-wrap" data-reveal>
      <div class="rail" aria-label="影像预览">
        <a class="rail-item" href="gallery.html">
          <span class="rail-item__index">01</span>
          <img src="assets/img/gallery/poster-01-thumb.jpg" alt="斯卡蒂精英二立绘海报" width="700" height="875" loading="lazy">
          <span class="rail-caption"><strong>斯卡蒂 / 精英二</strong><span>ILLUSTRATION · E2</span></span>
        </a>
        <a class="rail-item" href="gallery.html">
          <span class="rail-item__index">02</span>
          <img src="assets/img/gallery/poster-03-thumb.jpg" alt="斯卡蒂驭浪皮肤海报" width="700" height="875" loading="lazy">
          <span class="rail-caption"><strong>驭浪 / 珊瑚海岸</strong><span>OUTFIT · WR04</span></span>
        </a>
        <a class="rail-item" href="gallery.html">
          <span class="rail-item__index">03</span>
          <img src="assets/img/gallery/poster-05-thumb.jpg" alt="浊心斯卡蒂异格立绘海报" width="700" height="875" loading="lazy">
          <span class="rail-caption"><strong>浊心斯卡蒂 / 异格</strong><span>ALTER · IF</span></span>
        </a>
        <a class="rail-item" href="gallery.html">
          <span class="rail-item__index">04</span>
          <img src="assets/img/gallery/poster-02-thumb.jpg" alt="斯卡蒂初始立绘海报" width="700" height="875" loading="lazy">
          <span class="rail-caption"><strong>潮汐来客 / 初始</strong><span>ILLUSTRATION · E0</span></span>
        </a>
        <a class="rail-item" href="gallery.html">
          <span class="rail-item__index">05</span>
          <img src="assets/img/gallery/poster-04-thumb.jpg" alt="斯卡蒂下一顿午茶皮肤海报" width="700" height="875" loading="lazy">
          <span class="rail-caption"><strong>下一顿午茶 / 玛尔特</strong><span>OUTFIT · V</span></span>
        </a>
      </div>
    </div>
  </div>
</section>

<section class="section quote-band" aria-labelledby="voice-title">
  <div class="shell quote-inner">
    <div class="quote-intro" data-reveal>
      <p class="section-index">05 / VOICE</p>
      <h2 class="section-title" id="voice-title">她说的每一句话，<br>都像隔着一段<em>潮水</em>。</h2>
      <p>文字台词节选。完整语音与全部记录，请在游戏内体验。</p>
      <a class="section-link" href="voices.html" style="margin-top:24px">打开语音记录</a>
    </div>
    <div class="quote-stage" data-quote-rotator data-autoplay="true" data-reveal data-reveal-delay="1">
      <div>
        <div class="quote-slide" data-quote-slide>
          <blockquote>“为了你的安全着想，最好离我两米以上，也不要和我说话……我可不想你被冲着我来的危险伤到。”</blockquote>
          <cite>任命助理 / 初始</cite>
        </div>
        <div class="quote-slide" data-quote-slide hidden>
          <blockquote>“我的头发很长，很好看？啊，嗯，谢谢……要不要摸摸看？我的头发还是挺柔软的。”</blockquote>
          <cite>交谈 2 / 初始</cite>
        </div>
        <div class="quote-slide" data-quote-slide hidden>
          <blockquote>“你这人，怎么这么执着，这样我不就只能老老实实保护你了吗。”</blockquote>
          <cite>晋升后交谈 1 / 精英一</cite>
        </div>
        <div class="quote-slide" data-quote-slide hidden>
          <blockquote>“远方浩瀚蓝色与轻抚土地的白色碎片之下，埋葬着原本我所在乎的一切。”</blockquote>
          <cite>晋升后交谈 2 / 精英二</cite>
        </div>
        <div class="quote-slide" data-quote-slide hidden>
          <blockquote>“睡着了？睡吧，博士，得做个干燥的好梦哟。”</blockquote>
          <cite>闲置 / 初始</cite>
        </div>
      </div>
      <div class="quote-controls">
        <button class="circle-btn" type="button" data-quote-prev aria-label="上一句台词">←</button>
        <button class="circle-btn" type="button" data-quote-next aria-label="下一句台词">→</button>
        <span class="quote-count" data-quote-count>01 / 05</span>
      </div>
    </div>
  </div>
</section>

<section class="section closing">
  <div class="shell closing__inner">
    <div data-reveal>
      <p class="eyebrow">END OF TRANSMISSION</p>
      <h2 class="display-title">愿每一次下潜，<br>都能<em>循光而归</em>。</h2>
      <p class="section-lead" style="margin-top:24px">她不是需要被拯救的角色。她只是值得被认真理解的人。</p>
    </div>
    <div class="btn-row" data-reveal data-reveal-delay="1">
      <a class="btn btn--solid" href="story.html">进入深海回响</a>
      <a class="btn" href="gallery.html">查看全部影像</a>
    </div>
  </div>
</section>
"""

HOME_BODY = HOME_BODY.replace('loading="lazy"', 'loading="eager"')

PROFILE_BODY = """
<section class="page-hero page-hero--night" aria-labelledby="page-title">
  <span class="page-hero__ghost" aria-hidden="true">FILE</span>
  <div class="shell">
    <nav class="breadcrumb" aria-label="面包屑"><a href="index.html">INDEX</a><span>/</span><span>OPERATOR FILE</span></nav>
    <p class="eyebrow">OPERATOR FILE / AA01</p>
    <h1 class="page-title" id="page-title">干员<em>档案</em></h1>
    <p class="page-lead">代号斯卡蒂。关于她的过去，档案里有很多空白；关于她的现在，罗德岛仍在学习如何与她相处。</p>
    <div class="page-hero__bottom">
      <div class="badge-row">
        <span class="badge badge--accent">6★ 近卫</span>
        <span class="badge">无畏者</span>
        <span class="badge">阿戈尔</span>
        <span class="badge badge--cyan">深海猎人</span>
      </div>
      <span class="badge">NON-INFECTED / 非感染者</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell dossier-grid">
    <figure class="dossier-art" data-reveal>
      <img src="assets/img/skadi/e0.webp" alt="斯卡蒂初始立绘全身像" width="1083" height="1500" loading="lazy">
      <figcaption class="dossier-art__caption">AA01 / INITIAL VISUAL / ILLUSTRATION: ALCHEMANIAC</figcaption>
    </figure>
    <div class="dossier-copy" data-reveal data-reveal-delay="1">
      <p class="eyebrow">IDENTIFICATION</p>
      <h2 class="section-title" style="margin-top:14px;max-width:10ch">斯卡蒂<br>Skadi</h2>
      <dl class="info-table" style="margin-top:30px">
        <div class="info-row"><dt>代号</dt><dd>斯卡蒂 / Skadi</dd></div>
        <div class="info-row"><dt>编号</dt><dd>AA01</dd></div>
        <div class="info-row"><dt>职业</dt><dd>近卫 · 无畏者</dd></div>
        <div class="info-row"><dt>阵营</dt><dd>阿戈尔 / 深海猎人</dd></div>
        <div class="info-row"><dt>画师</dt><dd>alchemaniac</dd></div>
        <div class="info-row"><dt>中文 CV</dt><dd>张琦</dd></div>
        <div class="info-row"><dt>日文 CV</dt><dd>佐藤利奈</dd></div>
        <div class="info-row"><dt>英文 CV</dt><dd>Cristina Vee</dd></div>
        <div class="info-row"><dt>韩文 CV</dt><dd>金拿燏</dd></div>
        <div class="info-row"><dt>生日 / 身高</dt><dd>3 月 7 日 / 166 cm</dd></div>
        <div class="info-row"><dt>种族</dt><dd>未公开</dd></div>
        <div class="info-row"><dt>战斗经验</dt><dd>十三年</dd></div>
        <div class="info-row"><dt>感染状态</dt><dd>非感染者 / 体细胞源石融合率 0%</dd></div>
      </dl>

      <div class="subhead"><h2>综合体检测试</h2><span>PHYSICAL EXAM</span></div>
      <dl class="rating-list">
        <div class="rating-row"><dt>物理强度</dt><dd><i></i><i></i><i></i><i></i><i></i></dd><small>未公开</small></div>
        <div class="rating-row"><dt>战场机动</dt><dd><i class="on"></i><i class="on"></i><i class="on"></i><i></i><i></i></dd><small>标准</small></div>
        <div class="rating-row"><dt>生理耐受</dt><dd><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="hot"></i></dd><small>卓越</small></div>
        <div class="rating-row"><dt>战术规划</dt><dd><i class="on"></i><i class="on"></i><i class="on"></i><i></i><i></i></dd><small>标准</small></div>
        <div class="rating-row"><dt>战斗技巧</dt><dd><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i></i></dd><small>优良</small></div>
        <div class="rating-row"><dt>源石技艺适应性</dt><dd><i class="hot"></i><i></i><i></i><i></i><i></i></dd><small>缺陷</small></div>
      </dl>

      <div class="subhead"><h2>精英二属性</h2><span>E2 / LV.90 / TRUST</span></div>
      <div class="fact-inline">
        <div><dt>生命上限</dt><dd>3866</dd></div>
        <div><dt>攻击</dt><dd>1015 <small style="font-size:11px;color:var(--muted)">+80</small></dd></div>
        <div><dt>防御</dt><dd>263 <small style="font-size:11px;color:var(--muted)">+40</small></dd></div>
      </div>
      <p class="combat-note">部署费用 17→19 · 阻挡数 1 · 攻击间隔 1.5s · 再部署 70s · 法术抗性 0。数据为满信赖、无潜能、无模组。</p>

      <div class="subhead"><h2>档案摘录</h2><span>SELECTED FILES</span></div>
      <blockquote class="archive-quote">“干员斯卡蒂声称与她亲密交往的人最后都会遭遇不测，而她为了保护朋友，选择了不再拥有朋友。”<cite>档案资料三</cite></blockquote>
      <blockquote class="archive-quote">“只是，偶尔也有干员目击到斯卡蒂坐在甲板边沿，低声哼唱歌曲的场景。虽然无法理解歌词，但有目击经历的干员基本都声称，那是低沉、悠长，让他们感到忧伤的歌曲。”<cite>档案资料三</cite></blockquote>
      <blockquote class="archive-quote">“用家乡语言写下的歌谱。虽然完全没法理解这种文字，但她确实是打算教你这首歌的。”<cite>信物描述</cite></blockquote>
      <p style="color:var(--muted);font-size:13px;line-height:2">医疗部门的记录里，她的源石融合率为 0%，血液源石结晶密度为 0.013u/L。对罗德岛而言，这既是特例，也是另一个尚未解开的谜。</p>

      <div class="subhead"><h2>“天灾”之外</h2><span>BEYOND THE RUMOR</span></div>
      <p style="color:var(--muted);font-size:14px;line-height:2">普通干员对她的印象多来自战场：寡言、残酷、独来独往。但档案资料也写下另一面——她对合作请求的拒绝，很多时候只是因为不希望把危险带给别人。她把“保护”做成了一道墙，墙外的人看见的是冷漠，墙内的人承受的是孤独。</p>
      <div class="btn-row" style="margin-top:30px">
        <a class="btn btn--solid" href="story.html">继续阅读：深海回响</a>
        <a class="btn" href="combat.html">查看战斗数据</a>
      </div>
    </div>
  </div>
</section>
"""


STORY_BODY = """
<section class="page-hero page-hero--fog" aria-labelledby="page-title">
  <span class="page-hero__ghost" aria-hidden="true">TIDE</span>
  <div class="shell">
    <nav class="breadcrumb" aria-label="面包屑"><a href="index.html">INDEX</a><span>/</span><span>STORY</span></nav>
    <p class="eyebrow">STORY / THE TIDE REMEMBERS</p>
    <h1 class="page-title" id="page-title">深海<em>回响</em></h1>
    <p class="page-lead">她来自海面之下。那里有她的同胞、她的战场，也有她不愿再提起的失去。</p>
    <div class="page-hero__bottom">
      <div class="badge-row"><span class="badge badge--accent">剧情向</span><span class="badge">含《覆潮之下》《愚人号》相关内容</span></div>
      <span class="badge">READ WITH CARE</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell story-layout">
    <aside class="story-aside" data-reveal>
      <p class="section-index">01 / THE PAST</p>
      <h2 class="section-title">她的故事，<br>从<em>海底</em>开始。</h2>
      <blockquote class="archive-quote">“远方浩瀚蓝色与轻抚土地的白色碎片之下，埋葬着原本我所在乎的一切。”<cite>晋升后交谈 2</cite></blockquote>
      <p>以下内容以角色档案与主线活动中的公开信息为基础，加入少量叙事性整理。不同玩家对剧情的理解可能不同，欢迎保留自己的解读。</p>
      <div class="spoiler-note"><b>SPOILER</b><span>涉及深海猎人、盐风城、愚人号与浊心斯卡蒂的设定。若尚未体验相关剧情，建议先阅读档案页。</span></div>
    </aside>
    <div class="timeline" data-reveal data-reveal-delay="1">
      <article class="timeline-item">
        <span class="timeline-year">ORIGIN / 阿戈尔</span>
        <h3>深海猎人</h3>
        <p>斯卡蒂来自阿戈尔。在成为罗德岛干员之前，她是一名深海猎人——以巨剑与肉体对抗海嗣，把来自海洋的灾祸挡在陆地之外。</p>
        <p>她的战斗经验长达十三年，但更早的履历在档案中是一片空白。巨剑的打造方式难以解释，她的身体数据也远超常规；对医疗部门来说，她是一个无法被轻易归类的特例。</p>
      </article>
      <article class="timeline-item">
        <span class="timeline-year">EXILE / 离开故土</span>
        <h3>赏金猎人</h3>
        <p>灾难之后，她离开阿戈尔，以赏金猎人的身份在陆地上行走。她很少提起过去，也很少在一个地方停留太久。那些与她亲近的人，似乎总会遇到不幸。</p>
        <p>“我的过去可是很糟糕的。”这不是一句自嘲，而是一种预先划清界限的提醒。</p>
      </article>
      <article class="timeline-item">
        <span class="timeline-year">RHODES ISLAND / 罗德岛</span>
        <h3>独行者</h3>
        <p>她接受罗德岛的雇佣，承担单兵任务。战场上，她很少与队友配合，更多时候独自解决目标，让队友收拾残局。普通干员因此对她敬而远之。</p>
        <p>但她并不是无法合作。她只是太清楚，自己的力量会吸引什么样的危险。她把“离我远一点”说得很冷，却把“我来保护你”做得认真。</p>
      </article>
      <article class="timeline-item">
        <span class="timeline-year">UNDER TIDES / 盐风城</span>
        <h3>潮水之下</h3>
        <p>盐风城的事件让海嗣、深海教会与“伊莎玛拉”的名字浮出水面。她被迫再次面对自己的血脉与身份，也再次与歌蕾蒂娅、幽灵鲨站在同一边。</p>
        <p>她曾以为自己是被留下的最后一个深海猎人。后来她发现，海面之下还有同路的人，而海面之上，也有人愿意等她回来。</p>
      </article>
      <article class="timeline-item">
        <span class="timeline-year">STULTIFERA NAVIS / 愚人号</span>
        <h3>同路</h3>
        <p>在愚人号的航程中，深海猎人的命运进一步交汇。她不再只是那个独自挥剑的猎人，也开始学着相信同伴，学着把后背交给别人。</p>
        <p>“我到底是个深海猎人。”这句话既是对身份的确认，也是她重新选择与同胞站在一起的开始。</p>
      </article>
      <article class="timeline-item">
        <span class="timeline-year">IF / 另一种可能</span>
        <h3>浊心</h3>
        <p>如果她选择拥抱海洋，会变成什么样子？浊心斯卡蒂是另一条时间线，也是她内心裂缝的倒影。她不是斯卡蒂的终点，而是一个提醒：一个人可以被潮水带走，也可以选择循光回来。</p>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head" data-reveal>
      <div>
        <p class="section-index">02 / RELATIONS</p>
        <h2 class="section-title">她不是<em>一个人</em>。</h2>
      </div>
      <div class="section-head__aside"><p class="section-lead">即使她总把自己放在队伍之外，仍有一些名字，会让她停下脚步。</p></div>
    </div>
    <div class="relation-grid">
      <article class="relation-card" data-reveal>
        <div class="relation-card__top"><h3>幽灵鲨 / 劳伦缇娜</h3><span>OLD COMRADE</span></div>
        <p>旧日同僚。她记得幽灵鲨真正的职责，也记得要博士帮帮她。即使对方失去了记忆、穿上了修女服，她仍然认得出那个熟悉的影子。</p>
      </article>
      <article class="relation-card" data-reveal data-reveal-delay="1">
        <div class="relation-card__top"><h3>歌蕾蒂娅</h3><span>ABYSSAL HUNTER</span></div>
        <p>同为深海猎人。两人之间有过分歧，也有无法割断的血脉与责任。歌蕾蒂娅是那个会在关键时刻把她拉回来的人。</p>
      </article>
      <article class="relation-card" data-reveal data-reveal-delay="2">
        <div class="relation-card__top"><h3>博士</h3><span>TRUST</span></div>
        <p>她一开始要求你离她两米以上；后来，她说：“这样我不就只能老老实实保护你了吗。”这不是依赖，而是她第一次允许自己拥有一个想要保护的人。</p>
      </article>
      <article class="relation-card" data-reveal data-reveal-delay="3">
        <div class="relation-card__top"><h3>海嗣</h3><span>THE SEA</span></div>
        <p>敌人，也是她必须理解的镜子。“你们就是我们。你的血是我们的血。”海嗣让她恐惧，也让她不得不追问：自己究竟是谁。</p>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head" data-reveal>
      <div>
        <p class="section-index">03 / CONTRADICTION</p>
        <h2 class="section-title">她的<em>矛盾</em>，<br>也是她的温柔。</h2>
      </div>
      <div class="section-head__aside"><p class="section-lead">斯卡蒂的魅力不在于“强”，而在于强大与脆弱同时成立。</p></div>
    </div>
    <div class="contradiction-grid">
      <article class="contradiction-card" data-reveal><b>01 / DISTANCE</b><h3>靠近 = 危险</h3><p>她把疏远当作保护。越在意的人，越要推远；越想留下，越要假装随时可以离开。</p></article>
      <article class="contradiction-card" data-reveal data-reveal-delay="1"><b>02 / BELONGING</b><h3>归属 = 失去</h3><p>她渴望同胞与家，却又害怕再次经历失去。罗德岛给她的不是一个答案，而是一段可以慢慢走的路。</p></article>
      <article class="contradiction-card" data-reveal data-reveal-delay="2"><b>03 / STRENGTH</b><h3>强大 = 孤独</h3><p>她的力量让她能独自解决大多数问题，也让她习惯了不求助。真正的成长，也许是学会说一句“帮我”。</p></article>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="alt-feature" data-reveal>
      <div class="alt-feature__art">
        <img src="assets/img/skadi/alter.webp" alt="浊心斯卡蒂异格立绘：红色舞裙、黑色宽檐帽，身后是海嗣与红色潮水" width="1517" height="1600" loading="lazy">
      </div>
      <div class="alt-feature__copy">
        <p class="eyebrow eyebrow--accent">ALTER / CORRUPTING HEART</p>
        <h2>浊心斯卡蒂<br>另一种潮声。</h2>
        <p>如果潮水吞没了最后一束光，她会不会也变成海的一部分？异格不是另一个角色，而是同一个灵魂在极端假设下的回声。她仍然记得歌，只是那首歌已经不再属于陆地。</p>
        <blockquote class="archive-quote">“你以前觉得我们彻底离开海水就没法生存？不是的。”<cite>浊心斯卡蒂 / 交谈 1</cite></blockquote>
        <div class="btn-row"><a class="btn" href="gallery.html">查看异格影像</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section closing">
  <div class="shell closing__inner">
    <div data-reveal>
      <p class="eyebrow">THE TIDE REMEMBERS</p>
      <h2 class="display-title">她走过漫长的黑暗，<br>却仍然愿意<em>相信光</em>。</h2>
    </div>
    <div class="btn-row" data-reveal data-reveal-delay="1"><a class="btn btn--solid" href="voices.html">听她说话</a></div>
  </div>
</section>
"""


COMBAT_BODY = """
<section class="page-hero page-hero--tide" aria-labelledby="page-title">
  <span class="page-hero__ghost" aria-hidden="true">DRE</span>
  <div class="shell">
    <nav class="breadcrumb" aria-label="面包屑"><a href="index.html">INDEX</a><span>/</span><span>COMBAT FILE</span></nav>
    <p class="eyebrow">COMBAT FILE / DRE / FEARLESS</p>
    <h1 class="page-title" id="page-title">战斗<em>手册</em></h1>
    <p class="page-lead">她不是一名需要复杂操作的干员。把最危险的目标交给她，然后相信她能回来。</p>
    <div class="page-hero__bottom">
      <div class="badge-row"><span class="badge badge--accent">近卫 / 无畏者</span><span class="badge">阻挡 1</span><span class="badge">再部署 70s</span></div>
      <span class="badge badge--cyan">E2 · LV.90 · TRUST</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head" data-reveal>
      <div>
        <p class="section-index">01 / BASE STATS</p>
        <h2 class="section-title">把最危险的目标，<br>交给<em>一个人</em>。</h2>
      </div>
      <div class="section-head__aside"><p class="section-lead">高攻击与高生命让她拥有极强的单兵处理能力；阻挡数与法抗的短板，则要求博士替她选好位置。</p></div>
    </div>
    <dl class="stat-strip" data-reveal>
      <div><dt>生命上限</dt><dd>3866</dd></div>
      <div><dt>攻击</dt><dd>1015<small>+80</small></dd></div>
      <div><dt>防御</dt><dd>263<small>+40</small></dd></div>
      <div><dt>法术抗性</dt><dd>0</dd></div>
    </dl>
    <p class="combat-note">数据基准：精英二 90 级、满信赖、无潜能、无模组。部署费用 17→19，阻挡数 1，攻击间隔 1.5s，再部署 70s。</p>

    <div class="subhead"><h2>技能</h2><span>SKILLS / MASTER 3</span></div>
    <div class="skill-tabs" data-tabs>
      <div class="tab-list" role="tablist" aria-label="斯卡蒂技能">
        <button class="tab-btn" type="button" role="tab" id="tab-s1" aria-controls="panel-s1" aria-selected="true">S1 / 迅捷打击·γ型</button>
        <button class="tab-btn" type="button" role="tab" id="tab-s2" aria-controls="panel-s2" aria-selected="false" tabindex="-1">S2 / 跃浪击</button>
        <button class="tab-btn" type="button" role="tab" id="tab-s3" aria-controls="panel-s3" aria-selected="false" tabindex="-1">S3 / 涌潮悲歌</button>
      </div>
      <div class="tab-panel" role="tabpanel" id="panel-s1" aria-labelledby="tab-s1">
        <div class="skill-heading"><h3>迅捷打击·γ型</h3><span>AUTO / MANUAL / 35s</span></div>
        <p class="skill-desc">最稳定的一技能。攻击力与攻击速度同时提升，适合日常清杂与持续输出；不需要精确卡轴，也不依赖队友配合。</p>
        <dl class="skill-numbers">
          <div><dt>攻击力</dt><dd>+45%</dd></div>
          <div><dt>攻击速度</dt><dd>+45</dd></div>
          <div><dt>持续</dt><dd>35s</dd></div>
          <div><dt>消耗 / 初始</dt><dd>35 / 15</dd></div>
        </dl>
        <p class="use-case"><b>USE CASE</b><span>日常推图、清杂、稳定站场。专精收益平滑，但不是最优先。</span></p>
      </div>
      <div class="tab-panel" role="tabpanel" id="panel-s2" aria-labelledby="tab-s2" hidden>
        <div class="skill-heading"><h3>跃浪击</h3><span>PASSIVE / ON DEPLOY</span></div>
        <p class="skill-desc">部署后一段时间内攻击力大幅提升。她是空降单切的典型代表：落在精英敌人面前，用极短的窗口解决目标，然后撤退等待下一次部署。</p>
        <dl class="skill-numbers">
          <div><dt>攻击力</dt><dd>+170%</dd></div>
          <div><dt>持续</dt><dd>30s</dd></div>
          <div><dt>触发</dt><dd>部署后</dd></div>
          <div><dt>专精</dt><dd>M3</dd></div>
        </dl>
        <p class="use-case"><b>USE CASE</b><span>空降单切、处理高威胁精英、拆硬目标。搭配再部署缩减模组，循环更快。</span></p>
      </div>
      <div class="tab-panel" role="tabpanel" id="panel-s3" aria-labelledby="tab-s3" hidden>
        <div class="skill-heading"><h3>涌潮悲歌</h3><span>AUTO / MANUAL / 50s</span></div>
        <p class="skill-desc">同时提升攻击力、防御力与生命上限，让她从“单切工具”变成可以站场的重装型近卫。技能期间的面板极高，但启动费用也高，需要提前规划。</p>
        <dl class="skill-numbers">
          <div><dt>攻击 / 防御 / 生命</dt><dd>+130%</dd></div>
          <div><dt>持续</dt><dd>50s</dd></div>
          <div><dt>消耗 / 初始</dt><dd>90 / 70</dd></div>
          <div><dt>专精</dt><dd>M3</dd></div>
        </dl>
        <p class="use-case"><b>USE CASE</b><span>高压波次站场、阻挡高攻目标。需要治疗或减伤支持，避免技能真空期倒下。</span></p>
      </div>
    </div>

    <div class="subhead"><h2>天赋与模组</h2><span>TALENTS / MODULES</span></div>
    <div class="data-grid">
      <article class="data-card" data-reveal>
        <span class="data-card__label">TALENT 01</span>
        <h3>深海掠食者</h3>
        <p>精英二：编入队伍时，所有【深海猎人】干员的攻击力 +14%。她不仅是输出，也是深海体系的核心增益之一。</p>
      </article>
      <article class="data-card" data-reveal data-reveal-delay="1">
        <span class="data-card__label">TALENT 02</span>
        <h3>迅捷出击</h3>
        <p>精英二：自身再部署时间 -10 秒。配合 S2 的空降单切，让她能更频繁地回到战场。</p>
      </article>
    </div>
    <div class="module-grid">
      <article class="module-card" data-reveal>
        <span class="module-card__tag">DRE-X</span>
        <span class="data-card__label">MODULE / 往日残梦</span>
        <h3>为单切而生</h3>
        <p>攻击被阻挡的敌人时，攻击力提升至 115%；迅捷出击进一步缩短再部署时间（2 级 -20s / 3 级 -30s）。</p>
        <ul><li>适合空降单切与高频再部署</li><li>更强调“落地、解决、撤退”的节奏</li><li>对阻挡目标有额外伤害收益</li></ul>
      </article>
      <article class="module-card" data-reveal data-reveal-delay="1">
        <span class="module-card__tag" style="background:var(--cyan);color:var(--bg)">DRE-Y</span>
        <span class="data-card__label">MODULE / 潮湿的剑袋</span>
        <h3>为深海队而生</h3>
        <p>深海掠食者强化为全队攻击 +18% / +22%，并额外提供生命 +10% / +20%；特性追加一次免死回复，但会降低生命上限。</p>
        <ul><li>适合深海猎人体系与站场</li><li>把个人强度转化为团队增益</li><li>免死效果每场只触发一次，注意时机</li></ul>
      </article>
    </div>

    <div class="subhead"><h2>定位与用法</h2><span>ROLE / TACTICS</span></div>
    <div class="role-grid">
      <article class="role-card" data-reveal><span class="role-card__num">01 / DROP</span><h3>空降单切</h3><p>把 S2 斯卡蒂直接放在精英敌人脸上，利用落地后的高攻击窗口解决目标。打完就撤，等下一次再部署。</p></article>
      <article class="role-card" data-reveal data-reveal-delay="1"><span class="role-card__num">02 / HOLD</span><h3>高压站场</h3><p>S3 提供极高的攻击、防御与生命加成，适合阻挡高攻目标或拖住波次。需要治疗与减伤支持。</p></article>
      <article class="role-card" data-reveal data-reveal-delay="2"><span class="role-card__num">03 / ABYSS</span><h3>深海核心</h3><p>Y 模组让她的天赋覆盖全队。与歌蕾蒂娅、幽灵鲨等深海猎人同队时，她既是输出，也是增益节点。</p></article>
    </div>

    <div class="subhead"><h2>培养顺序</h2><span>TRAINING PRIORITY</span></div>
    <div class="data-grid" style="grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr)">
      <ol class="check-list" data-reveal>
        <li><span class="num">01</span><strong>精英二 90 级</strong><small>核心属性</small></li>
        <li><span class="num">02</span><strong>S2 跃浪击 专三</strong><small>空降单切</small></li>
        <li><span class="num">03</span><strong>S3 涌潮悲歌 专三</strong><small>站场强化</small></li>
        <li><span class="num">04</span><strong>按玩法选择模组</strong><small>X 单切 / Y 深海队</small></li>
        <li><span class="num">05</span><strong>信赖 100% / 200%</strong><small>解锁档案与台词</small></li>
      </ol>
      <aside class="data-card" data-reveal data-reveal-delay="1">
        <span class="data-card__label">ABYSSAL SYNERGY</span>
        <h3>同队建议</h3>
        <p>深海猎人体系能让她的天赋收益最大化；即使不组深海队，她也可以作为独立的空降单切使用。</p>
        <div class="chip-row">
          <span class="chip">歌蕾蒂娅</span><span class="chip">幽灵鲨</span><span class="chip">归溟幽灵鲨</span><span class="chip">乌尔比安</span><span class="chip">治疗 / 减伤</span>
        </div>
      </aside>
    </div>
    <p class="data-source">数据参考：<a class="text-link" href="https://prts.wiki/w/%E6%96%AF%E5%8D%A1%E8%92%82" target="_blank" rel="noopener noreferrer">PRTS 明日方舟中文 Wiki</a>（2026-11 查询）。技能数值为专精三；模组效果为 3 级描述。游戏版本更新后请以游戏内实际数据为准。本页仅作角色介绍与课程设计，不构成抽取或练度建议。</p>
  </div>
</section>
"""


GALLERY_ITEMS = [
    {
        "full": "assets/img/gallery/poster-01.jpg",
        "thumb": "assets/img/gallery/poster-01-thumb.jpg",
        "alt": "斯卡蒂精英二立绘海报，银白长发与巨剑，深色海面背景",
        "caption": "斯卡蒂 / 精英二",
        "meta": "ILLUSTRATION · E2",
        "category": "立绘",
        "w": 700,
        "h": 875,
    },
    {
        "full": "assets/img/gallery/poster-02.jpg",
        "thumb": "assets/img/gallery/poster-02-thumb.jpg",
        "alt": "斯卡蒂初始立绘海报，站在星空与山脊前",
        "caption": "潮汐来客 / 初始",
        "meta": "ILLUSTRATION · E0",
        "category": "立绘",
        "w": 700,
        "h": 875,
    },
    {
        "full": "assets/img/gallery/poster-03.jpg",
        "thumb": "assets/img/gallery/poster-03-thumb.jpg",
        "alt": "斯卡蒂驭浪皮肤海报，沙滩与遮阳伞，白色泳装",
        "caption": "驭浪 / 珊瑚海岸",
        "meta": "OUTFIT · WR04",
        "category": "衣装",
        "w": 700,
        "h": 875,
    },
    {
        "full": "assets/img/gallery/poster-04.jpg",
        "thumb": "assets/img/gallery/poster-04-thumb.jpg",
        "alt": "斯卡蒂下一顿午茶皮肤海报，室内午后与红茶",
        "caption": "下一顿午茶 / 玛尔特",
        "meta": "OUTFIT · V",
        "category": "衣装",
        "w": 700,
        "h": 875,
    },
    {
        "full": "assets/img/gallery/poster-05.jpg",
        "thumb": "assets/img/gallery/poster-05-thumb.jpg",
        "alt": "浊心斯卡蒂异格海报，红色舞裙与海嗣",
        "caption": "浊心斯卡蒂 / 异格",
        "meta": "ALTER · IF",
        "category": "异格",
        "w": 700,
        "h": 875,
    },
    {
        "full": "assets/img/gallery/poster-06.jpg",
        "thumb": "assets/img/gallery/poster-06-thumb.jpg",
        "alt": "听潮主题海报，雾中的山脊与声呐圆环",
        "caption": "听潮 / 视觉练习",
        "meta": "IMPRESSION · TIDE",
        "category": "印象",
        "w": 700,
        "h": 875,
    },
    {
        "full": "assets/img/gallery/mood-01.jpg",
        "thumb": "assets/img/gallery/mood-01.jpg",
        "alt": "雾气笼罩的绿色山脊与远处海岸",
        "caption": "雾从海面升起",
        "meta": "IMPRESSION · 01",
        "category": "印象",
        "w": 1600,
        "h": 1067,
    },
    {
        "full": "assets/img/gallery/mood-02.jpg",
        "thumb": "assets/img/gallery/mood-02.jpg",
        "alt": "星空下的雪山剪影",
        "caption": "星夜航线",
        "meta": "IMPRESSION · 02",
        "category": "印象",
        "w": 1600,
        "h": 1067,
    },
    {
        "full": "assets/img/gallery/mood-03.jpg",
        "thumb": "assets/img/gallery/mood-03.jpg",
        "alt": "俯瞰海岸的蓝绿色海水与白色浪花",
        "caption": "潮汐的纹理",
        "meta": "IMPRESSION · 03",
        "category": "印象",
        "w": 1600,
        "h": 1067,
    },
    {
        "full": "assets/img/gallery/official-wallpaper.jpg",
        "thumb": "assets/img/gallery/official-wallpaper.jpg",
        "alt": "明日方舟珊瑚海岸斯卡蒂官方视觉图",
        "caption": "珊瑚海岸 / 官方视觉",
        "meta": "OFFICIAL · PROMO",
        "category": "官方",
        "w": 2000,
        "h": 1125,
    },
]


def gallery_items_html() -> str:
    cards = []
    for index, item in enumerate(GALLERY_ITEMS, start=1):
        cards.append(
            f"""
      <figure class="gallery-card" data-category="{item['category']}">
        <button class="gallery-btn" type="button" data-full="{item['full']}" data-caption="{item['caption']}" data-meta="{item['meta']}" aria-label="查看大图：{item['caption']}">
          <img src="{item['thumb']}" alt="{item['alt']}" width="{item['w']}" height="{item['h']}" loading="lazy">
          <span class="gallery-btn__overlay"><span>{item['category']} / {item['meta']}</span><b>VIEW ↗</b></span>
        </button>
        <figcaption class="gallery-caption"><strong>{item['caption']}</strong><span>{item['meta']}</span></figcaption>
      </figure>"""
        )
    return "\n".join(cards)


GALLERY_BODY = f"""
<section class="page-hero page-hero--night" aria-labelledby="page-title">
  <span class="page-hero__ghost" aria-hidden="true">IMAGE</span>
  <div class="shell">
    <nav class="breadcrumb" aria-label="面包屑"><a href="index.html">INDEX</a><span>/</span><span>VISUAL ARCHIVE</span></nav>
    <p class="eyebrow">VISUAL ARCHIVE / LIGHT &amp; TIDE</p>
    <h1 class="page-title" id="page-title">影像<em>档案</em></h1>
    <p class="page-lead">官方立绘、衣装、异格与氛围印象。有些画面记录的是她，有些画面记录的是我们看见她时的心情。</p>
    <div class="page-hero__bottom">
      <div class="badge-row"><span class="badge badge--accent">10 张影像</span><span class="badge">官方立绘 + 印象练习</span></div>
      <span class="badge badge--cyan">CLICK TO ENLARGE</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="filter-bar" data-filter-group data-filter-target="#gallery-grid">
      <button class="filter-btn" type="button" data-filter="all" aria-pressed="true">全部</button>
      <button class="filter-btn" type="button" data-filter="立绘" aria-pressed="false">立绘</button>
      <button class="filter-btn" type="button" data-filter="衣装" aria-pressed="false">衣装</button>
      <button class="filter-btn" type="button" data-filter="异格" aria-pressed="false">异格</button>
      <button class="filter-btn" type="button" data-filter="官方" aria-pressed="false">官方</button>
      <button class="filter-btn" type="button" data-filter="印象" aria-pressed="false">印象</button>
      <span class="filter-count"><span data-filter-count>10</span> ITEMS</span>
      <span class="filter-status visually-hidden" data-filter-status aria-live="polite"></span>
    </div>
    <div class="gallery-grid" id="gallery-grid">
{gallery_items_html()}
    </div>
    <p class="gallery-empty" data-empty hidden>这个分类暂时没有影像。</p>
    <p class="data-source">官方立绘与官方视觉图版权归鹰角网络 / Hypergryph 所有，仅作非商业课程展示。印象图为 Unsplash 授权摄影（摄影：Unsplash 社区），经调色与排版后作为氛围配图使用，不代表游戏内设定。来源与许可见 README。</p>
  </div>
</section>

<dialog class="lightbox" data-lightbox aria-label="影像查看器">
  <div class="lightbox-inner">
    <button class="lightbox-close" type="button" data-lightbox-close aria-label="关闭影像查看器">×</button>
    <button class="lightbox-nav lightbox-prev" type="button" data-lightbox-prev aria-label="上一张影像">←</button>
    <figure class="lightbox-figure">
      <img data-lightbox-image src="" alt="">
      <figcaption><strong data-lightbox-caption></strong><span data-lightbox-meta></span></figcaption>
    </figure>
    <button class="lightbox-nav lightbox-next" type="button" data-lightbox-next aria-label="下一张影像">→</button>
    <span class="lightbox-count" data-lightbox-count></span>
  </div>
</dialog>
"""


VOICE_FEATURE = [
    ("为了你的安全着想，最好离我两米以上，也不要和我说话……我可不想你被冲着我来的危险伤到。", "任命助理 / 初始"),
    ("我的头发很长，很好看？啊，嗯，谢谢……要不要摸摸看？我的头发还是挺柔软的。", "交谈 2 / 初始"),
    ("你这人，怎么这么执着，这样我不就只能老老实实保护你了吗。", "晋升后交谈 1 / 精英一"),
    ("远方浩瀚蓝色与轻抚土地的白色碎片之下，埋葬着原本我所在乎的一切。", "晋升后交谈 2 / 精英二"),
    ("睡着了？睡吧，博士，得做个干燥的好梦哟。", "闲置 / 初始"),
]

VOICE_CARDS = [
    ("初始", "独白", "斯卡蒂，赏金猎人。你真要签下我？我可是那种，会给你带来灾祸的人哦。", "报到 / 初始"),
    ("初始", "日常", "为了你的安全着想，最好离我两米以上，也不要和我说话……我可不想你被冲着我来的危险伤到。", "任命助理 / 初始"),
    ("初始", "日常", "我的头发很长，很好看？啊，嗯，谢谢……要不要摸摸看？我的头发还是挺柔软的。", "交谈 2 / 初始"),
    ("精英一", "信赖", "你这人，怎么这么执着，这样我不就只能老老实实保护你了吗。", "晋升后交谈 1 / 精英一"),
    ("精英二", "独白", "远方浩瀚蓝色与轻抚土地的白色碎片之下，埋葬着原本我所在乎的一切。我很害怕，害怕厄运会再次夺走我重要的人，所以我才会选择逃离，我不希望我珍视的人……因我而受伤。", "晋升后交谈 2 / 精英二"),
    ("信赖 100%", "信赖", "根据传说，我的族裔已经和那些灾祸战斗了无数年。说不定，我们也帮你们这些城市人把灾祸挡在了陆地之外……所以说，是不是该请我喝一杯，好好谢谢我？", "信赖提升后交谈 2 / 信赖 100%"),
    ("信赖 200%", "独白", "当你历经漫长黑暗、终于浮出海面——睁开眼睛的刹那，灿烂星空滴落眼眶、无垠波浪拂过面颊，眼泪和家的味道，都是咸的。相比下，罗德岛的浴缸真是又窄又浅……我一定得带你去试试才行。", "信赖提升后交谈 3 / 信赖 200%"),
    ("初始", "日常", "睡着了？睡吧，博士，得做个干燥的好梦哟。", "闲置 / 初始"),
    ("初始", "战场", "呯呯地冲过去，咚地打倒敌人，啪地解决掉——原来你们是这么战斗的，我记住啦。", "观看作战记录 / 初始"),
    ("精英二", "信赖", "这样渴求我的力量，真的让我很困扰……如果你真的无所畏惧，那么做好准备，和我一起直面无边无际的黑暗吧。", "精英化晋升 2 / 精英二"),
    ("信赖", "日常", "离我那么近……我，我可没有能完全保护你的自信！", "信赖触摸 / 信赖"),
]


def voice_feature_html() -> str:
    slides = []
    for index, (quote, cite) in enumerate(VOICE_FEATURE):
        hidden = "" if index == 0 else " hidden"
        slides.append(
            f"""
      <div class="quote-slide" data-quote-slide{hidden}>
        <blockquote>“{quote}”</blockquote>
        <cite>{cite}</cite>
      </div>"""
        )
    return "\n".join(slides)


def voice_cards_html() -> str:
    cards = []
    for index, (condition, category, quote, cite) in enumerate(VOICE_CARDS, start=1):
        cards.append(
            f"""
      <article class="voice-card" data-category="{category}">
        <div class="voice-card__top"><span>{category} / {condition}</span><small>LOG {index:02d}</small></div>
        <blockquote id="voice-{index}">“{quote}”</blockquote>
        <div class="voice-card__bottom">
          <cite>{cite}</cite>
          <button class="copy-btn" type="button" data-copy-target="#voice-{index}" aria-label="复制台词：{cite}">复制</button>
        </div>
      </article>"""
        )
    return "\n".join(cards)


VOICES_BODY = f"""
<section class="page-hero page-hero--tide" aria-labelledby="page-title">
  <span class="page-hero__ghost" aria-hidden="true">VOICE</span>
  <div class="shell voice-hero">
    <div>
      <nav class="breadcrumb" aria-label="面包屑"><a href="index.html">INDEX</a><span>/</span><span>VOICE LOG</span></nav>
      <p class="eyebrow">VOICE LOG / TRUST &amp; TIDE</p>
      <h1 class="page-title" id="page-title">语音<em>记录</em></h1>
      <p class="page-lead">她说的每一句话，都像隔着一段潮水。要靠近一点，才能听清那些没有说出口的部分。</p>
      <div class="page-hero__bottom">
        <div class="badge-row"><span class="badge badge--accent">中文台词节选</span><span class="badge">按信赖阶段整理</span></div>
        <span class="badge badge--cyan">CV / 张琦</span>
      </div>
    </div>
    <div class="voice-avatar" aria-hidden="true">
      <img src="assets/img/skadi/avatar-feature.jpg" alt="" width="520" height="520" loading="eager">
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="voice-feature" data-quote-rotator data-autoplay="true" data-reveal>
      <p class="eyebrow">FEATURED LINE / 01</p>
      <div>
{voice_feature_html()}
      </div>
      <div class="quote-controls">
        <button class="circle-btn" type="button" data-quote-prev aria-label="上一句台词">←</button>
        <button class="circle-btn" type="button" data-quote-next aria-label="下一句台词">→</button>
        <span class="quote-count" data-quote-count>01 / 05</span>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head" data-reveal>
      <div>
        <p class="section-index">01 / ALL LINES</p>
        <h2 class="section-title">从“离我远一点”，<br>到“<em>我来保护你</em>”。</h2>
      </div>
      <div class="section-head__aside"><p class="section-lead">按场景与信赖阶段整理的台词节选。完整语音、语气与停顿，仍然要在游戏里听。</p></div>
    </div>
    <div class="filter-bar" data-filter-group data-filter-target="#voice-grid">
      <button class="filter-btn" type="button" data-filter="all" aria-pressed="true">全部</button>
      <button class="filter-btn" type="button" data-filter="日常" aria-pressed="false">日常</button>
      <button class="filter-btn" type="button" data-filter="信赖" aria-pressed="false">信赖</button>
      <button class="filter-btn" type="button" data-filter="独白" aria-pressed="false">独白</button>
      <button class="filter-btn" type="button" data-filter="战场" aria-pressed="false">战场</button>
      <span class="filter-count"><span data-filter-count>11</span> LINES</span>
      <span class="filter-status visually-hidden" data-filter-status aria-live="polite"></span>
    </div>
    <div class="voice-grid" id="voice-grid">
{voice_cards_html()}
    </div>
    <div class="voice-note" style="margin-top:24px">
      <b>NOTE</b>
      <span>本页仅收录文字台词，不提供语音试听。角色台词、语音与官方立绘版权归鹰角网络 / Hypergryph 所有。完整语音请前往游戏内干员档案收听。</span>
    </div>
    <div class="data-grid" style="margin-top:22px">
      <article class="data-card" data-reveal>
        <span class="data-card__label">VOICE CAST</span>
        <h3>声音的四种温度</h3>
        <p>中文：张琦 · 日文：佐藤利奈 · 英文：Cristina Vee · 韩文：金拿燏。不同语言里的她，有着不一样的冷与软。</p>
      </article>
      <article class="data-card" data-reveal data-reveal-delay="1">
        <span class="data-card__label">A SMALL NOTE</span>
        <h3>把“冷淡”听完整</h3>
        <p>她说话常常先划清距离，再把关心藏进后半句。越往后听，越能发现那些“别靠近”的句子，其实都在说“别受伤”。</p>
      </article>
    </div>
  </div>
</section>
"""


NOT_FOUND_BODY = """
<section class="notfound">
  <div class="notfound__inner">
    <p class="notfound__signal"><i aria-hidden="true"></i> SIGNAL LOST / NO RESPONSE</p>
    <p class="notfound__code">404</p>
    <h1>这段潮声，断在了半途。</h1>
    <p>你寻找的页面不在当前档案里。可能是链接写错了，也可能是它被潮水带走了。回到首页，重新接入信号。</p>
    <div class="btn-row">
      <a class="btn btn--solid" href="index.html">返回首页</a>
      <a class="btn" href="profile.html">打开干员档案</a>
    </div>
  </div>
</section>
"""


PAGES = {
    "index.html": page(
        "斯卡蒂 · 深海档案｜潮汐之下，仍在歌唱",
        "一个关于《明日方舟》干员斯卡蒂的非官方角色介绍站：干员档案、深海回响、战斗手册、影像与语音记录。",
        "home",
        HOME_BODY,
    ),
    "profile.html": page(
        "干员档案｜斯卡蒂 · 深海档案",
        "斯卡蒂干员档案：基础资料、综合体检测试、精英二属性、档案摘录与信物。",
        "profile",
        PROFILE_BODY,
    ),
    "story.html": page(
        "深海回响｜斯卡蒂 · 深海档案",
        "从阿戈尔到罗德岛，从盐风城到愚人号：斯卡蒂与深海猎人的故事。",
        "story",
        STORY_BODY,
    ),
    "combat.html": page(
        "战斗手册｜斯卡蒂 · 深海档案",
        "斯卡蒂战斗数据：技能、天赋、模组、定位与培养顺序。",
        "combat",
        COMBAT_BODY,
    ),
    "gallery.html": page(
        "影像档案｜斯卡蒂 · 深海档案",
        "斯卡蒂官方立绘、衣装、异格与氛围影像，支持分类筛选与大图查看。",
        "gallery",
        GALLERY_BODY,
    ),
    "voices.html": page(
        "语音记录｜斯卡蒂 · 深海档案",
        "斯卡蒂中文台词节选：从初始到信赖 200%，按场景分类查看并复制。",
        "voices",
        VOICES_BODY,
    ),
    "404.html": page(
        "信号中断｜斯卡蒂 · 深海档案",
        "页面不存在。回到深海档案首页。",
        "",
        NOT_FOUND_BODY,
    ),
}


def main() -> None:
    for filename, html in PAGES.items():
        (ROOT / filename).write_text(html, encoding="utf-8")
        print("wrote", filename, len(html))


if __name__ == "__main__":
    main()
