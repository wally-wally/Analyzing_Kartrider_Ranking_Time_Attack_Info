import csv
import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup

# oidUser 추출
user_nickname = input('닉네임을 입력하세요. : ')
url = f'http://kart.nexon.com/Garage/Main?strRiderID={user_nickname}'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
tags = str(soup.select_one('#MenuButton3'))

oidUser = ''
for letter in tags[32:]:
    if letter.isdecimal():
        oidUser += letter
    else:
        break

# 기록실에서 스피드별 타임어택 기록 추출
while True:
    speed = input('원하는 타임어택 기록의 속도(채널)을 입력하세요.(S0, S1, S2, S3중 하나 입력) : ')
    if speed not in ['S0', 'S1', 'S2', 'S3']:
        print('채널 명칭을 올바르게 다시 입력하세요.')
    else:
        break
select_speed = int(speed[-1])
adjust_num = (select_speed % 4) - 1
time_attack_dict = {}

for i in range(1, 100):
    try:
        re_url = f'http://kart.nexon.com/Garage/Record?oidUser={oidUser}&gpage=1&tpage={i}&lc={adjust_num}'
        re_html = requests.get(re_url).text
        re_soup = BeautifulSoup(re_html, 'html.parser')
        data = re_soup.select_one('#CntTime > div > div.CntTime3 > div.CntTime2Sec > table > tbody > tr:nth-child(1) > td.CntTime2L4 > span.TxtBlu').text
    except AttributeError:
        break

    for j in range(1, 4):
        try:
            common_re_url = f'#CntTime > div > div.CntTime3 > div.CntTime2Sec > table > tbody > tr:nth-child({j})'
            map_data = re_soup.select(f'{common_re_url} > th')[0].text
            rank_data = re_soup.select(f'{common_re_url} > td.CntTime2L2 > span')[0].text
            car_data = re_soup.select(f'{common_re_url} > td.CntTime2L3')[0].text
            time_data = re_soup.select(f'{common_re_url} > td.CntTime2L4 > span.TxtBlu')[0].text
            time_attack_dict[3*i-(3-j)] = {
                'map': map_data,
                'rank': rank_data,
                'car': car_data,
                'time': time_data
            }
        except IndexError:
            break
# pprint(time_attack_dict)

if time_attack_dict != {}:
    with open(f'timeattack_{user_nickname}_S{select_speed}.csv', 'w', encoding='utf-8', newline='') as f:
        fieldnames = ('map', 'rank', 'car', 'time')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for value in time_attack_dict.values():
            writer.writerow(value)
elif time_attack_dict == {}:
    print(f'S{select_speed}의 타임어택을 진행하지 않았습니다.')