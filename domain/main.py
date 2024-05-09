import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

from referee_EDA import referee_EDA_page
from Player import Player

# 페이지 선언 
def main_page():
    st.title('Main Page 🎈')
    st.sidebar.title('Side Main 🎈')

def page2():
    pass

def page3():
    pass

def page4():
    referee_EDA_page()
    st.sidebar.title('Referee EDA')
    st.sidebar.write("### 유럽 5대 리그 Yellow Card 분석")
    st.sidebar.write("### 유럽 5대 리그 Yellow Card 트렌드 분석")
    st.sidebar.write("### 유럽 5대 리그 Red Card 분석")
    st.sidebar.write("### 유럽 5대 리그 Red Card 트렌드 분석")
    st.sidebar.write("### 유럽 5대 리그 Fouls/Tackles 분석")
    st.sidebar.write("### 유럽 5대 리그 Fouls/Tackles 트렌드 분석")
    st.sidebar.write("### 유럽 5대 리그 Fouls/Game 트렌드 분석")
    st.sidebar.write("### 인사이트 도출")

def page5():
    Player()
    st.sidebar.title('선수 성공 여부 파악')
    st.sidebar.write('좋아하는 선수와 리그 스탯을 통해')
    st.sidebar.write('성공 여부를 알아보세요!')


# 딕셔너리 선언 {  ‘selectbox항목’ : ‘페이지명’ …  }
page_names_to_funcs = {'Main Page': main_page, '승리기여 주요 지표 #1':page2, 'BL 승리기여 주요 지표':page3, 'Referee EDA': page4, '선수 성공여부 파악': page5}

# 사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = st.sidebar.selectbox('Select a page', page_names_to_funcs.keys())

# 해당 페이지 부르기
page_names_to_funcs[selected_page]()
