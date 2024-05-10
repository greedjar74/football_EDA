import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
from PIL import Image

from referee_main import referee_main
from feature_main import feature_main
from Player import Player

# 페이지 선언 
def main_page():
    st.title('Main Page 🎈')
    st.sidebar.title('Side Main 🎈')

def page2():
    feature_main()
    st.sidebar.title('승리 기여 주요 지표')

def page3():
    referee_main()
    st.sidebar.title('Referee EDA')

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
