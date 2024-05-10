import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
from PIL import Image

from referee_EDA import referee_EDA_page
from Player import Player
from feature_BL import feature_BL
from feature_EPL import feature_EPL
from feature_LL import feature_LL
from feature_L1 import feature_L1
from feature_SA import feature_SA
from feature_Big5 import feature_Big5
from feature import feature

# 페이지 선언 
def main_page():
    st.title('Main Page 🎈')
    st.sidebar.title('Side Main 🎈')

def page2():
    feature()

def page3():
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

def page4():
    Player()
    st.sidebar.title('선수 성공 여부 파악')
    st.sidebar.write('좋아하는 선수와 리그 스탯을 통해')
    st.sidebar.write('성공 여부를 알아보세요!')


# 딕셔너리 선언 {  ‘selectbox항목’ : ‘페이지명’ …  }
page_names_to_funcs = {'Main Page': main_page, '리그별 승리 주요 지표':page2,  
                       'Referee EDA': page3, '선수 성공여부 파악': page4}

# 사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = st.sidebar.selectbox('Select a page', page_names_to_funcs.keys())

# 해당 페이지 부르기
page_names_to_funcs[selected_page]()
