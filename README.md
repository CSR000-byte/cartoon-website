# 🐱🚀 卡创 · 星际小猫号

> ✨ *一封写给所有童心未泯之人的情书* ✨

![卡创](https://img.shields.io/badge/卡创-星际小猫号-6C5CE7?style=for-the-badge&logo=data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🐱</text></svg>)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

---

## 📦 项目简介

**卡创 · 星际小猫号** 是一个梦幻太空猫咪主题的品牌形象网站。在这里，一群可爱的星际小动物乘坐着星际小猫号飞船，穿越银河、探索星球、收集星光。

> 🎯 **品牌理念：** 用最柔软的方式，治愈每一个疲惫的心灵。真诚、可爱、想象力无边！

---

## 🚀 在线访问

🌐 **GitHub Pages：** [https://你的用户名.github.io/cartoon-website](https://你的用户名.github.io/cartoon-website)

> 💡 部署后请将上面的链接替换为实际的 GitHub Pages URL。

---

## 📁 项目结构

```
cartoon-website/
├── 📄 index.html              # 🏠 首页（英雄区 + 特色展示）
├── 📄 roles.html              # 🎭 角色页（6个角色卡片网格）
├── 📄 stories.html            # 📚 故事页（4篇星际冒险故事）
├── 📄 gallery.html            # 🎨 画廊页（12幅作品瀑布流）
├── 📄 about.html              # 💌 关于页（理念/团队/联系）
├── 📁 css/
│   └── 📄 style.css           # 全局样式系统 + 动画
├── 📁 js/
│   └── 📄 main.js             # 全局交互脚本
├── 📁 assets/
│   ├── 📁 images/             # 图片资源
│   ├── 📁 icons/              # 图标资源
│   └── 📁 fonts/              # 字体资源
├── 📄 README.md               # 📖 项目说明（你在这里！）
├── 📄 .gitignore              # Git 忽略配置
└── 📄 CNAME                   # 自定义域名（可选）
```

---

## 🎨 设计规范

| 维度 | 说明 |
|------|------|
| 🎯 **主题** | 太空 + 小猫（🐱🚀），梦幻、可爱、治愈 |
| 🎨 **主色** | `#6C5CE7` 星空紫 + `#00CEC9` 极光青 |
| 🌈 **辅色** | `#FDCB6E` 星光黄 + `#FF7675` 星云粉 |
| 🌌 **背景** | 深蓝到紫黑渐变（模拟夜空）+ 星星闪烁动画 |
| ✍️ **字体** | 标题 `Fredoka One`，正文 `Quicksand` |
| 🔘 **圆角** | 全局 20px-40px 大圆角，按钮 100px 胶囊形 |
| 📦 **阴影** | box-shadow 漂浮立体感，偏移量 6px-10px |
| 🎬 **动画** | 星星闪烁、角色浮动、卡片悬停上浮、滚动入场 |

---

## ⚡ 交互功能

- ✅ **导航高亮** — 当前页面自动高亮
- ✅ **星空画布** — Canvas 动态星星闪烁背景
- ✅ **回到顶部** — 右下角悬浮火箭按钮
- ✅ **Toast 通知** — 点击卡片弹出可爱提示
- ✅ **暗色/亮色切换** — 左下角主题切换按钮
- ✅ **响应式布局** — 适配 375px / 768px / 1200px
- ✅ **滚动动画** — Intersection Observer 驱动入场动画
- ✅ **联系表单** — 前端验证（演示模式）

---

## 🧪 本地运行

### 方法一：Python HTTP Server

```bash
cd cartoon-website
python -m http.server 8000
```

然后打开浏览器访问：**http://localhost:8000**

### 方法二：Node.js (npx serve)

```bash
cd cartoon-website
npx serve .
```

---

## 🎭 角色介绍

| 角色 | 名字 | 职位 | 性格 |
|------|------|------|------|
| 🐱 | 小星 | 船长 | 勇敢、乐观、领袖 |
| 🦊 | 火狐 | 工程师 | 热情、聪明、发明家 |
| 🐼 | 胖达 | 厨师长 | 温柔、美食家、治愈 |
| 🐰 | 月兔 | 导航员 | 敏捷、聪慧、通信专家 |
| 🦄 | 彩虹马 | 加速师 | 魔法、梦幻、星光使者 |
| 🐧 | 企鹅船长 | 副船长 | 冷静、战术、可靠后盾 |

---

## 📚 故事列表

1. 🌿 **《月亮上的猫薄荷》** — 月球背面的神秘发现
2. 💫 **《流星快递员》** — 速度与友情的星际冒险
3. 🎣 **《银河钓鱼记》** — 胖达的悠闲钓鱼日
4. 🍬 **《星星糖果铺》** — 银河系最甜的故事

---

## 🚀 部署指南

### 1. 创建 GitHub 仓库

```bash
# 在 GitHub 上创建新仓库 cartoon-website
gh repo create cartoon-website --public --description "🐱🚀 卡创 · 星际小猫号 - 梦幻太空猫咪主题品牌网站"
```

### 2. 推送代码

```bash
cd cartoon-website
git add .
git commit -m "🎉 feat: 初始化卡创·星际小猫号品牌网站"
git remote add origin https://github.com/你的用户名/cartoon-website.git
git branch -M main
git push -u origin main
```

### 3. 启用 GitHub Pages

1. 打开仓库 Settings → Pages
2. Source 选择 `main` 分支，目录选择 `/ (root)`
3. 点击 Save，等待部署完成
4. 访问 `https://你的用户名.github.io/cartoon-website`

---

## 🛠️ 技术栈

- **HTML5** — 语义化标签
- **CSS3** — 自定义属性、Grid/Flexbox、动画、渐变
- **Vanilla JavaScript** — Canvas API、Intersection Observer、LocalStorage
- **Google Fonts** — Fredoka One + Quicksand

---

## 📝 License

MIT © 2026 卡创

---

<p align="center">
  <strong>🐱🚀 星际小猫号，准备发射！ ✨🌌</strong><br>
  <small>Made with 💜 & stardust by 卡创</small>
</p>
