import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

def feature_Big5():
    FW = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/position data/FW_5seasons.csv')
    AM = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/position data/AM_5seasons.csv')
    M = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/position data/M_5seasons.csv')
    DM = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/position data/DM_5seasons.csv')
    D = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/position data/D_5seasons.csv')
    GK = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/position data/GK_5seasons.csv')

    FW.drop('Unnamed: 0', axis=1, inplace=True)
    AM.drop('Unnamed: 0', axis=1, inplace=True)
    M.drop('Unnamed: 0', axis=1, inplace=True)
    DM.drop('Unnamed: 0', axis=1, inplace=True)
    D.drop('Unnamed: 0', axis=1, inplace=True)
    GK.drop('Unnamed: 0', axis=1, inplace=True)

    st.header('유럽 5대 리그 포지션별 승리기여 주요 지표 추출')

    # FW
    st.write('### FW 포지션 승리기여 지표 추출')
    FW_numeric_df = FW.select_dtypes(['int64', 'float64'])
    FW_corr_matrix = FW_numeric_df.corr()
    FW_corr_matrix_Pts = FW_corr_matrix[['Pts']]
    FW_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    FW_fig = px.imshow(FW_corr_matrix_Pts)
    st.write(FW_fig)

    index_li = FW_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = FW_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # AM
    st.write('### AM 포지션 승리기여 지표 추출')
    AM_numeric_df = AM.select_dtypes(['int64', 'float64'])
    AM_corr_matrix = AM_numeric_df.corr()
    AM_corr_matrix_Pts = AM_corr_matrix[['Pts']]
    AM_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    AM_fig = px.imshow(AM_corr_matrix_Pts)
    st.write(AM_fig)

    index_li = AM_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = AM_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # M
    st.write('### M 포지션 승리기여 지표 추출')
    M_numeric_df = M.select_dtypes(['int64', 'float64'])
    M_corr_matrix = M_numeric_df.corr()
    M_corr_matrix_Pts = M_corr_matrix[['Pts']]
    M_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    M_fig = px.imshow(M_corr_matrix_Pts)
    st.write(M_fig)

    index_li = M_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = M_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # DM
    st.write('### DM 포지션 승리기여 지표 추출')
    DM_numeric_df = DM.select_dtypes(['int64', 'float64'])
    DM_corr_matrix = DM_numeric_df.corr()
    DM_corr_matrix_Pts = DM_corr_matrix[['Pts']]
    DM_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    DM_fig = px.imshow(DM_corr_matrix_Pts)
    st.write(DM_fig)

    index_li = DM_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = DM_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # D
    st.write('### D 포지션 승리기여 지표 추출')
    D_numeric_df = D.select_dtypes(['int64', 'float64'])
    D_corr_matrix = D_numeric_df.corr()
    D_corr_matrix_Pts = D_corr_matrix[['Pts']]
    D_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    D_fig = px.imshow(D_corr_matrix_Pts)
    st.write(D_fig)

    index_li = D_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = D_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    # GK
    st.write('### GK 포지션 승리기여 지표 추출')
    GK_numeric_df = GK.select_dtypes(['int64', 'float64'])
    GK_corr_matrix = GK_numeric_df.corr()
    GK_corr_matrix_Pts = GK_corr_matrix[['Pts']]
    GK_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

    GK_fig = px.imshow(GK_corr_matrix_Pts)
    st.write(GK_fig)

    index_li = GK_corr_matrix_Pts.iloc[:6].index.tolist()
    corr_li = GK_corr_matrix_Pts['Pts'].tolist()
    for i in range(1, 6):
        st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

    st.write('## 인사이트 도출')
    st.write('#### 1. 전체적인 상관계수 값이 0.5보다 작다.')
    st.write('- 특정 한, 두개의 지표가 승리에 압도적인 영향을 주는 것은 아니다.')
    st.write('- 팀의 승리는 여러 요소들의 조합으로 이루어지는 것으로 수치로 표시하기 힘든 요소도 반영된다.')
    st.write('#### 2. 전체적인 결과를 고려했을 때 패스 성공률이 중요하다.')
    st.write('- 팀 자체적으로 패스 관련 훈련이 필요하다.')
    st.write('- 선수들은 서로 패스를 할 때 더 집중하고 팀원들과의 합을 맞추는데 집중해야된다.')
    st.write('#### 3. 수비수의 경우 다른 포지션에 비해 수치적으로 판단하기 힘들다.')
    st.write('#### 4. 골키퍼는 경기당 실점, 클린시트 횟수 등 추가적인 데이터가 필요하다.')