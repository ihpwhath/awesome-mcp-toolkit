# 🚀 Awesome MCP Toolkit (Model Context Protocol)

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/badge.svg)](https://github.com/sindresorhus/awesome)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub Stars](https://img.shields.io/github/stars/ihpwhath/awesome-mcp-toolkit?style=social)](https://github.com/ihpwhath/awesome-mcp-toolkit)

> **打造下一代 AI Agent 与 Model Context Protocol (MCP) 开源工具集、协议指南与实战模板。**
> 无论是 Gemini、Claude 还是 OpenAI，通过标准的 MCP 协议将大模型与真实世界的 API、数据库和本地工具无缝链接！

---

## 📌 目录 (Table of Contents)

- [🌟 为什么选择 MCP?](#-为什么选择-mcp)
- [🛠️ 精选 MCP 工具与服务器 (Curated MCP Servers)](#️-精选-mcp-工具与服务器-curated-mcp-servers)
  - [开发与代码 (Developer & Code)](#开发与代码-developer--code)
  - [数据库与存储 (Databases & Storage)](#数据库与存储-databases--storage)
  - [云服务与 API (Cloud & APIs)](#云服务与-api-cloud--apis)
- [🔐 远程 MCP 与 OAuth 2.0 鉴权指南](#-远程-mcp-与-oauth-20-鉴权指南)
- [⚡ 快速开始 (Quickstart)](#-快速开始-quickstart)
- [🤝 贡献指南 (Contributing)](#-贡献指南-contributing)
- [📄 开源协议 (License)](#-开源协议-license)

---

## 🌟 为什么选择 MCP?

**Model Context Protocol (MCP)** 是连接 AI 模型与数据源的标准开放协议。类似于数据接口领域的 “USB 接口”，MCP 允许开发者一次编写，即可让 Gemini、Claude、Cursor 等多种 AI 客户端即插即用。

---

## 🛠️ 精选 MCP 工具与服务器 (Curated MCP Servers)

### 开发与代码 (Developer & Code)
* **[Agent QA](https://github.com/vostride/agent-qa)** - 通过 CLI 与 MCP 接口运行自然语言 Web 和移动端回归测试，并保留持久化测试记忆。
* **[GitHub MCP Server](https://github.com/github/github-mcp-server)** - 官方 GitHub 远程与本地 MCP 服务器，支持仓库管理、代码检索与 PR/Issue 操作。
* **[Git MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/git)** - 本地 Git 仓库版本控制与差异分析。

### 数据库与存储 (Databases & Storage)
* **[PostgreSQL MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres)** - 安全读取与查询 Postgres 数据库。
* **[Google Drive MCP](https://github.com/modelcontextprotocol/servers)** - 检索与搜索 Google Drive 文档、表格与文件。

### 云服务与 API (Cloud & APIs)
* **[FastMCP](https://github.com/PrefectHQ/fastmcp)** - 高性能 Python 快速构建 MCP 服务器与 OAuth 代理框架。
* **[Google SecOps MCP](https://security.googlecloudcommunity.com)** - 远程集成云安全与告警自动化。

---

## 🔐 远程 MCP 与 OAuth 2.0 鉴权指南

在使用远程 MCP 服务时，推荐遵循 **OAuth 2.0 / 2.1** 标准鉴权规范：
1. **授权端点 (Authorization URL)**: `https://your-domain.com/oauth/authorize`
2. **令牌端点 (Token URL)**: `https://your-domain.com/oauth/token`
3. **回调重定向 (Redirect URI)**: `https://vertexaisearch.cloud.google.com/oauth-redirect`

---

## ⚡ 快速开始 (Quickstart)

```bash
# 克隆本项目
git clone https://github.com/ihpwhath/awesome-mcp-toolkit.git
cd awesome-mcp-toolkit

# 安装快速 Python 依赖
pip install fastmcp

# 运行示例 MCP 服务
python mcp_servers/quickstart.py
```

---

## 🤝 贡献指南 (Contributing)

欢迎提交 PR 增加更多高质量的 MCP 工具、案例与教程！详情请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

如果这个项目对您有帮助，请点个 **⭐ Star** 支持一下！

---

## 📄 开源协议 (License)

本项目采用 [MIT License](LICENSE) 开源协议。
