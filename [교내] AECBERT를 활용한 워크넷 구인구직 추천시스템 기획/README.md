# [딥러닝] AECBERT를 활용한 워크넷 구인구직 추천시스템 기획 프로젝트

<br>

## 프로젝트 기간
- 2023.03.15 ~ 2023.07.21

<br>

## 프로젝트 소개 

- 학교 [딥러닝] 최종 프로젝트
- 협업-콘텐츠 기반의 하이브리드 추천시스템 기획 ‘AECBERT’

<img width="705" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/18b044b1-1a6d-4266-854c-f690bb4d82f6"> 


<br>

## 프로젝트 과정

### 0. 선행연구조사

* AutoEncoders
* DeepFM
* BERT (Embedding)
* HyBrid Recommender Systems

<img width="696" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/9b854ed3-63db-4290-a775-5c0062020f9f"> <img width="705" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/18b044b1-1a6d-4266-854c-f690bb4d82f6"> 

<img width="320" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/48268fee-87e4-43fb-91ea-e5105a1c3db4"> <img width="691" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/44cc9134-aee5-41ef-9377-00ead0c6273c">



### 1.  워크넷 특징 및 문제 정의

<img width="708" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/30edcd8f-f82e-4c4d-9ee5-7ba6c3a28c08">


###  2. 제안 모델

* 협업필터링 + 콘텐츠 기반 필터링 + Similar Document Augmentation

<img width="694" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/6973a5dd-95c3-4992-a4b2-1991b550393b">


### 3. Data Augmentation

<img width="703" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/fc4a2a0b-061f-4401-a36b-2d95f2fa8043">

### 4. 결론

<img width="695" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/4bf87d25-4e3f-4848-a533-32d2cc049469">

### 5. 한계

<img width="646" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/eb242ecd-f391-42a2-b01b-abf2a9cb382b">


<br>

## 느낀점

* 사실 딥러닝 수업에서 추천시스템을 배우지는 않았다. 따로 책과 논문을 통해 공부를 진행했었는데, 직접 찾아보고 지식을 습득하는 과정에서 많이 배웠고, 머릿속에도 기억이 많이 남았다.
* 정말 아쉬운 점은 사용자의 로그 데이터가 없었기 때문에 개발을 할 수 없었고, 기획만 했다는 점이다.
* 그리고 만약 개발을 한다고 해도 BERT의 사전학습 모델에 필요한 대량의 Corpus가 없고, 현재 상황에서의 컴퓨팅 환경에서는 불가능하기 때문에 이 부분이 아쉬웠다.
