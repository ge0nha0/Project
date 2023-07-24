# [Machine Learning] Categorical Feature Encoding 프로젝트

<br>

## 프로젝트 기간
- 2022.10.28 ~ 2022.11.04

<br>

## 프로젝트 소개 
* Categorical Feature Encoding 실험 및 분석

* 실험데이터: Kaggle의 Categorical Feature Encoding Challenge II에서 제공하는 데이터
  
* 적용모델: Logistic Regression, Decision Tree, MLP (반드시 튜닝할 필요없음)
  
* 분석내용: 
(1, 필수) 모델별로 어떤 Categorical Feature Encoding 기법이 유용한가?
(2, 선택) Categorical Feature 유형(binary features, low- and high-cardinality nominal features, low- and high-cardinality ordinal features, cyclical features)
별로 적합한 Categorical Feature Encoding이 있는가?

<img width="835" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/fc9f3377-50a2-4299-9b12-54897c512db3">

<br>

## 프로젝트 과정

1. Categorical Feature Encoding 기법 & 전략

2. 모델별 Encoding 성능 비교

<img width="688" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/22fb7a90-0fda-4eed-814d-88c01435181d">


3. 모델별 Encoding 분석

4. 고유값 기준으로 Feature 분류

5. Feature 종류별로 Encoding

<img width="1231" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/08f6a0bd-76f8-4864-98cc-6c4fb47fb685">


6. 최적의 조합

<img width="707" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/5ce9895b-bd38-4a05-857b-5cf80b64ebe4">


<br>

## 느낀점
* 모든 모델에서 베이지안 기반의 Encoder기법이 유용했고, 베이지안 Encoder기법을 제외하면
* Logistic Regresssion에서는 One-Hot Encoding,
* Decision Tree에서는 Ordinal Encoding,
* MLP에서는 Leave One Out Encoding이 가장 유용했음


* Norminal Feature의 경우, 카디널리티가 낮을 때는 One-hot Encoding, 카디널리티가 높을 때는 베이지안 기반의 M-Estimator Encoding이 가장 유용했음.
* Ordinal Feature의 경우, Ordinal Encoding이 가장 유용함.
* Cyclical Feature의 경우, One-hot Encoding이 가장 유용함.

