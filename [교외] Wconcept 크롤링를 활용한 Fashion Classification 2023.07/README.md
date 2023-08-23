# (Toy Project) Wconcept 크롤링를 활용한 Fashion Classification 프로젝트 - Resnet50 / EfficientNet B7

<br>

## 프로젝트 기간
- 2023.06.29 ~ 2023.08.22

<br>

## 프로젝트 소개 

<img width="704" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/4ac93562-c518-4a69-8ffb-e7c98749cbc1">

- 논문 스터디에서 Resnet50과 EfficientNet 모델을 공부하며 관심 있는 패션 분야에 직접 적용해보기 위해서 Toy Project를 진행함.


<br>

## 프로젝트 과정

### 1. 데이터 수집
<img width="1455" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/4b9cbd4d-1c39-44e8-86d6-bee8f66e1d98">

- 카테고리 별로 이미지 크롤링 진행
- 옷 이미지 url, 이미지 저장되는 이름, 옷 카테고리, 카테고리 사이즈, 개별 옷 url, 그 옷의 소재, 제조자(수입자)를 딕셔너리로 저장
- 크롤링 이후 csv 생성

### 2. 이미지 데이터 정제
<img width="1382" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/d97ac50a-db97-4122-b2e4-a883d751dc42">

- 데이터 프레임의 image url 컬럼을 사용하여 이미지 다운로드
- 다운 받은 이미지 데이터 수동 전처리
- train/test 폴더 안에 카테고리 하위 폴더 생성 후, 이미지 업로드

### 3. 데이터 분류
<img width="1402" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/4d5c9145-862c-4db0-910a-9922cfe8bd6e">


- 이미지 파일 이름 넘버링
- 이미지 랜덤 추출하여 train / test split
- train / test의 이미지들을 다시 넘버링 진행

### 4. 이미지 전처리
- 이미지 resize후 tensor 형태로 변환
- resize한 이미지 normalize

### 5. 이미지 Augmentation
 <img width="697" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/3727ff6f-5024-423b-be09-159167956c23">

- torchvision.transforms를 이용해 이미지 augmentation

### 6. 데이터 클래스 정의
- 모델에 들어갈 데이터의 클래스와 loader 정의

### 7. ResNet 50 Modeling
<img width="755" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/ac3bbcce-02a4-4407-b047-9145255995e6">

- summary를 활용하여 출력 tensor 확인
- Layer의 Filter 확인
- ResNet50 Train / Test 진행

### 8. 실험 결과
<img width="703" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/137284b4-b817-47cc-a6bf-b07b8cf745df">

### 9. EfficientNet Modeling
<img width="586" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/b63e3bdf-a44a-4b03-8b38-a30c1ccbe0a2">


<br>

## 느낀점
- 학습을 진행했던 ResNet50보다 pre-training한 EfficientNet B7의 성능이 더 높았음.
- 추후에 EfficientNet보다 성능이 더 뛰어나다고 알려진 ConvNeXt의 모델을 사용해서 적용해보고자 함.
