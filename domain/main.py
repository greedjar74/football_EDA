import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

from referee_EDA import referee_EDA_page

# 페이지 선언 
def main_page():
    st.title('Main Page 🎈')
    st.sidebar.title('Side Main 🎈')

def page2():
    referee_EDA_page()

def page3():
    st.title('Main 3 🎉')
    st.sidebar.title('Side 3 🎉')

    
# 딕셔너리 선언 {  ‘selectbox항목’ : ‘페이지명’ …  }
page_names_to_funcs = {'Main Page': main_page, 'Referee': page2, 'Position': page3}

# 사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = st.sidebar.selectbox('Select a page', page_names_to_funcs.keys())

# 해당 페이지 부르기
page_names_to_funcs[selected_page]()