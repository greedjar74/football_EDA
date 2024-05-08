import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

BL_referee = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/referee/BL_referee_5seasons.csv')
EPL_referee = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/referee/EPL_referee_5seasons.csv')
LL_referee = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/referee/LL_referee_5seasons.csv')
L1_referee = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/referee/L1_referee_5seasons.csv')
SA_referee = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/referee/SA_referee_5seasons.csv')

BL_referee_path_list = os.listdir('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/Bundesliga/BL_Referee')
EPL_referee_path_list = os.listdir('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/EPL/EPL_Referee')
LL_referee_path_list = os.listdir('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/Laliga/LL_Referee')
L1_referee_path_list = os.listdir('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/League1/L1_Referee')
SA_referee_path_list = os.listdir('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/SerieA/SA_Referee')

# 5대 리그에 대해서 5시즌 데이터를 읽어온다.
BL_referee_data_list = []
for path in BL_referee_path_list:
    tmp = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/Bundesliga/BL_Referee/' + path)
    tmp.drop('Unnamed: 0', axis=1, inplace=True)
    BL_referee_data_list.append(tmp)

EPL_referee_data_list = []
for path in EPL_referee_path_list:
    tmp = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/EPL/EPL_Referee/'+path)
    tmp.drop('Unnamed: 0', axis=1, inplace=True)
    EPL_referee_data_list.append(tmp)

LL_referee_data_list = []
for path in LL_referee_path_list:
    tmp = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/Laliga/LL_Referee/' + path)
    tmp.drop('Unnamed: 0', axis=1, inplace=True)
    LL_referee_data_list.append(tmp)

L1_referee_data_list = []
for path in L1_referee_path_list:
    tmp = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/League1/L1_Referee/' + path)
    tmp.drop('Unnamed: 0', axis=1, inplace=True)
    L1_referee_data_list.append(tmp)

SA_referee_data_list = []
for path in SA_referee_path_list:
    tmp = pd.read_csv('/Users/kimhongseok/eda_side_project/football_EDA/5_seasons/SerieA/SA_Referee/' + path)
    tmp.drop('Unnamed: 0', axis=1, inplace=True)
    SA_referee_data_list.append(tmp)


st.header('Referee EDA')

# Yellow card 누적 그래프
Yellow_tmp = []
Yellow_tmp.append(BL_referee['Yel'].sum())
Yellow_tmp.append(EPL_referee['Yel'].sum())
Yellow_tmp.append(LL_referee['Yel'].sum())
Yellow_tmp.append(L1_referee['Yel'].sum())
Yellow_tmp.append(SA_referee['Yel'].sum())

Yellow_df = pd.DataFrame(Yellow_tmp, index=['BL', 'EPL', 'LL', 'L1', 'SA'], columns=['Yellow'])
Yellow_df.reset_index(inplace=True)
Yellow_df.columns = ['League', 'Yellow']

fig1 = plt.figure(figsize=(8, 5))
sns.barplot(data=Yellow_df, x='League', y='Yellow')
plt.grid(True)
plt.title('Big5 League Yellow Card')
st.write(fig1)

# 5시즌 동안 5개 리그의 Yellow카드 트렌드 그래프
BL_Yellow_trend = []
for data in BL_referee_data_list:
    BL_Yellow_trend.append(data['Yel'].sum())

BL_Yellow_trend_df = pd.DataFrame(BL_Yellow_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
BL_Yellow_trend_df.reset_index(inplace=True)
BL_Yellow_trend_df.columns = ['Season', 'Yellow']

EPL_Yellow_trend = []
for data in EPL_referee_data_list:
    EPL_Yellow_trend.append(data['Yel'].sum())

EPL_Yellow_trend_df = pd.DataFrame(EPL_Yellow_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
EPL_Yellow_trend_df.reset_index(inplace=True)
EPL_Yellow_trend_df.columns = ['Season', 'Yellow']

LL_Yellow_trend = []
for data in LL_referee_data_list:
    LL_Yellow_trend.append(data['Yel'].sum())

LL_Yellow_trend_df = pd.DataFrame(LL_Yellow_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
LL_Yellow_trend_df.reset_index(inplace=True)
LL_Yellow_trend_df.columns = ['Season', 'Yellow']

L1_Yellow_trend = []
for data in L1_referee_data_list:
    L1_Yellow_trend.append(data['Yel'].sum())

L1_Yellow_trend_df = pd.DataFrame(L1_Yellow_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
L1_Yellow_trend_df.reset_index(inplace=True)
L1_Yellow_trend_df.columns = ['Season', 'Yellow']

SA_Yellow_trend = []
for data in SA_referee_data_list:
    SA_Yellow_trend.append(data['Yel'].sum())

SA_Yellow_trend_df = pd.DataFrame(SA_Yellow_trend,index=['18-19', '19-20', '20-21', '21-22', '22-23'])
SA_Yellow_trend_df.reset_index(inplace=True)
SA_Yellow_trend_df.columns = ['Season', 'Yellow']

fig2 = plt.figure(figsize=(8, 5))

plt.plot(BL_Yellow_trend_df['Season'], BL_Yellow_trend_df['Yellow'], marker='^', linestyle='-', color='black', label='Bundesliga')
plt.plot(EPL_Yellow_trend_df['Season'], EPL_Yellow_trend_df['Yellow'], marker='o', linestyle='-', color='b', label='EPL')
plt.plot(LL_Yellow_trend_df['Season'], LL_Yellow_trend_df['Yellow'], marker='D', linestyle='-', color='magenta', label='Laliga')
plt.plot(L1_Yellow_trend_df['Season'], L1_Yellow_trend_df['Yellow'], marker='s', linestyle='-', color='red', label='Ligue1')
plt.plot(SA_Yellow_trend_df['Season'], SA_Yellow_trend_df['Yellow'], marker='x', linestyle='-', color='green', label='SerieA')

plt.ylim([500, 2000])
plt.grid(True)
plt.legend()
plt.title('Big5 League Yellow Card Trend')
st.write(fig2)

# 5대 리그 Red 카드 누적 그래프
Red_tmp = []
Red_tmp.append(BL_referee['Red'].sum())
Red_tmp.append(EPL_referee['Red'].sum())
Red_tmp.append(LL_referee['Red'].sum())
Red_tmp.append(L1_referee['Red'].sum())
Red_tmp.append(SA_referee['Red'].sum())

Red_df = pd.DataFrame(Red_tmp, index=['BL', 'EPL', 'LL', 'L1', 'SA'], columns=['Red'])
Red_df.reset_index(inplace=True)
Red_df.columns = ['League', 'Red']

fig3 = plt.figure(figsize=(8, 5))
sns.barplot(data=Red_df, x='League', y='Red')
plt.title('Big5 League Red Card')
plt.grid(True)
st.write(fig3)

# 5대 리그 Red 카드 5시즌 트렌드