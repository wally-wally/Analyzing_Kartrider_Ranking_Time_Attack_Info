# :pencil: README

<br>

## :one: Summary

**:racing_car: 온라인 게임 'Kartrider'의 Timeattack 데이터를 수집하고 분석**

​	:round_pushpin: `bootstrap`, `django`를 이용하여 데이터를 관리할 수 있는 홈페이지 제작

​	:round_pushpin: 유저의 닉네임과 채널명을 입력하여 csv 파일로 타임어택 데이터 수집

​	:round_pushpin: 작성된 csv 파일로 데이터를 분석하여 원하는 정보를 차트형태로 출력

<br>

## :two: Flow Chart

![flow_chart](https://user-images.githubusercontent.com/52685250/63640446-666bf780-c6db-11e9-9810-c4c675cf00a7.jpg)

<br>

## :three: Getting Started

- 소스 코드 clone 받기

```bash
git clone https://github.com/wally-wally/Analyzing_Kartrider_Ranking_Time_Attack_Info.git
```

- 가상환경 설정

```bash
python -m venv venv
source venv/Scripts/activate
```

- 필요한 라이브러리 패키지 설치

```bash
pip install -r requirements.txt
```

- DB 설정(sqlite3가 설치되어 있다는 가정하에 진행할 것)

```bash
python manage.py makemigrations
python manage.py migrate
```

- 로컬에서 서버 실행

```bash
python manage.py runserver
```

<br>

## :four: Homepage Configuration(Main Page)

:heavy_check_mark: <b>login 전 상태</b>

![01](https://user-images.githubusercontent.com/52685250/67218979-3b471f80-f462-11e9-97a6-b0bd455f211a.JPG)

:heavy_check_mark: <b>login 후 상태</b>

![02](https://user-images.githubusercontent.com/52685250/67218980-3bdfb600-f462-11e9-9148-5171d287dea3.JPG)

- `navbar`
  - 좌측 상단
    - 로그인 전에는 `로그인`, `회원가입` 메뉴가 표시됨
    - 로그인 후에는 `Account Management`와 메인 페이지로 갈 수 있는 `Back` 메뉴가 표시되며 `Account Management`를 선택하면 Dropdown 형태로 계정을 관리할 수 있는 기능들이 표시됨
  - 우측 상단
    - `Go to 'wally-wally GitHub'` : 제작자의 GitHub 주소로 연결되도록 링크 설정
    - `Hello, Guest` 또는 `Hello, user_name` : 로그인을 안 한 경우 `Guest`로, 로그인을 한 경우 로그인한 user_name으로 이름이 표시됨
- `Select Menu`
  - 각 메뉴는 `bootstrap`의 component인 `collapse`을 이용하여 각 메뉴를 선택하면 상세 설명을 볼 수 있도록 구성
  - 또한  `bootstrap`의 component인 `carousel`을 이용하여 상세 설명에서 예시과정 캡쳐화면을 추가
  - 각 메뉴 선택 후 `Move` 버튼을 클릭하면 각 해당 전용 페이지로 이동
  - `★Go to play Kartrider!★` : 카트라이더 메인 홈페이지 주소를 링크로 설정

<br>

## :four: Changes

- `2019/08/25` (ver 1.0)
  - `Collect Data`
    - 데이터 수집 상태를 홈페이지에 출력되는 문구의 글꼴 수정
  - `Analysis Data`
    - 차트를 파일로 저장하여 활용할 수 있도록 `data_graph_img` 폴더에 자동으로 저장되도록 기능 추가
    - `2.타임어택 순위 분포도` 차트 출력시 마지막 범위로 csv 파일에 저장된 rank의 최댓값을 기준으로 하여 그 이상 순위의 `rank_count`를 표시하도록 코드 수정
    - csv 파일이 없어 데이터 분석을 할 수 없을 때 출력되는 문구의 글꼴 수정

<br>

- `2019/10/22` (ver 1.1)
  - 계정(account) 관련 기능 추가
    - 회원가입, 로그인, 회원 정보 수정, 비밀번호 변경, 회원탈퇴
    - 로그인을 해야 홈페이지 기능 사용 가능
  - project이름, app이름 view 이름 변경
  - `analysis_result` 를 통해 만드는 데이터를 분석하는 부분을 별도 함수로 분리하여 작성
    - `func_01` : 랭킹 타임어택에서 사용된 차량 종류의 비율 - 파이 차트
    - `func_02` : 랭킹 타임어택 순위 분포도 - 막대 그래프
  - app_name을 이용한 url 재구성
  - template 재구성
    - base templates `data_pages` app의 templates 폴더로 이동
    - `resolver`를 이용하여 `data_pages`의 `collect_form.html`, `analysis_form.html`을 `form.html` templates으로 합치고,  `collect_result.html`, `analysis_result.html`을 `result.html` templates으로 합침

<br>

- `2019/10/23` (ver 1.2.1)
  - 추출한 데이터를 저장할 수 있는 `Data Storage` 데모 버전 구현
  - 추출한 데이터의 종류, 유저 닉네임, 채널명, 그래프를 볼 수 있으며 필요에 따라 데이터 삭제도 가능
  - 추후 데이터별 이미지를 각각 저장할 수 있도록 구현할 계획

<br>

- `2020/10/12` (ver 1.2.1)
  - 카트라이더 내 차고 홈페이지 변경된 URL 주소 반영