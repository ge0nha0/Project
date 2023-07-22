#!/usr/bin/env python
# coding: utf-8

# # 1. 데이터 수집
# ## Naver News 
# ### Naver API와 BeautifulSoup을 활용
# #### 데이터 수집은 Jupyter Notebook에서 돌렸고, csv 파일을 구글 드라이브에 옮겼습니다.

# In[ ]:


import os
import sys
import time
import urllib.request
import time
import json
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tqdm import tqdm

import pandas as pd
import numpy as np


# In[ ]:


client_id = # client id 
client_secret = # client secret

base_url = 'https://openapi.naver.com/v1/search/news.json'
query = '영국패션' # 검색할 키워드 
encQuery = urllib.parse.quote(query.encode('utf-8')) 
n_display = 10 # 한 번에 보여줄 검색 결과 수
sort = 'sim' # 검색 결과 정렬 방식
search_result_li = []  # 검색 결과를 저장할 리스트

for start in range(1,999,10): #1~100페이지
    url = f'{base_url}?query={encQuery}&display={n_display}&start={start}&sort={sort}'
    my_request = urllib.request.Request(url)  # URL로 요청 객체 생성
    my_request.add_header("X-Naver-Client-Id",client_id)  # Client-Id 헤더 추가
    my_request.add_header("X-Naver-Client-Secret",client_secret)  # Client Secret 헤더 추가
    response = urllib.request.urlopen(my_request) # 요청 보내고 응답 받음
    rescode = response.getcode() # 응답 상태 코드 확인
  
    if(rescode==200):  # 응답이 성공적으로 받아온 경우
        response_body = response.read()  # 응답 데이터 읽기
    else:
        print("Error Code:" + rescode)  # 응답이 정상적이지 않을 경우 에러 코드 출력
    search_result_str = response_body.decode('utf-8')  # 응답 데이터를 문자열로 디코딩
    search_results = json.loads(search_result_str)  # JSON 형식의 응답 데이터를 파싱하여 Python 객체로 변환
    search_result_li.append(search_results)  # 검색 결과를 리스트에 추가
print(search_result_li) # 모든 검색 결과를 출력


# In[ ]:


titles_li = [] # 뉴스 제목을 저장할 리스트
links_li = []  # 뉴스 링크를 저장할 리스트

for result in search_result_li:  # 이전에 검색한 모든 검색 결과에 대해 반복
    titles = []  # 현재 검색 결과의 뉴스 제목을 저장할 리스트
    links = []   # 현재 검색 결과의 뉴스 링크를 저장할 리스트
    p = re.compile('https://n.news.naver.com/.+')  # 정규표현식을 사용하여 네이버 뉴스 링크인지 확인하는 패턴 생성
    for item in result['items']:
        if p.match(item['link']):  # item의 링크가 네이버 뉴스 링크인지 확인
            title = item['title']  # item의 제목 추출
            link = item['link']    # item의 링크 추출
            titles.append(title)   # 현재 검색 결과의 뉴스 제목 리스트에 추가
            links.append(link)     # 현재 검색 결과의 뉴스 링크 리스트에 추가
    titles_li += titles            # 현재 검색 결과의 뉴스 제목 리스트를 전체 뉴스 제목 리스트에 추가
    links_li += links              # 현재 검색 결과의 뉴스 링크 리스트를 전체 뉴스 링크 리스트에 추가

print('뉴스 개수 :' ,len(links_li))  # 전체 뉴스 개수 출력


# In[ ]:


article_ids = ['newsct_article', 'articeBody']
contents = []

for link in tqdm(links_li):  # 이전에 수집한 모든 뉴스 링크에 대해 반복
    html = urllib.request.urlopen(link)         # 뉴스 링크로부터 HTML 데이터 가져오기
    bs_obj = BeautifulSoup(html, 'html.parser') # BeautifulSoup를 사용하여 HTML 파싱
    for article_id in article_ids:  # 본문을 찾기 위한 HTML 요소의 id 리스트에 대해 반복
        content = bs_obj.find_all('div', {'id':article_id})
        if len(content) > 0:   # 해당 id를 가진 HTML 요소를 찾은 경우
            contents.append(content[0].text)   # 첫 번째 HTML 요소의 텍스트를 뉴스 본문 리스트에 추가
            break
        else:   # 해당 id를 가진 HTML 요소를 찾지 못한 경우
            continue
        time.sleep(3)


# In[ ]:


result_dict = {'제목': titles_li, '내용': contents}
df = pd.DataFrame.from_dict(result_dict)
print(len(df))
df # dataframe 형태로 만듬


# In[ ]:


df.to_csv('{}_뉴스.csv'.format(query),encoding='utf-8-sig',index=False)


# ## Colab 패키지 불러오기

# In[ ]:


import os, sys
from google.colab import drive
drive.mount('/content/drive')


# In[ ]:


get_ipython().system('pip install konlpy')
get_ipython().system('pip install wordcloud')
get_ipython().system('pip install nltk')


# In[ ]:


# 코랩 패키지 버전 확인
get_ipython().system('pip show konlpy # 0.6.0')
get_ipython().system('pip show wordcloud #1.8.2.2')
get_ipython().system('pip show nltk # 3.8.1')
get_ipython().system('python --version # 3.10.11')


# In[ ]:


fs_10 = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/10대패션_뉴스.csv')
fs_20 = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/20대패션_뉴스.csv')
fs_30 = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/30대패션_뉴스.csv')
fs_40 = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/40대패션_뉴스.csv')
fs_50 = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/50대패션_뉴스.csv')

fs_1980 = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/1980년대패션_뉴스.csv')
fs_1990 = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/1990년대패션_뉴스.csv')
fs_2000 = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/2000년대패션_뉴스.csv')
fs_2010 = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/2010년대패션_뉴스.csv')
fs_2020 = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/2020패션_뉴스.csv')

fs_m = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/남자패션_뉴스.csv')
fs_w = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/여자패션_뉴스.csv')

fs_sp = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/봄패션_뉴스.csv')
fs_su = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/여름패션_뉴스.csv')
fs_au = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/가을패션_뉴스.csv')
fs_wi = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/겨울패션_뉴스.csv')

fs_usa = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/미국패션_뉴스.csv')
fs_jap = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/일본패션_뉴스.csv')
fs_fra = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/프랑스패션_뉴스.csv')
fs_ita = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/이탈리아패션_뉴스.csv')
fs_eng = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/영국패션_뉴스.csv')

fs_spa = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/SPA_뉴스.csv')
fs_nike = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/나이키_뉴스.csv')
fs_lux = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/명품_뉴스.csv') 
fs_work = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/패션워크_뉴스.csv')


# In[ ]:


print(fs_10.shape)
print(fs_20.shape)
print(fs_30.shape)
print(fs_40.shape)
print(fs_50.shape)

print(fs_1980.shape)
print(fs_1990.shape)
print(fs_2000.shape)
print(fs_2010.shape)
print(fs_2020.shape)

print(fs_m.shape)
print(fs_w.shape)

print(fs_sp.shape)
print(fs_su.shape)
print(fs_au.shape)
print(fs_wi.shape)

print(fs_usa.shape)
print(fs_jap.shape)
print(fs_fra.shape)
print(fs_ita.shape)
print(fs_eng.shape)

print(fs_spa.shape)
print(fs_nike.shape)
print(fs_lux.shape)
print(fs_work.shape)


# In[ ]:


# 키워드 열 추가하기 -> drop_duplicates 후에 키워드 별로 정리할 때 편하게 하기 위함
fs_10['키워드'] = '10대패션'
fs_20['키워드'] = '20대패션'
fs_30['키워드'] = '30대패션'
fs_40['키워드'] = '40대패션'
fs_50['키워드'] = '50대패션'

fs_1980['키워드'] = '1980년대패션'
fs_1990['키워드'] = '1990년대패션'
fs_2000['키워드'] = '2000년대패션'
fs_2010['키워드'] = '2010년대패션'
fs_2020['키워드'] = '2020년대패션'

fs_m['키워드'] = '남자패션'
fs_w['키워드'] = '여자패션'

fs_sp['키워드'] = '봄패션'
fs_su['키워드'] = '여름패션'
fs_au['키워드'] = '가을패션'
fs_wi['키워드'] = '겨울패션'

fs_usa['키워드'] = '미국패션'
fs_jap['키워드'] = '일본패션'
fs_fra['키워드'] = '프랑스패션'
fs_ita['키워드'] = '이탈리아패션'
fs_eng['키워드'] = '영국패션'

fs_spa['키워드'] = 'SPA'
fs_nike['키워드'] = '나이키'
fs_lux['키워드'] = '명품'
fs_work['키워드'] = '패션워크'

