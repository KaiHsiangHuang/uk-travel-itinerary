import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="英国旅行行程 - 9月14-21日", layout="wide")

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=4000, scrolling=True)
