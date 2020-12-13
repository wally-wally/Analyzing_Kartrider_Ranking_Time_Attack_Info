# :pencil: README

<br>

## :one: Summary

**:racing_car: 온라인 게임 'Kartrider'의 Timeattack 데이터를 수집하고 분석**

​	:round_pushpin: `Django`를 이용하여 랭킹 타임어택 데이터를 관리할 수 있는 홈페이지 제작

​	:round_pushpin: 유저의 닉네임과 채널명을 입력하여 csv 파일로 타임어택 데이터 수집

​	:round_pushpin: 작성된 csv 파일로 데이터를 분석하여 원하는 정보를 차트형태로 출력

<br>

## :two: Tech Stack

:round_pushpin: <b>Programming Language</b> : `Python 3.7.4`

:round_pushpin: <b>Frontend, Backend</b> : `Django 2.2.4`

:round_pushpin: <b>Database</b> : `sqlite3`

:round_pushpin: <b>Data Analysis</b> : `numpy 1.17.0`

:round_pushpin: <b>Chart Library</b> : `matplotlib 3.1.1`

:round_pushpin: <b>Development Enviornment</b> : `Windows 10`

:round_pushpin: <b>Using Editor</b> : `Visual Studio Code`

<br>

## :three: Getting Started

:heavy_check_mark: <b>소스 코드 clone 받기</b>

```bash
git clone https://github.com/wally-wally/Analyzing_Kartrider_Ranking_Time_Attack_Info.git
```

:heavy_check_mark: <b>가상환경 설정</b>

- Python 3.7 이상의 버전을 우선 설치하고 아래 명령어를 입력해주세요.

```bash
python -m venv venv
source venv/Scripts/activate
```

:heavy_check_mark: <b>필요한 라이브러리 패키지 설치</b>

```bash
pip install -r requirements.txt
```

:heavy_check_mark: <b>Database 설정</b>

- sqlite3를 우선 설치하고 아래 명령어를 입력해주세요.

```bash
python manage.py makemigrations
python manage.py migrate
```

:heavy_check_mark: <b>로컬환경에서 서버 실행</b>

```bash
python manage.py runserver
```

:heavy_check_mark: <b>메인 페이지로 이동</b>

- `http://127.0.0.1:8000/data_pages/`

<br>

## :four: Flow Chart

![flow_chart](https://user-images.githubusercontent.com/52685250/63640446-666bf780-c6db-11e9-9810-c4c675cf00a7.jpg)

<br>

## :five: Homepage Configuration

### (1) 메인 페이지, 회원가입, 로그인

![001](https://user-images.githubusercontent.com/52685250/102000938-ca328d80-3d2f-11eb-9723-2730930ef4b6.PNG)

![002](https://user-images.githubusercontent.com/52685250/102000940-cb63ba80-3d2f-11eb-8075-cf54ff89c9f3.PNG)

![003](https://user-images.githubusercontent.com/52685250/102000941-cb63ba80-3d2f-11eb-97ac-801ad4fbb62f.PNG)

<br>

### (2) 데이터 수집

![004](https://user-images.githubusercontent.com/52685250/102000942-cbfc5100-3d2f-11eb-9c50-788f7082427b.PNG)
![005](https://user-images.githubusercontent.com/52685250/102000943-cbfc5100-3d2f-11eb-9127-443a9f437ea7.PNG)

- 유저 닉네임과 채널명을 선택한 후 `Send` 버튼을 누르면 카트라이더 내 차고 페이지에서 해당 유저의 랭킹 타임어택 데이터를 크롤링합니다.
- `데이터 수집이 완료되었습니다.` 라는 문구가 나오면 성공적으로 크롤링한 데이터를 csv 파일로 저장했고 이 파일은 해당 프로젝트의 루트 디렉토리에 저장됩니다.
- 만약 해당 채널(ex. `S1`)에서 랭킹 타임어택을 진행하지 않은 경우 `S1의 타임어택을 진행하지 않았습니다.` 라는 문구가 나오고 유저 닉네임이 존재하지 않으면 `OOO님의 라이더 정보가 없습니다.` 라는 문구가 나옵니다.

<br>

### (3) 데이터 분석

- 타임어택에서 사용된 차량의 비율(파이 차트)

![006](https://user-images.githubusercontent.com/52685250/102000944-cc94e780-3d2f-11eb-8023-fd313495e75d.PNG)
![007](https://user-images.githubusercontent.com/52685250/102000945-cc94e780-3d2f-11eb-979d-026ce398a13d.PNG)
![008](https://user-images.githubusercontent.com/52685250/102000946-cd2d7e00-3d2f-11eb-9540-0b70b605d6c9.PNG)

- 타임어택 순위 분포도(막대 그래프)

![009](https://user-images.githubusercontent.com/52685250/102000947-cd2d7e00-3d2f-11eb-9b84-a184f8c5b491.PNG)
![010](https://user-images.githubusercontent.com/52685250/102000948-cdc61480-3d2f-11eb-9b0f-8166ca592427.PNG)

- 유저 닉네임과 채널명 그리고 보고 싶은 데이터의 유형을 선택한 후 `Send` 버튼을 클릭하면 `Data Storage` 페이지로 이동됩니다.
- 그 후 `DETAIL` 버튼을 클릭하면 분석된 차트 정보를 볼 수 있습니다.
- 참고로 타임어택 순위 분포도는 순위 간격을 지정해줘야 하기 때문에 `rank interval` 항목을 꼭 입력해줘야 합니다.
- <b><u>그리고 데이터 분석은 데이터 수집이 완료된 항목에 대해서만 가능하지 이점 유의하시기 바랍니다!</u></b>
  - ABC님의 S2 채널 랭킹 타임어택 데이터를 수집한 경우 ABC님의 S2 채널 데이터 분석 가능하지만 S1 채널 데이터는 수집하지 않았기 때문에 S1 채널의 데이터 분석은 불가능

