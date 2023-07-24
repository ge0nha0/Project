# [D&A Basic Session] 'COVID19 집단감염의 추이로 본 정책의 효과' 데이터분석 프로젝트

<br>

## 프로젝트 기간
- 2022.04.25 ~ 2022.05.24

<br>

## 프로젝트 소개 
국민대학교 D&A 학회 BASE SESSION 시각화 Competition이었으며, 'COVID19 집단감염의 추이를 통해 정책의 효과에 대한 데이터분석'을 하는 프로젝트이다.

데이터는 다음과 같다.
* (1) Patientinfo.csv (2020.01.20 ~ 2020.06.30까지의 코로나 환자 데이터)
* (2) Region.csv (지역 정보 데이터)
* (3) Weather.csv (날씨 데이터)
* (4) Searchtrend.csv (2016.01.01 ~ 2022.06.29까지의 해당 단어 검색 비율 데이터)
* (5) Policy.csv (정부가 날짜별로 어떠한 관련 정책을 발령했는지에 대한 데이터)
* (6) Case.csv (유명한 코로나 발생 케이스에 대한 데이터)

<br>

## 프로젝트 과정

### 0. 문제 정의
* 행정학에서 배운 재난관리 Process로 시작 (행정학 Domain 활용)
<img width="676" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/f398b90f-c530-4f5b-92c0-df38bfd6d46b">

* 신종 인플루엔자, 메르스 등 이전 감염병 사례가 있었음에도 코로나 대응 정책이 미흡하였음 

### 1. 데이터 전처리
* 결측치 대체
* data feature 문자열 -> Datetime 형태로 변환

### 2. 데이터 시각화
* seaborn, pyecharts(Bar)를 활용하여 시각화 진행
* 집단감염 시작일과 정책 시행일 시각화
* 신천지 교회 집단감염 추세 시각화
* 31번 확진자 확정 판정일 기준 전후 비교
* 이태원 클럽 집단감염 추세 시각화
* 정책 시행 전후 연령대별 확진자 비교
* 쿠팡 물류센터 집단감염 추세 시각화
* 6/12 전후 서울, 인천, 경기 확진자 비교

<img width="1608" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/e6e2e76e-f2bd-4fc5-a881-40db5b5b911a">

<img width="1599" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/e170f0a6-afd4-4384-b471-38e1dffca9cc">



<br>

## 느낀점
* 데이터 시각화를 통해 정부와 국민들이 재난상황에서의 "골든타임"의 중요성을 기억하며 예방 및 대비를 철저히 했으면 좋겠음
* Github 같은 협업툴을 활용하여 팀 프로젝트의 효율성에 대한 중요성을 알 수 있었음
