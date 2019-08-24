import csv
import requests
import json
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
from bs4 import BeautifulSoup
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def collect_info(request):
    return render(request, 'pages/collect_info.html')


def collect_situation(request):
    user_nickname = request.POST.get('user_nickname')
    speed = request.POST.get('speed')

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
    
    select_speed = int(speed[1])
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
        result = '데이터 수집이 완료되었습니다.'
    elif time_attack_dict == {}:
        result = f'S{select_speed}의 타임어택을 진행하지 않았습니다.'
    
    context = {
        'result': result,
    }

    return render(request, 'pages/collect_situation.html', context)


def analysis_info(request):
    return render(request, 'pages/analysis_info.html')


def analysis_data(request):
    rank_list = []
    car_list = []
    csv_file_exist = 1 # 해당 채널의 csv 파일이 있는지 확인하기 위한 변수
    result = ''
    divisor = ''
    
    user_nickname = request.POST.get('user_nickname')
    speed = request.POST.get('speed')
    choice_type = request.POST.get('Select_data')
    
    select_speed = int(speed[1])

    try:
        with open(f'timeattack_{user_nickname}_S{select_speed}.csv', newline='', encoding='utf-8') as f:
            record_data = csv.DictReader(f)
            for data in record_data:
                rank_list.append(data['rank'])
                car_list.append(data['car'])
    except FileNotFoundError:
        csv_file_exist = 0

    if csv_file_exist:
        if choice_type == '1.타임어택에서 사용된 차량의 비율 -- 파이 차트':
            car_kind = []
            car_count = []
            for car in car_list:
                if car not in car_kind:
                    car_kind.append(car)
                    car_count.append(1)
                else:
                    car_count[car_kind.index(car)] += 1

            plt.style.use('ggplot')
            plt.rc('font', family = 'Malgun Gothic')
            plt.figure(figsize=(14, 9))
            plt.axis('equal')
            plt.pie(car_count, labels=car_kind, autopct='%1.f%%', startangle=90, textprops={'fontsize': 16})
            plt.title('타임어택에서 사용된 차량의 비율', fontsize=20)
            plt.legend(fontsize=11)
            plt.savefig(f'pages/static/pages/images/car_rate.png')
            result = '1'
        else: # 타임어택 순위 분포도
            divisor = int(request.POST.get('divisor'))
            rank_list_int = [int(data) for data in rank_list] # string형인 rank 데이터를 int형을 변환하여 새로운 리스트에 저장
            max_rank = max(rank_list_int) # 최하위 rank 데이터 저장
            rank_list = rank_list_int # 다시 rank_list에 저장

            x_value = []
            rank_count = [0] * ((max_rank//divisor)) if not max_rank % divisor else [0] * ((max_rank//divisor)+1)
            for i in range(divisor, max_rank + divisor, divisor):
                x_value.append(f'~{i}위')

            for rank in rank_list:
                if not rank % divisor:
                    rank_count[(rank//divisor)-1] += 1
                else:
                    rank_count[rank//divisor] += 1

            n_groups = len(x_value)
            index = np.arange(n_groups)
            plt.rc('font', family = 'Malgun Gothic')
            plt.figure(figsize=(14, 6))
            plt.bar(index, rank_count, 0.8, tick_label=x_value, color='g', align='center')
            plt.xlabel('rank_range', fontsize=15)
            plt.ylabel('rank_count', fontsize=15)
            plt.title('타임어택 순위 분포도', fontsize=20)
            # plt.xticks(index, x_value, fontsize=15)
            plt.savefig(f'pages/static/pages/images/rank_distribution.png')
            result = '2'
    else: # csv 파일이 존재하지 않는 경우
        result = f'{user_nickname}님의 S{select_speed} 채널의 타임어택 기록 csv 파일이 없습니다.'
    
    context = {
        'user_nickname': user_nickname,
        'select_speed': select_speed,
        'divisor': divisor,
        'result': result,
    }

    return render(request, 'pages/analysis_data.html', context)