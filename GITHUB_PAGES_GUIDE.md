# GitHub Pages 保姆级上传教程

本项目已经打包为 [skadi-archive.zip](skadi-archive.zip)。下面按“从零开始”的顺序操作即可。

> 目标：把网站发布成类似
> `https://你的用户名.github.io/skadi-archive/`
> 的公开网址。

---

## 第 0 步：先确认你拿到了什么

你需要的文件是：

```text
skadi-archive.zip
```

**不是**直接上传这个 ZIP 压缩包。GitHub Pages 不会自动解压它，必须先解压，再上传里面的文件。

---

## 第 1 步：解压 ZIP

### Windows

1. 找到 `skadi-archive.zip`。
2. 右键 → **全部解压缩 / Extract All**。
3. 选择一个容易找到的位置，例如桌面。
4. 打开解压后的文件夹。

解压后应该直接看到：

```text
index.html
profile.html
story.html
combat.html
gallery.html
voices.html
404.html
assets/
README.md
CREDITS.md
.nojekyll
```

### 关键检查

打开解压后的文件夹，**第一层**必须能看到 `index.html`。

正确：

```text
skadi-archive/
├─ index.html
├─ assets/
└─ 其它页面
```

错误：

```text
skadi-archive/
└─ skadi-archive/
   ├─ index.html
   └─ assets/
```

如果出现“文件夹套文件夹”，进入里面那一层再上传。

---

## 第 2 步：注册 / 登录 GitHub

1. 打开 https://github.com
2. 没有账号：点击 **Sign up**，用邮箱注册。
3. 有账号：点击 **Sign in** 登录。
4. 建议完成邮箱验证，否则部分功能可能受限。

---

## 第 3 步：新建一个仓库

1. 登录后，点击右上角 **+**。
2. 选择 **New repository**。
3. 按下表填写：

| 项目 | 填写 |
| --- | --- |
| Repository name | `skadi-archive`（也可以叫别的英文名） |
| Description | 可选，例如 `Skadi fan site` |
| Public / Private | 必须选 **Public** |
| Add a README file | **不要勾选** |
| Add .gitignore | **不要选** |
| Choose a license | **不要选** |

4. 点击 **Create repository**。

> 为什么选 Public？
> GitHub Pages 免费账户通常只支持公开仓库。作业展示也需要公开访问。

---

## 第 4 步：上传网站文件

进入新建好的空仓库后：

1. 点击页面中间的 **uploading an existing file**，或点击 **Add file → Upload files**。
2. 打开你解压后的网站文件夹。
3. 全选里面的**文件和文件夹**：
   - Windows：`Ctrl + A`
   - Mac：`Command + A`
4. 把它们拖进 GitHub 的上传区域。
5. 等待文件列表全部出现（本项目约 45 个文件、6.8 MB）。
6. 在下方 **Commit changes** 输入框里写：

```text
Upload Skadi website
```

7. 点击绿色按钮 **Commit changes**。

### 上传后必须检查根目录

回到仓库首页，文件列表第一层应该能看到：

```text
index.html
profile.html
story.html
combat.html
gallery.html
voices.html
404.html
assets
README.md
CREDITS.md
.nojekyll
```

如果只看到 `skadi-archive` 文件夹，说明你把整个文件夹传上去了，这是**错误**的。需要把里面的文件移到仓库根目录。

### 隐藏文件看不到怎么办？

`.nojekyll` 和 `.gitignore` 是点开头的文件。Windows 资源管理器如果看不到：

1. 打开资源管理器 → **查看**。
2. 勾选 **隐藏的项目 / Hidden items**。
3. 再全选上传。

如果实在找不到 `.nojekyll`，先上传其它文件也能运行；但建议保留它。

---

## 第 5 步：开启 GitHub Pages

1. 在仓库页面顶部点击 **Settings**（设置）。
2. 左侧菜单找到 **Pages**。
3. 在 **Build and deployment** 区域：
   - **Source** 选择 **Deploy from a branch**
   - **Branch** 选择 **main**
   - 文件夹选择 **/ (root)**
4. 点击 **Save**。

> 如果左侧没有 Pages，先确认仓库是 Public，并且你是仓库所有者。

---

## 第 6 步：等待并访问

保存后：

1. 页面顶部会出现类似提示：
   `Your site is live at https://你的用户名.github.io/skadi-archive/`
2. 第一次发布通常需要 **1—3 分钟**。
3. 点击 **Visit site**，或手动打开这个网址。

### 网址规则

| 仓库名 | 网址 |
| --- | --- |
| `skadi-archive` | `https://用户名.github.io/skadi-archive/` |
| `用户名.github.io` | `https://用户名.github.io/` |

作业提交时，交 **Pages 网址**，不是 `github.com/用户名/仓库名` 的仓库地址。

---

## 第 7 步：检查是否真的成功

打开网址后检查：

- [ ] 首页出现“潮汐之下，仍在歌唱”
- [ ] 顶部导航能进入档案、故事、战斗、影像、语音
- [ ] 图片能显示，页面有深色背景和红色强调色
- [ ] 手机浏览器打开也正常
- [ ] 刷新后没有 404
- [ ] 随便点一个页面，网址里带有 `skadi-archive/...`

建议把网址发给同学或老师，用另一台设备打开测试。

---

## 第 8 步：以后如何更新

### 方法 A：网页上传覆盖

1. 在仓库首页点击 **Add file → Upload files**。
2. 上传修改后的同名文件（例如新的 `index.html`）。
3. 提交 commit。
4. Pages 会自动重新构建，等 1—3 分钟刷新。

### 方法 B：GitHub Desktop（文件多时推荐）

1. 安装 GitHub Desktop。
2. `File → Clone repository`，选择你的仓库。
3. 把本地文件复制进克隆目录。
4. 在 GitHub Desktop 中填写提交说明，点击 **Commit to main**。
5. 点击 **Push origin**。

---

## 常见问题排查

### 1. 打开网址显示 404

依次检查：

1. **Settings → Pages** 是否已经 Save。
2. Branch 是否是 `main`，目录是否是 `/ (root)`。
3. 仓库根目录是否真的有 `index.html`。
4. 文件名是否是小写 `index.html`，不是 `Index.html`。
5. 是否刚保存，等待 1—3 分钟。
6. 打开仓库的 **Actions** 标签，看 `pages build and deployment` 是否成功。

### 2. 页面能打开，但没有样式 / 图片全裂

通常是 `assets` 文件夹位置不对。

正确：

```text
index.html
assets/css/style.css
assets/img/skadi/e2.webp
```

错误：

```text
skadi-archive/index.html
skadi-archive/assets/...
```

或者：

```text
assets/css/css/style.css
```

请保持 `assets` 在仓库根目录，且不要改文件夹名。

### 3. 只显示 README，不显示网站

说明 `index.html` 不在根目录，或者名字不对。GitHub Pages 默认优先加载根目录的 `index.html`。

### 4. 修改后网页没变化

- 确认已经 **Commit changes**。
- 等 1—3 分钟。
- 用 `Ctrl + F5` 强制刷新。
- 检查 Actions 是否构建成功。

### 5. 上传时提示文件太多

本项目只有 45 个文件，正常一次能传完。如果浏览器卡住：

- 分批上传：先传 HTML，再传 `assets`。
- 或使用 GitHub Desktop。

### 6. 中文文件名 / 大小写问题

本项目所有资源路径都是小写英文，不要手动改成中文或大写。GitHub Pages 区分大小写。

### 7. 私有仓库可以发布吗

免费账户通常不行。把仓库改成 **Public**：
`Settings → General → Danger Zone → Change visibility`。

---

## 提交作业时建议写什么

```text
作品名称：深海档案 · 斯卡蒂角色介绍网站
页面数量：6 个内容页 + 自定义 404 页
技术：HTML5 + CSS3 + 原生 JavaScript
发布地址：https://你的用户名.github.io/skadi-archive/
仓库地址：https://github.com/你的用户名/skadi-archive
```

---

## 最后的安全提醒

- 不要把 GitHub 密码、验证码、个人访问令牌发给任何人。
- 如果让别人帮你发布，使用 GitHub 的设备码登录，不要直接给密码。
- 发布后检查页脚和 [CREDITS.md](CREDITS.md) 中的版权说明是否保留。

---

## 一页纸速查

```text
解压 ZIP
→ 登录 GitHub
→ New repository（Public，不勾 README）
→ Add file → Upload files
→ 上传解压后的全部内容
→ Commit changes
→ Settings → Pages
→ Deploy from a branch
→ main / (root)
→ Save
→ 等 1—3 分钟
→ 打开 https://用户名.github.io/仓库名/
```

如果卡在某一步，把**当前页面截图**或**报错文字**发给我，我可以按你看到的界面继续带你操作。
