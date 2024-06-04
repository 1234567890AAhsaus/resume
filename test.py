import streamlit as st

# 设置页面配置
st.set_page_config(page_title="郭嘉鑫的个人网页", layout="centered")

# 页面标题
st.title("郭嘉鑫的个人网页")

# 简介
st.header("简介")
st.write("你好！我是郭嘉鑫，专业为财务管理。")

# 教育背景
st.header("教育背景")
st.write("华东理工大学")

# 技能
st.header("技能")
skills = ["Python", "MATLAB", "Excel"]
st.write(", ".join(skills))

# 图片画廊
st.header("图片画廊")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("郭嘉鑫_蓝桥杯.jpg", caption="Image 1", use_column_width=True)
with col2:
    st.image("计算机二级_2024_3证书_页面_1.jpg", caption="Image 2", use_column_width=True)
with col3:
    st.image("计算机二级_2024_3证书_页面_2.jpg", caption="Image 3", use_column_width=True)

# 社交媒体
st.header("社交媒体")
st.markdown("[bilibili](https://account.bilibili.com/account/home?spm_id_from=333.1007.0.0)")
st.markdown("[GitHub](https://github.com/1234567890AAhsaus)")

# 联系表单
st.header("联系表单")
with st.form("contact_form"):
    name = st.text_input("你的名字")
    email = st.text_input("你的邮箱")
    message = st.text_area("你的留言")
    submit_button = st.form_submit_button(label="提交")
    if submit_button:
        st.success("感谢你的留言！")

# 联系方式
st.header("联系方式")
st.write("微信号: _1234567890AAhsaus")

# 在页面底部添加空白行，以更好地分隔内容
st.markdown("<br><br>", unsafe_allow_html=True)
