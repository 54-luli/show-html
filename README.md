# HTML Report Viewer

基于 Streamlit 的 HTML 报告查看器。

## 功能

- 侧边栏日期选择器，默认选择今天或最近的日期
- 刷新按钮重新获取报告列表
- 动态生成 TAB 栏渲染多个 HTML 报告

## 文件结构

```
show-html/
  app.py              # 主程序
  static/
    2026-04-30/       # 日期目录
      task1.html      # HTML报告文件
      task2.html
```

## 使用方式

```bash
cd show-html
streamlit run app.py --logger.level=error
```

## 依赖

- Python 3.8+
- Streamlit 1.11.0+
