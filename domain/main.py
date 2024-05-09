import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

from referee_EDA import referee_EDA_page
from Player import Player
from feature_BL import feature_BL
from feature_EPL import feature_EPL
from feature_LL import feature_LL
from feature_L1 import feature_L1
from feature_SA import feature_SA
from feature_Big5 import feature_Big5

# 페이지 선언 
def main_page():
    st.title('Main Page 🎈')
    st.sidebar.title('Side Main 🎈')

def page2():
    feature_BL()
    st.sidebar.title('Bundesliga')
    st.sidebar.write("### FW")
    st.sidebar.write("### AM")
    st.sidebar.write("### M")
    st.sidebar.write("### DM")
    st.sidebar.write("### D")
    st.sidebar.write("### GK")

def page3():
    feature_EPL()
    st.sidebar.title('EPL')
    st.sidebar.write("### FW")
    st.sidebar.write("### AM")
    st.sidebar.write("### M")
    st.sidebar.write("### DM")
    st.sidebar.write("### D")
    st.sidebar.write("### GK")

def page4():
    feature_LL()
    st.sidebar.title('Laliga')
    st.sidebar.write("### FW")
    st.sidebar.write("### AM")
    st.sidebar.write("### M")
    st.sidebar.write("### DM")
    st.sidebar.write("### D")
    st.sidebar.write("### GK")

def page5():
    feature_L1()
    st.sidebar.title('Ligue1')
    st.sidebar.write("### FW")
    st.sidebar.write("### AM")
    st.sidebar.write("### M")
    st.sidebar.write("### DM")
    st.sidebar.write("### D")
    st.sidebar.write("### GK")

def page6():
    feature_SA()
    st.sidebar.title('SerieA')
    st.sidebar.write("### FW")
    st.sidebar.write("### AM")
    st.sidebar.write("### M")
    st.sidebar.write("### DM")
    st.sidebar.write("### D")
    st.sidebar.write("### GK")

def page7():
    feature_Big5()
    st.sidebar.title('유럽 5대 리그 통합')
    st.sidebar.write("### FW")
    st.sidebar.write("### AM")
    st.sidebar.write("### M")
    st.sidebar.write("### DM")
    st.sidebar.write("### D")
    st.sidebar.write("### GK")

def page8():
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

def page9():
    Player()
    st.sidebar.title('선수 성공 여부 파악')
    st.sidebar.write('좋아하는 선수와 리그 스탯을 통해')
    st.sidebar.write('성공 여부를 알아보세요!')


# 딕셔너리 선언 {  ‘selectbox항목’ : ‘페이지명’ …  }
page_names_to_funcs = {'Main Page': main_page, 'BL 승리기여 주요 지표':page2, 'EPL 승리기여 주요 지표':page3, 
                       'LL 승리기여 주요 지표':page4, 'L1 승리기여 주요 지표':page5,'SA 승리기여 주요 지표':page6, 
                       '5대 리그 통합 승리기여 주요 지표':page7, 'Referee EDA': page8, '선수 성공여부 파악': page9}

# 사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = st.sidebar.selectbox('Select a page', page_names_to_funcs.keys())

# 해당 페이지 부르기
page_names_to_funcs[selected_page]()
