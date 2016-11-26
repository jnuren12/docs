# <sup style="font-size: .4em"><u>A Taste of</u></sup> Web LSD

## 网联技术沙龙

---

# 小调查

---

# HTML + CSS?

---

# Bootstrap?

---

# JavaScript?

---

# Node.js + NPM?

---

# ES6?

---

# 提神

## 没别的意思

---

### $ whoami

- AnqurVanillapy, 你们熟悉的辣鸡
- 放心, 今天不虐狗
- Python, JavaScript, GNU/Linux
- 自家用幻灯工具 [gmhp](https://github.com/anqurvanillapy/gmhp)

---

# Guidelines

## 风格

---

### Guidelines?

- Specs
- Codestyles
    + HTML/CSS/JS
    + w/ linters
- Conventions

---

### In brief

- In FE dev,
    + spaces, not tabs
    + 2, not 4
    + don't close empty tags
- More?
    + id, class, type...
    + BEM/SUIT
    + linters

---

### "Lyk Dis!"

来看个例子吧.

```bash
$ pygmentize -g starter.html
```

---

# Why?

## One-man code!

---

# OT

## Off topic rn...

---

# LSD

## D-麦角酸二乙胺

---

### _别这样..._

![let-your-spirit-soar](let-your-spirit-soar.gif)

---

# Legibility

## 可读性

---

### Legibility

- 可读性, mainly
    + specs, again (not today <span style="color: red">×</span>)
    + code readability (yeah <span style="color: green">√</span>)
- our sight is the metrics

---

![medium](medium.png)

---

![douban-fm-obfuscated-js](130917_douban.fm.werid_js.png)

(obfuscated, not bad.)

---

### "geez."

![computer-boy-thumb-up](computer-boy-thumb-up.gif)

---

### Bootstrap

"Bootstrap, Bootstrap everywhere ..."

- 一堆 class, 栅格系统...
- `role=""`
- `aria-level=`
- `aria-hidden="true"`
- ...

---

### a11y

- Accessibility
    + ARIA, Accessibility Rich Internet Application
    + 网页阅读器, e.g. Safari for iOS
    + 残疾人专用, e.g. VoiceOver
    + 强迫症专用, DevTools all the things!

---

### Tips

- 别用 `<div>`, `<span>` 这样的元素做按钮
- 用 `<div>` 做简单分块之前想好了吗
- 如果你是 Bootstrap 用户, 那么只用它就足够了
- google "bootstrap themes"
- 别用 ARIA, 除非老板说要用
- 阅读多一些 CSS 有关的东西

---

![wait-a-min](wait-a-min.jpg)

---

# Semantics

## 语义

---

### Semantics

- 语义, 以代码可读性为基础
    + HTML5 Semantic Elements
    + w/ a11y, e.g. 网页阅读器

---

### Semantic Elements

- `<header>`, `<footer>`
- `<nav>`
- `<main>`
- `<article>`, `<section>`, `<summary>`
- `<aside>`
- `<figure>`, `<figcaption>`

---

### DO IT LIVE!

现场看看效果.

```bash
$ code semantic-fun.html
$ http-server .
```

---

### More?

- 表格中还是用 `<button type="submit">` 提交吧
- 或者 `<input type="submit">`
- 如果是必须要 xhr 的 SPA, 借助框架吧 :)
- 一定记住, `<div>` 和 `<span>` 是无语义的, 只和布局有关

---

![theres-more](theres-more.jpg)

---

# Delegation

## 委托

---

### "Nunya bidness."

- 你们还没到理解和应用的阶段
- 包括我 :X
- 但你们会好奇怎么一步登天
- 包括我 :) 谁不是呢!

---

### Browser, LLAP!

- 不同浏览器在不同系统渲染的网页有什么视觉上的区别?
    + 播放器长得不一样
    + 按钮不同
    + 输入框什么的也不同 (其实就是表单)

---

# Shadow DOM!

## 有奖竞猜

---

### 不可改

- 原生的组件
- 和 Flash Player 等不同
- 按钮和输入框不是 Shadow DOM, 但是其属性在各浏览器间不同
    + 比如, `color: buttonface`

---

# Web Components!

## More than Shadow DOM

---

### UA?

- 有没有了解过 user-agent stylesheet?
- 有没有自己定义过标签?
- 有没有觉得 `<div class="">` 麻烦?

---

# Custom Elements

## `<jnuren></jnuren>`

---

### Custom Elements

- An open Shadow DOM (external files)
- Registered by Custom Elements API
- Reusable for everyone

---

# Browser Support

## 科科

---

# Chrome

## !== 谷歌浏览器

---

# difs? how-tos?

---

### DO IT LIVE!

Wrap things up w/o Bootstrap!

![deal-with-it](deal-with-it.jpg)

---

# `display: flex`

## jfgi, man.

---

### Q&A

![qna](qna.png)

---

# Web crawler

## Easter Egg!
