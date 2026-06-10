# intfocus-portal

> 胜因学院内部开发门户：技术文档中心、开发规范指南与企业文化平台。

🔗 **在线访问**：[intfocus.archived.jaden.tech](https://intfocus.archived.jaden.tech)

## 项目说明

本项目是胜因公司内部技术门户站点，为开发团队提供统一的文档查阅、规范学习和协作指引，包括：

- **生态系统**：胜因学院小程序、胜因盒子 TV 大屏等产品入口
- **开发文档**：编程规范（Gitlab/Java/MySQL/JavaScript/CDN）、开发规范、API 接口文档、项目源码体系
- **企业文化**：职场共识、团队协作、在线文档、胜因周刊
- **外链导航**：胜因官网、个人简历

## 技术栈

- **前端框架**：Vue.js 2.x
- **UI 框架**：Tailwind CSS（CDN）
- **图标库**：Font Awesome 4.7
- **构建工具**：Hexo 6.3.0（静态站点生成）
- **PWA 支持**：Service Worker + Workbox
- **深色主题**：科技感 UI（`#0f172a` 深蓝背景）
- **响应式设计**：支持移动端 + 桌面端

## 部署

本项目通过 GitHub Pages 部署，绑定自定义域名 `intfocus.archived.jaden.tech`。

```bash
# 本地预览
python3 -m http.server 8080
```

## 核心功能

### 1. 双屏滑动主页

首页采用全屏双屏设计：
- **第一屏**：品牌展示 + 核心亮点（生命力、轻量、可视化）
- **第二屏**：导航菜单（生态系统、开发文档、企业文化）

### 2. 开发规范体系

- 编程规范：Gitlab / Java / MySQL / JavaScript / CDN
- 开发规范：环境、ETL、API 设计、RDC 接口、业务菜单
- 接口文档：小程序、DataV 报表、运营平台

### 3. 企业文化模块

- 职场共识 & 协作培训
- 在线文档 & 胜因周刊

## 敏感信息说明

本项目为内部技术门户，包含：
- 内部 GitLab 项目链接（`*.idata.mobi`）
- 内部 Jenkins 部署地址
- 团队成员贡献者列表

外部访问仅展示公开文档，敏感操作需内网权限。

## License

© 李俊杰 Jaden Li. All rights reserved.
