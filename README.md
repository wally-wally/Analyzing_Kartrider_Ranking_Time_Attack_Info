# :pencil: README(written by wally-wally)

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

## :three: Homepage Configuration(Main Page)

![main](https://user-images.githubusercontent.com/52685250/63640482-d4b0ba00-c6db-11e9-9d0b-8ea4d653cf69.JPG)

- `navbar`
  - 좌측 상단에
    - `Kartrider_search_myinfo(Data Analysis) (made by wally-wally)` : 홈페이지의 메인 주제와 만든이의 GitHub 닉네임을 작성
  - 우측 상단
    - `Go to 'wally-wally GitHub'` : 제작자의 GitHub 주소로 연결되도록 링크 설정
    - `Send e-mail to wally-wally` : 제작자에게 e-mail을 보낼 수 있도록 링크 설정
- `Select Menu`
  - 각 메뉴는 `bootstrap`의 component인 `collapse`을 이용하여 각 메뉴를 선택하면 상세 설명을 볼 수 있도록 구성
  - 또한  `bootstrap`의 component인 `carousel`을 이용하여 상세 설명에서 예시과정 캡쳐화면을 추가
  - 각 메뉴 선택 후 `Move` 버튼을 클릭하면 각 해당 전용 페이지로 이동
  - `★Go to play Kartrider!★` : 카트라이더 메인 홈페이지 주소를 링크로 설정