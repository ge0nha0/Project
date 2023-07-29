# [회귀분석]'성인근로자의 근무형태·수면시간이 건강 관련 삶의 지수에 미치는 영향' 프로젝트

<br>

## 프로젝트 기간
- 2021.11.01 ~ 2021.12.10

<br>

## 프로젝트 소개 
- 자료는 국민건강영양조사 제8기 1차년도(2019년)자료를 이용하였다. 모름, 무응답은 결측치로 간주했고, 결측치는 모두 제거하고 분석하였다.
- 대상을 야간근무자와 주간근무자로 선정하였으며 삶의 질의 차이와 흡연, 음주, 운동이 교대 근무시 삶의 질과 건강상태에 미치는 관련성을 확인하였다.
- 이 분석은 야간근무자에 대한 삶의 질 향상에 건강관리 기초자료를 제공하는 것에 의의를 둔다.

<br>

## 프로젝트 과정

### 1. 변수 설정
* 종속 변수: HINT-8 지수
* 독립 변수
  -BP16_1: 주중 하루 평균 수면시간
  -EC_wht_23: 주당 평균 근로시간
  -BE3_32: 걷기 지속 시간
  -BS3_2(성인): 하루평균 흡연량
  -EC_wht_23: 주당 평균 근로시간
  -BE3_87: 여가_중강도 신체활동 시간
  -sex: 성별 (0:여자, 1:남자)
  -edu: 교육수준
  -EC_wht: 변형근로시간 (0:야간근무, 1: 주간+저녁근무)

<img width="842" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/15878c41-8697-450b-a3f9-511bcc0e3976">

### 2. 변수선택 기준 및 선택 방법

* 수정된 결정계수와 MSE
* Mallows-Cp
* BIC
* PRESS_p
* 단계별 회귀 -> 전진 선택법 -> 후진제거법

<img width="600" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/2519d982-32c3-4d45-aacd-e3268c87afc2">

### 3. 회귀진단 및 모형확인

* 편회귀그림
* 적합결여검정
* 변수변환 (분산안정화 변환 / 정규성을 위한 변환)

<img width="622" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/abb6dc02-9ea0-4bb6-9582-5a89496b33e0">


### 4. 다중공선성 확인

<img width="428" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/f34dc7bd-4f37-47ab-b4c8-8b1d4f9a1eda">


### 5. 잔차분석 & 지렛값

<img width="554" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/eacd1f2a-3d97-4d92-a6a9-cb6584f304fd">


### 6. 영향력 측도

* Cook's distance
* DFBETAS
* DFFITS
* COVRATIO

<img width="608" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/96448d98-b021-4559-bde7-ebaf8fe27f24">


### 7. 더빈-왓슨 검정

<img width="299" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/a1ab6bbc-65f5-420b-9afb-6466539b190d">


### 8. 모형 확인

<img width="557" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/1b216eab-630e-4e98-a755-de05707f6c18">


### 9. 결론

* 근무형태에 따른 평균 HINT_8지수가 효과가 있음.

<img width="586" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/36cc3911-5cdd-4c9e-96e0-56c4354c1b6f">

<br>

## 느낀점
* 설명변수를 너무 적게 설정하여 R^2값의 유의미한 결과를 도출할 수 없었음.
* 변수를 선택할 때 P-value 값을 기준으로 많이 한 것 같아서 변수가 유의미하지 않을 수도 있음.
