import csv
import requests
import json
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'data_pages/index.html')


def collect_form(request):
    return render(request, 'data_pages/form.html')


def collect_result(request):
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
    
    context = {'result': result,}

    return render(request, 'data_pages/result.html', context)


def analysis_form(request):
    return render(request, 'data_pages/form.html')


# analysis_data 01. 랭킹 타임어택에서 사용된 차량의 비율 -- 파이 차트
def func_01(cars, nickname, speed): # arguments : car_list, user_nickname, speed, choice_type
    car_kind, car_count = [], []
    for car in cars:
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
    plt.savefig(f'data_img/car_rate_{nickname}_S{speed}.png')
    plt.savefig(f'data_pages/static/data_pages/images/car_rate.png')
    return '1' # 어떤 형태의 데이터를 추출했는지 확인하는 변수

# analysis_data 02. 랭킹 타임어택 순위 분포도 -- 막대 그래프
def func_02(ranks, divisor, nickname, speed): # arguments : rank_list, user_nickname, speed, chice_type
    rank_list_int = [int(data) for data in ranks] # string형인 rank 데이터를 int형을 변환하여 새로운 리스트에 저장
    max_rank = max(rank_list_int) # 최하위 rank 데이터 저장
    ranks = rank_list_int # 다시 rank_list(여기서는 ranks 변수임)에 저장

    x_value = []
    rank_count = [0] * ((max_rank//divisor)) if not max_rank % divisor else [0] * ((max_rank//divisor)+1)
    for i in range(divisor, max_rank + divisor, divisor):
        x_value.append(f'~{i}위')
    x_value[-1] = f'{i - divisor + 1}위~'

    for rank in ranks:
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
    plt.savefig(f'data_img/rank_distribution_{nickname}_S{speed}_(gap_{divisor}).png')
    plt.savefig(f'data_pages/static/data_pages/images/rank_distribution.png')
    return '2'


def analysis_result(request):
    rank_list, car_list = [], []
    csv_file_exist = 1 # 해당 채널의 csv 파일이 있는지 확인하기 위한 변수
    
    # form 태그로 POST 방식으로 넘어논 데이터들 추출
    user_nickname = request.POST.get('user_nickname')
    speed = request.POST.get('speed')
    choice_type = int(request.POST.get('Select_data')[0])
    
    select_speed = int(speed[1]) # string형의 speed 변수를 숫자 데이터만 추출하여 int형으로 변환

    # csv 파일에서 순위 데이터와 차량 데이터를 추출하여 rank_list, car_list에 추가
    try:
        with open(f'timeattack_{user_nickname}_S{select_speed}.csv', newline='', encoding='utf-8') as f:
            record_data = csv.DictReader(f)
            for data in record_data:
                rank_list.append(data['rank'])
                car_list.append(data['car'])
    # csv 파일이 없는 경우 체크 변수를 0으로 설정
    except FileNotFoundError:
        csv_file_exist = 0

    if csv_file_exist: # csv 파일이 존재하는 경우
        if choice_type == 1:
            result = func_01(car_list, user_nickname, select_speed)
        else: # 타임어택 순위 분포도
            divisor = int(request.POST.get('divisor')) # 2. 순위 분포도 gap 설정을 위한 변수
            result = func_02(rank_list, divisor, user_nickname, select_speed)
    else: # csv 파일이 존재하지 않는 경우
        result = f'{user_nickname}님의 S{select_speed} 채널의 타임어택 기록 csv 파일이 없습니다.'
    
    context = {
        'user_nickname': user_nickname,
        'select_speed': select_speed,
        'result': result,
    }

    return render(request, 'data_pages/result.html', context)

def back_analysis_menu(request):
    return redirect('data_pages:analysis_form')