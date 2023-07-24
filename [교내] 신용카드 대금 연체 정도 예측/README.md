# [D&A Machine Learning Session] 신용카드 대금 연체 정도 예측 프로젝트

<br>

## 프로젝트 기간
- 2022.11.01 ~ 2022.11.29

<br>

## 프로젝트 소개 
* 신용카드 사용자 데이터를 통해 사용자의 대금 연체 정도를 예측하는 알고리즘 개발 
* 평가지표: Logloss
  
<img width="881" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/140c3a83-05dc-4bcd-a0ff-46ad1f1eafe2">


<br>

## 프로젝트 과정

1. EDA & Data preprocessing

2. 다양한 Feature를 생성하여 예측 성능 향상
   
3. Ensemble 전략
-> 각 모델들의 상관관계를 낮추기 위해서 각 팀원들이 각자 다른 모델을 선택해 모델학습을 진행함

<img width="833" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/e753c695-555f-45f1-8700-127cc8a4cfdf">


4. 각자 만든 Feature를 모두 합쳐서 Catboost 단일모델로 모델학습을 진행함

<img width="789" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/2dceb682-8a0c-4154-8ec3-c3dbd0dd9ade">


5. 중복되는 Feature를 제거하여 기본변수까지 포함하여 총 98개의 Feature를 생성함

6. Feature importance를 직접 확인해서 중요도가 낮은 Feature 10개를 삭제했지만, 성능이 떨어짐

7. Feature를 모두 합친 Catboost 모델을 최종모델로 선택함

<br>

## 느낀점
* Ensemble의 성능 향상 도모를 위해서는 데이터 간의 독립성이 최대한 보장되어야한다. 하지만 생성한 feature set들이 매우 비슷해서 Ensemble에서 좋은 성능을 기대할 수 없었음.  -> feature 중복
* 오로지 성능 향상을 위해 다양한 Feature를 생성했다는 점이 너무 아쉬움. Feature Importance를 시각화해봐도 Top 위치에 있는 Feature들이 왜 성능이 좋은지에 대한 이유를 말할 수 없음. -> 설명 가능 X
