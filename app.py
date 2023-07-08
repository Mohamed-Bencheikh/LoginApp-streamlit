import streamlit as st

# Header
st.header("Welcome to _:blue[CODART]_")
st.write("Remember! Coding is Art.")
st.write("LOGIN")
# Form
with st.form("myform"):
    uname = st.text_input(label="Username", placeholder="username",
                          help="enter your username!")
    pwd = st.text_input(label="Pasword", placeholder="password",
                        help="enter your password!", type='password')
    btn_sub = st.form_submit_button(
        label="submit", type='primary', help="Click to login!")
if btn_sub:
    if pwd == 'pass123':
        st.success("Welcome "+uname+" ✅")
    else:
        st.error("Incorrect login 🚨")

# Sidebar
st.sidebar.markdown("Home")
st.sidebar.markdown("sign up")
st.sidebar.markdown("about")
st.sidebar.selectbox("Contact", options=("LinkdIn", "Instagram", "Email"))
st.sidebar.markdown("_:gray[MBC@2023]_")
st.form(key='form')
