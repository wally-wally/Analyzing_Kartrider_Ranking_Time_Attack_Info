import csv
import matplotlib.pyplot as plt
import numpy as np

rank_list = []
car_list = []
csv_file_exist = 1 # 해당 채널의 csv 파일이 있는지 확인하기 위한 변수

user_nickname = input('닉네임을 입력하세요. : ')
while True:
    speed = input('원하는 타임어택 기록의 속도(채널)을 입력하세요.(S0, S1, S2, S3중 하나 입력) : ')
    if speed not in ['S0', 'S1', 'S2', 'S3']:
        print('채널 명칭을 올바르게 다시 입력하세요.')
    else:
        break
select_speed = int(speed[-1])

try:
    with open(f'timeattack_{user_nickname}_S{select_speed}.csv', newline='', encoding='utf-8') as f:
        record_data = csv.DictReader(f)
        for data in record_data:
            rank_list.append(data['rank'])
            car_list.append(data['car'])
except FileNotFoundError:
    csv_file_exist = 0


if csv_file_exist: # csv 파일이 존재하는 경우 데이터 분석 가능
    print('========Select data what you want========')
    print('1.타임어택에서 사용된 차량의 비율 -- 파이 차트')
    print('2.타임어택 순위 분포도 -- 막대 그래프')
    print('=========================================')

    while True:
        choice_type = int(input('1 또는 2를 입력하세요. : '))
        if choice_type == 1 or choice_type == 2:
            break
        else :
            print('다시 입력하세요.')

    if choice_type == 1: # 타임어택에서 사용된 차량의 비율
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
        plt.figure(figsize=(12, 8))
        plt.axis('equal')
        plt.pie(car_count, labels=car_kind, autopct='%1.f%%', startangle=90, textprops={'fontsize': 15})
        plt.title('타임어택에서 사용된 차량의 비율', fontsize=20)
        plt.legend(fontsize=12)
        plt.savefig(f'data_graph_img/car_rate_{user_nickname}_S{select_speed}.png')
        plt.show()

    else: # 타임어택 순위 분포도
        rank_list_int = [int(data) for data in rank_list] # string형인 rank 데이터를 int형을 변환하여 새로운 리스트에 저장
        max_rank = max(rank_list_int) # 최하위 rank 데이터 저장
        rank_list = rank_list_int # 다시 rank_list에 저장

        while True:
            divisor = int(input('원하는 순위 간격을 입력하세요.(단, 10의 배수로만 입력) : '))
            if divisor % 10:
                print('10의 배수 숫자로 다시 입력하세요.')
            else:
                break

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
        plt.figure(figsize=(16, 8))
        plt.bar(index, rank_count, 0.8, tick_label=x_value, color='g', align='center')
        plt.xlabel('rank_range', fontsize=15)
        plt.ylabel('rank_count', fontsize=15)
        plt.title('타임어택 순위 분포도', fontsize=20)
        # plt.xticks(index, x_value, fontsize=15)
        plt.savefig(f'data_graph_img/rank_distribution_{user_nickname}_S{select_speed}_(gap_{divisor}).png')
        plt.show()
else: # csv 파일이 존재하지 않는 경우
    print(f'{user_nickname}님의 S{select_speed} 채널의 타임어택 기록 csv 파일이 없습니다.')