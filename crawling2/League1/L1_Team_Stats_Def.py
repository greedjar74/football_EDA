from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time

# 웹 페이지 생성
driver = webdriver.Chrome()
driver.get('https://1xbet.whoscored.com/')
time.sleep(1)

# 팝업 제어
#popup = driver.find_element(By.CLASS_NAME, 'webpush-swal2-container')
#popup.find_element(By.CLASS_NAME, 'webpush-swal2-close').click()
#time.sleep(1)

url_list = ['https://1xbet.whoscored.com/Regions/74/Tournaments/22/Seasons/9129/Stages/21037/TeamStatistics/France-Ligue-1-2022-2023',
            'https://1xbet.whoscored.com/Regions/74/Tournaments/22/Seasons/8671/Stages/19866/TeamStatistics/France-Ligue-1-2021-2022',
            'https://1xbet.whoscored.com/Regions/74/Tournaments/22/Seasons/8185/Stages/18594/TeamStatistics/France-Ligue-1-2020-2021',
            'https://1xbet.whoscored.com/Regions/74/Tournaments/22/Seasons/7814/Stages/17593/TeamStatistics/France-Ligue-1-2019-2020',
            'https://1xbet.whoscored.com/Regions/74/Tournaments/22/Seasons/7344/Stages/16348/TeamStatistics/France-Ligue-1-2018-2019']

year_list = ['22_23', '21_22', '20_21', '19_20', '18_19']
for i in range(5):
    url = url_list[i]
    year = year_list[i]

    driver.get(url) # 해당 시즌으로 이동
    time.sleep(3)

    # Offensive로 이동
    driver.find_element(By.XPATH, '//*[@id="stage-team-stats-options"]/li[2]/a').click()
    time.sleep(2)
    off_container = driver.find_element(By.ID, 'stage-team-stats-defensive')
    container = off_container.find_element(By.ID, 'top-team-stats-summary-content')
    team_container = container.find_elements(By.TAG_NAME, 'tr')

    all_data = []

    for team in team_container:
        td_list = team.find_elements(By.TAG_NAME, 'td')
        tmp = td_list[0].text
        tmp_li = tmp.split('.')
        Team = tmp_li[1][1:]
        Shotspg = td_list[1].text
        Tacklespg = td_list[2].text
        Interceptionspg = td_list[3].text
        Foulspg = td_list[4].text
        Offsidespg = td_list[5].text

        team_data = [Team, Shotspg, Tacklespg, Interceptionspg, Foulspg, Offsidespg]
        all_data.append(team_data)

    team_df = pd.DataFrame(all_data)    
    team_df.columns = ['Team', 'def_Shotspg', 'def_Tacklespg', 'def_Interceptionspg', 'def_Foulspg', 'def_Offsidespg']
    team_df.to_csv(f'{year}_L1_Team_Stats_defensive.csv', encoding='utf-8-sig')
    print(team_df.tail())