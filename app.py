"""
HTML Report Viewer - Streamlit Web Application

功能说明：
    1. 侧边栏提供日期选择器，默认选择今天（如有报告）或最近的日期
    2. 刷新按钮用于重新获取当前日期下的报告列表
    3. 主页面根据文件数量动态生成TAB栏，每个TAB渲染对应的HTML文件

文件结构：
    show-html/
        app.py              # 主程序
        static/
            2026-04-30/     # 日期目录
                task1.html  # HTML报告文件
                task2.html
                ...

使用方式：
    cd E:\\python61\\pycharm_code\\openclaw-test\\show-html
    streamlit run app.py --logger.level=error
"""

import streamlit as st
from datetime import datetime, date
from pathlib import Path

# =============================================================================
# 页面配置
# =============================================================================

# 设置页面标题、图标和布局模式
st.set_page_config(
    page_title="HTML Report Viewer",
    page_icon="📄",
    layout="wide"
)

# =============================================================================
# 常量定义
# =============================================================================

# 静态文件目录路径（与app.py同级目录下的static文件夹）
STATIC_DIR = Path(__file__).parent / "static"

# =============================================================================
# 核心函数
# =============================================================================

def get_available_dates():
    """
    获取所有有HTML文件的日期目录

    扫描static目录下的所有子目录，检查每个子目录是否包含HTML文件。
    只返回包含HTML文件的日期目录名，按日期倒序排列。

    Returns:
        list: 包含HTML文件的日期目录名列表，格式如 ["2026-04-30", "2026-04-29"]
    """
    if not STATIC_DIR.exists():
        return []

    dates = []
    for item in STATIC_DIR.iterdir():
        if item.is_dir():
            # 检查该目录下是否有HTML文件
            has_html = any(f.suffix == ".html" for f in item.iterdir() if f.is_file())
            if has_html:
                dates.append(item.name)

    # 按日期倒序排列（最新的日期在前）
    dates.sort(reverse=True)
    return dates


def get_html_files(date_str):
    """
    获取指定日期目录下的所有HTML文件

    Args:
        date_str: 日期字符串，格式如 "2026-04-30"

    Returns:
        list: HTML文件名列表，按文件名排序
    """
    date_dir = STATIC_DIR / date_str
    if not date_dir.exists():
        return []

    files = []
    for item in date_dir.iterdir():
        if item.is_file() and item.suffix == ".html":
            files.append(item.name)

    # 按文件名排序
    files.sort()
    return files


def get_tab_name(filename):
    """
    从文件名提取TAB显示名称

    去掉.html后缀，直接使用文件名作为TAB名称。
    例如：task1.html -> task1

    Args:
        filename: 文件名，如 "task1.html"

    Returns:
        str: TAB名称，如 "task1"
    """
    if filename.endswith(".html"):
        return filename[:-5]  # 去掉最后5个字符（.html）
    return filename


def calculate_height(html_content):
    """
    根据HTML内容长度动态计算渲染高度

    内容越长，高度越大，但限制在800-2000像素范围内。

    Args:
        html_content: HTML文件内容字符串

    Returns:
        int: 渲染高度（像素）
    """
    content_length = len(html_content)
    # 最小800px，最大2000px，中间按内容长度线性计算
    height = min(2000, max(800, content_length // 50))
    return height

# =============================================================================
# 主程序
# =============================================================================

# 侧边栏标题
st.sidebar.title("选择报告")

# 获取可用日期列表
available_dates = get_available_dates()

if not available_dates:
    # 无报告时的提示
    st.sidebar.warning("暂无报告")
else:
    # 将日期字符串转换为date对象，用于日期选择器
    available_date_objs = [datetime.strptime(d, "%Y-%m-%d").date() for d in available_dates]

    # 获取今天的日期
    today = date.today()

    # 默认选择逻辑：今天有报告就选今天，否则选最近的日期
    if today in available_date_objs:
        default_date = today
    else:
        default_date = available_date_objs[0]

    # -------------------------------------------------------------------------
    # 侧边栏组件
    # -------------------------------------------------------------------------

    # 日期选择器
    selected_date = st.sidebar.date_input(
        "选择日期",
        value=default_date,
        min_value=min(available_date_objs),
        max_value=max(available_date_objs)
    )

    # 刷新按钮（primary样式，宽度撑满）
    refresh = st.sidebar.button("🔄 刷新", type="primary", use_container_width=True)

    # 点击刷新时重新运行应用
    if refresh:
        st.rerun()

    # -------------------------------------------------------------------------
    # 主页面渲染
    # -------------------------------------------------------------------------

    # 将选择的日期转换为字符串格式
    selected_date_str = selected_date.strftime("%Y-%m-%d")

    # 检查选择的日期是否有报告
    if selected_date_str not in available_dates:
        st.sidebar.warning("该日期暂无报告")
    else:
        # 获取该日期下的HTML文件列表
        html_files = get_html_files(selected_date_str)

        if html_files:
            # 生成TAB名称列表
            tab_names = [get_tab_name(f) for f in html_files]

            # 创建TAB组件
            tabs = st.tabs(tab_names)

            # 在每个TAB中渲染对应的HTML文件
            for tab, filename in zip(tabs, html_files):
                with tab:
                    # 构建文件完整路径
                    file_path = STATIC_DIR / selected_date_str / filename

                    # 读取HTML文件内容
                    with open(file_path, "r", encoding="utf-8") as f:
                        html_content = f.read()

                    # 动态计算渲染高度
                    height = calculate_height(html_content)

                    # 渲染HTML内容（启用滚动）
                    st.components.v1.html(
                        html_content,
                        height=height,
                        scrolling=True
                    )