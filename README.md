# HTML Report Viewer

基于 Streamlit 的 HTML 报告查看器。

## 功能

- 侧边栏日期选择器，默认选择今天或最近的日期
- 刷新按钮重新获取报告列表
- 动态生成 TAB 栏渲染多个 HTML 报告

## 文件结构

```
show-html/
  app.py              # 主程序（带完整注释）
  requirements.txt    # Python 依赖（Streamlit Cloud 部署必需）
  README.md           # 项目说明
  .gitignore          # Git 忽略配置
  static/             # 静态文件目录
    2026-04-30/       # 日期目录（格式：YYYY-MM-DD）
      task1.html      # HTML 报告文件
      task2.html
```

## 本地运行

```bash
# 1. 进入项目目录
cd show-html

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行应用（--logger.level=error 忽略警告）
streamlit run app.py --logger.level=error
```

## 添加新报告

1. 在 `static/` 目录下创建日期目录（如 `2026-05-01/`）
2. 将 HTML 文件放入该目录
3. 刷新页面即可看到新报告

---

## Streamlit Cloud 部署指南

### 前置条件

1. GitHub 账号
2. 项目已推送到 GitHub 仓库
3. 项目根目录必须有 `requirements.txt` 文件

### 部署步骤

#### 1. 准备 GitHub 仓库

```bash
# 初始化 Git（如果还没有）
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit"

# 使用 gh 命令创建仓库并推送
gh repo create show-html --public --source=. --push
```

#### 2. 登录 Streamlit Cloud

1. 访问 https://share.streamlit.io/
2. 点击 "Sign in with GitHub" 使用 GitHub 账号登录
3. 授权 Streamlit 访问你的 GitHub 仓库

#### 3. 创建新应用

1. 点击 "New app" 按钮
2. 填写配置：
   - **Repository**: 选择 `54-luli/show-html`
   - **Branch**: `master`（或 `main`）
   - **Main file path**: `app.py`
3. 点击 "Deploy!" 按钮

#### 4. 等待部署完成

- 首次部署需要几分钟时间
- 部署成功后会显示应用 URL，格式如：
  `https://show-html-xxxxx.streamlit.app/`

### 更新部署

当你更新 GitHub 仓库后，Streamlit Cloud 会自动重新部署：

```bash
# 修改代码后提交并推送
git add .
git commit -m "Update app"
git push
```

### 常见问题

#### Q: 部署失败，提示找不到模块
A: 确保 `requirements.txt` 包含所有依赖，每行一个包名

#### Q: 页面显示空白或报错
A: 检查 Streamlit Cloud 的日志，点击应用页面的 "Manage app" → "Logs"

#### Q: 如何查看部署状态
A: 访问 https://share.streamlit.io/ 查看所有应用列表和状态

---

## 项目维护笔记

### 文件命名规范

- 日期目录：`YYYY-MM-DD` 格式（如 `2026-04-30`）
- HTML 文件：任意名称，建议用 `task1.html`、`task2.html` 等

### 代码修改后同步到 GitHub

```bash
# 1. 修改代码
# 2. 提交更改
git add .
git commit -m "描述你的修改"
git push
# 3. Streamlit Cloud 会自动重新部署
```

### 依赖

- Python 3.8+
- Streamlit 1.11.0+（支持 `st.tabs`）

---

## GitHub 仓库地址

https://github.com/54-luli/show-html

## Streamlit Cloud 部署地址

部署成功后会生成类似以下地址：
https://show-html-xxxxx.streamlit.app/
