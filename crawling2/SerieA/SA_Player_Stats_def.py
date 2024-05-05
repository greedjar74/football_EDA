from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time

# 웹 페이지 생성
driver = webdriver.Chrome()
driver.get('https://1xbet.whoscored.com/')
time.sleep(2)

# 팝업 제어
#popup = driver.find_element(By.CLASS_NAME, 'webpush-swal2-container')
#popup.find_element(By.CLASS_NAME, 'webpush-swal2-close').click()
#time.sleep(1)

url_list = ['https://1xbet.whoscored.com/Regions/108/Tournaments/5/Seasons/9159/Stages/21087/PlayerStatistics/Italy-Serie-A-2022-2023',
            'https://1xbet.whoscored.com/Regions/108/Tournaments/5/Seasons/8735/Stages/19982/PlayerStatistics/Italy-Serie-A-2021-2022',
            'https://1xbet.whoscored.com/Regions/108/Tournaments/5/Seasons/8330/Stages/18873/PlayerStatistics/Italy-Serie-A-2020-2021',
            'https://1xbet.whoscored.com/Regions/108/Tournaments/5/Seasons/7928/Stages/17835/PlayerStatistics/Italy-Serie-A-2019-2020',
            'https://1xbet.whoscored.com/Regions/108/Tournaments/5/Seasons/7468/Stages/16548/PlayerStatistics/Italy-Serie-A-2018-2019']

year_list = ['22_23', '21_22', '20_21', '19_20', '18_19']
next_tap = [33, 34, 35, 31, 30]

for i in range(5):
    url = url_list[i]
    year = year_list[i]

    driver.get(url) # 해당 시즌으로 이동
    time.sleep(3)
    # defnsive로 이동
    driver.find_element(By.XPATH, '//*[@id="stage-top-player-stats-options"]/li[2]/a').click()
    time.sleep(3)

    all_data = []
    for j in range(next_tap[i]):
        container_tmp = driver.find_element(By.ID, 'statistics-table-defensive')
        container = container_tmp.find_element(By.ID, 'player-table-statistics-body')
        player_container = container.find_elements(By.TAG_NAME, 'tr')

        for player in player_container:
            Name = player.find_element(By.CLASS_NAME, 'iconize-icon-left').text
            Tackles = player.find_element(By.CLASS_NAME, 'tacklePerGame').text
            Inter = player.find_element(By.CLASS_NAME, 'interceptionPerGame').text
            Fouls = player.find_element(By.CLASS_NAME, 'foulsPerGame').text
            Offsides = player.find_element(By.CLASS_NAME, 'offsideWonPerGame').text
            Clear = player.find_element(By.CLASS_NAME, 'clearancePerGame').text
            Drb = player.find_element(By.CLASS_NAME, 'wasDribbledPerGame').text
            Blocks = player.find_element(By.CLASS_NAME, 'outfielderBlockPerGame').text
            OwnG = player.find_element(By.CLASS_NAME, 'goalOwn').text

            player_data = [Name, Tackles, Inter, Fouls, Offsides, Clear, Drb, Blocks, OwnG]
            all_data.append(player_data)
        
        if j != next_tap[i]:
            buttons = driver.find_element(By.ID, 'statistics-paging-defensive')
            buttons.find_element(By.ID, 'next').click()
            time.sleep(2)

    player_df = pd.DataFrame(all_data)    
    player_df.columns = ['Name', 'Tackles', 'Inter', 'Fouls', 'Offsides', 'Clear', 'Drb', 'Blocks', 'OwnG']
    player_df.to_csv(f'{year}_SA_Player_Stats_def.csv', encoding='utf-8-sig')
    print(player_df.tail())