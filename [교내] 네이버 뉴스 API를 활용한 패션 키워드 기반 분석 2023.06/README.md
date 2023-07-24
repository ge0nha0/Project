# (텍스트데이터분석) 네이버 뉴스 API를 활용한 패션 키워드 기반 분석 프로젝트

<br>

## 프로젝트 기간
- 2023.05.01 ~ 2023.06.06

<br>

## 프로젝트 소개 

* 네이버 뉴스 API를 활용하여 패션 키워드 기반 분석해보기

-데이터: 네이버 뉴스 API + BeautifulSoup를 활용하여 패션 Keyword 25개 수집
* 10대패션, 20대패션, 30대패션, 40대패션, 50대패션, 
* 1980년대패션,1990년대패션,2000년대패션,2010년대패션,2020년대패션, 
* 남자패션, 여자패션, 
* 봄패션,여름패션,가을패션,겨울패션,
* 미국패션, 일본패션, 프랑스패션, 이탈리아패션, 영국패션,
* SPA,나이키,명품,패션워크

<img width="748" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/4022a6f9-c10f-4f8d-aa89-17358ce33a4b">


<br>

## 프로젝트 과정

1. 데이터 수집 (Naver News API)

2. 데이터 전처리 (Cleaning, Tokenization / Pos tagging / Stopword Removal)

<img width="1029" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/af05825f-21b2-46b0-967b-81094e99b967">


3. 텍스트 모델링 (WordCloud, Text Classification)

<img width="993" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/d80fe69b-2fff-44a3-8b44-712dc0463b41">


4. 결론

<img width="924" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/2c151e81-252e-400a-8ed1-1ebe9b01ab73">

<img width="998" alt="image" src="https://github.com/ge0nha0/Projects/assets/100743813/b26f5093-5a90-408e-9a28-3e0126b21761">


<br>

## 느낀점
* NLP의 konlpy package 설치가 되지 않았기 때문에 google colab에서 프로젝트를 진행함. 이를 통해 Jupyter Notebook 말고도 다른 가상환경에서도 데이터분석을 할 수 있어야겠다는 필요성을 느낌.
* 한국어 전처리는 용언이 있기 때문에 매우 어려움. 그래서 Data Cleaning을 전처리 이후에도 계속 진행해야 됨. (매우 중요!)
* Stopwords를 활용하여 데이터전처리를 효과적으로 할 수 있음.
