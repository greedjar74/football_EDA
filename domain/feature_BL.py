import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

BL_FW = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/EDA/Bundesliga/Budesliga_data/BL_Position_Player_Stats/BL_FW_Player.csv')
BL_AM = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/EDA/Bundesliga/Budesliga_data/BL_Position_Player_Stats/BL_AM_Player.csv')
BL_M = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/EDA/Bundesliga/Budesliga_data/BL_Position_Player_Stats/BL_M_Player.csv')
BL_DM = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/EDA/Bundesliga/Budesliga_data/BL_Position_Player_Stats/BL_DM_Player.csv')
BL_D = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/EDA/Bundesliga/Budesliga_data/BL_Position_Player_Stats/BL_D_Player.csv')
BL_GK = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/EDA/Bundesliga/Budesliga_data/BL_Position_Player_Stats/BL_GK_Player.csv')

BL_FW.drop('Unnamed: 0', axis=1, inplace=True)
BL_AM.drop('Unnamed: 0', axis=1, inplace=True)
BL_M.drop('Unnamed: 0', axis=1, inplace=True)
BL_DM.drop('Unnamed: 0', axis=1, inplace=True)
BL_D.drop('Unnamed: 0', axis=1, inplace=True)

BL_Team = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/EDA/Bundesliga/Budesliga_data/Bundesliga_22_23_Team_Table_Added.csv')
BL_Team.columns = ['Team', 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts', 'Goals',
       'Shots pg', 'Yellow', 'Red', 'Poss%', 'Pass%', 'A_Won', 'Rating',
       'Shoted pg', 'Tackles pg', 'Intercept pg', 'Fouls pg', 'Offsides pg',
       'Shots OT pg', 'Dribbles pg', 'Fouled pg']

st.header('Bundesliga 포지션별 승리기여 주요 지표 추출')

# FW
st.write('### FW 포지션 승리기여 지표 추출')
BL_FW_df = pd.merge(BL_FW, BL_Team[['Team', 'Pts']], on='Team', how='inner')
BL_FW_numeric_df = BL_FW_df.select_dtypes(['int64', 'float64'])
BL_FW_numeric_df.drop(['OwnG', 'Rating', 'team_number', 'MoM'], axis=1, inplace=True)
BL_FW_corr_matrix = BL_FW_numeric_df.corr()
BL_FW_corr_matrix_Pts = BL_FW_corr_matrix[['Pts']]
BL_FW_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

FW_fig = px.imshow(BL_FW_corr_matrix_Pts)
st.write(FW_fig)

index_li = BL_FW_corr_matrix_Pts.iloc[:6].index.tolist()
corr_li = BL_FW_corr_matrix_Pts['Pts'].tolist()
for i in range(1, 6):
    st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

# AM
st.write('### AM 포지션 승리기여 지표 추출')
BL_AM_df = pd.merge(BL_AM, BL_Team[['Team', 'Pts']], on='Team', how='inner')
BL_AM_numeric_df = BL_AM_df.select_dtypes(['int64', 'float64'])
BL_AM_numeric_df.drop(['OwnG', 'Rating', 'team_number', 'MoM'], axis=1, inplace=True)
BL_AM_corr_matrix = BL_AM_numeric_df.corr()
BL_AM_corr_matrix_Pts = BL_AM_corr_matrix[['Pts']]
BL_AM_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

AM_fig = px.imshow(BL_AM_corr_matrix_Pts)
st.write(AM_fig)

index_li = BL_AM_corr_matrix_Pts.iloc[:6].index.tolist()
corr_li = BL_AM_corr_matrix_Pts['Pts'].tolist()
for i in range(1, 6):
    st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

# M
st.write('### M 포지션 승리기여 지표 추출')
BL_M_df = pd.merge(BL_M, BL_Team[['Team', 'Pts']], on='Team', how='inner')
BL_M_numeric_df = BL_M_df.select_dtypes(['int64', 'float64'])
BL_M_numeric_df.drop(['Rating', 'team_number', 'MoM'], axis=1, inplace=True)
BL_M_corr_matrix = BL_M_numeric_df.corr()
BL_M_corr_matrix_Pts = BL_M_corr_matrix[['Pts']]
BL_M_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

M_fig = px.imshow(BL_M_corr_matrix_Pts)
st.write(M_fig)

index_li = BL_M_corr_matrix_Pts.iloc[:6].index.tolist()
corr_li = BL_M_corr_matrix_Pts['Pts'].tolist()
for i in range(1, 6):
    st.write(f'{index_li[i]}: {corr_li[i]:.3f}')

# M
st.write('### M 포지션 승리기여 지표 추출')
BL_M_df = pd.merge(BL_M, BL_Team[['Team', 'Pts']], on='Team', how='inner')
BL_M_numeric_df = BL_M_df.select_dtypes(['int64', 'float64'])
BL_M_numeric_df.drop(['OwnG', 'Rating', 'team_number', 'MoM'], axis=1, inplace=True)
BL_M_corr_matrix = BL_M_numeric_df.corr()
BL_M_corr_matrix_Pts = BL_M_corr_matrix[['Pts']]
BL_M_corr_matrix_Pts.sort_values('Pts', ascending=False, inplace=True)

M_fig = px.imshow(BL_M_corr_matrix_Pts)
st.write(M_fig)

index_li = BL_M_corr_matrix_Pts.iloc[:6].index.tolist()
corr_li = BL_M_corr_matrix_Pts['Pts'].tolist()
for i in range(1, 6):
    st.write(f'{index_li[i]}: {corr_li[i]:.3f}')