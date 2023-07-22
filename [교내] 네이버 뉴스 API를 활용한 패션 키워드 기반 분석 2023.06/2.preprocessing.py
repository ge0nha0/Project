#!/usr/bin/env python
# coding: utf-8

# # 2. 텍스트 데이터 전처리
# ## 2.1 Cleaning
# ### 제목과 내용을 기준으로 중복 기사 제거

# In[ ]:


# 중복기사 제거
# 데이터 Concat 후 중복값(제목, 내용 기준으로) 제거 # 12,025 -> 10,526

df = pd.concat([fs_10,fs_20, fs_30, fs_40, fs_50, fs_1980, fs_1990, fs_2000, fs_2010, fs_2020,
           fs_m, fs_w, fs_sp, fs_su, fs_au, fs_wi, fs_usa, fs_jap, fs_fra, fs_ita, fs_eng,
           fs_spa, fs_nike, fs_lux, fs_work], ignore_index=True)


# In[ ]:


# 제목과 내용 기준으로 첫번째 겹친 것은 살려두고 나머지는 제거
df = df.drop_duplicates(['제목', '내용'], keep = 'first', ignore_index=True)


# In[ ]:


# 정규표현식을 통한 데이터 전처리
import re

# '\n사진이미지사진자료기자기사뉴스' 패턴을 포함하는 문자열을 공백으로 대체하여 제거
regex = r'[\n사진이미지사진자료기자기사뉴스]'
df['내용'] = df['내용'].apply(lambda x: re.sub(regex, '', x))

df['전처리 내용'] = df['내용'].copy()

 # '\w' (알파벳과 숫자), '\s' (공백)이 아닌 문자를 공백으로 대체하여 제거
regex = r'[^\w\s]' 

df['전처리 내용'] = df['내용'].apply(lambda x: re.sub(regex, '', str(x)))
# '\n', '\t', '\r'을 빈 문자열로 대체하여 제거
df['전처리 내용'] = df['전처리 내용'].str.replace('\n', '')
df['전처리 내용'] = df['전처리 내용'].str.replace('\t', '')
df['전처리 내용'] = df['전처리 내용'].str.replace('\r', '')

# 문자열 앞뒤의 공백을 제거
df['전처리 내용'] = df['전처리 내용'].str.strip()


# # Tokenization & Pos Tagging & Stopword Removal
# stopwords들을 정의하고 이를 제외해서 분석하겠습니다.

# In[ ]:


from konlpy.tag import Okt         
t = Okt()


# In[ ]:


# 토큰화
li1 = [] # 토큰화된 결과를 저장할 리스트
# df 데이터프레임의 각 행에 대해 반복
for _, row in tqdm(df.iterrows()):
    # 현재 행의 content 값을 df_text 변수에 할당
    df_text = row['전처리 내용']  
    # df_text를 한국어 형태소 분석기를 사용하여 토큰화한 결과를 ko 변수에 할당  
    ko = t.pos(df_text)
    li1.append(ko)


# In[ ]:


# 일곱번째 행 ->  Pos Tagging
print(li1[6])


# In[ ]:


# 단어 별 구체적으로 토큰화
li2 = [] # 단어별로 구체적으로 토큰화된 결과를 저장할 리스트
for li in li1: 
    li3 = [] # 단어별로 구체적으로 토큰화된 결과를 저장할 리스트
    for ele in li: 
        li3.append(ele[0]) # 토큰화된 결과의 첫 번째 요소(단어)를 리스트에 추가
    li2.append(li3)  # 단어별로 구체적으로 토큰화된 결과를 리스트에 추가


# In[ ]:


# 일곱번째 행 -> 구체적 토큰화 진행
print(li2[6])


# In[ ]:


#stopword Removal
with open('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/stopwords.txt', 'r', encoding='utf-8') as f:
    stopwords = f.readlines()
stopwords = [x.replace('\n','') for x in stopwords]
okt = Okt()

toks = li2 # 토큰화된 결과 리스트
li4 = [] # 불용어 제거된 결과를 저장할 리스트
for tok in toks:
    li5 = []  # 불용어가 아닌 토큰을 저장할 리스트
    for to in tok:
         if to not in stopwords: # 토큰이 불용어가 아닌 경우에만 처리
            li5.append(to)
    li4.append(li5) 


# In[ ]:


# 일곱번째 행 -> Stopword 제거
print(li4[6])


# In[ ]:


#dataframe 생성
df_li = []
for tok in li4:
    to = ' '.join(tok)
    df_li.append(to) 

df1 = pd.DataFrame(df_li).rename(columns = {0:'전처리 내용2'})
df2 = pd.concat([df,df1],axis=1)
df2


# In[ ]:


df2.to_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/df2.csv',index=False, encoding='utf-8-sig')


# In[ ]:


df2 = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Naver_뉴스_패션/data/df2.csv')


# In[ ]:


# 전처리 내용2에서 결측값 2개 발견
df2['전처리 내용2'].isna().sum()


# In[ ]:


# 전처리 내용2 결측치 제거
df2.dropna(inplace=True)


# In[ ]:


# 결측치 제거 결과 0
df2['전처리 내용2'].isna().sum()


# In[ ]:


df3 = df2.drop(['제목', '내용', '전처리 내용'], axis=1)


# # 키워드 열을 기준으로 다시 데이터프레임을 나누기
# 

# In[ ]:


fs_10 = df3[df3['키워드'] == '10대패션']
fs_20 = df3[df3['키워드'] == '20대패션']
fs_30 = df3[df3['키워드'] == '30대패션']
fs_40 = df3[df3['키워드'] == '40대패션']
fs_50 = df3[df3['키워드'] == '50대패션']

fs_1980 = df3[df3['키워드'] == '1980년대패션']
fs_1990 = df3[df3['키워드'] == '1990년대패션']
fs_2000 = df3[df3['키워드'] == '2000년대패션']
fs_2010 = df3[df3['키워드'] == '2010년대패션']
fs_20200 = df3[df3['키워드'] == '2020년대패션']

fs_m = df3[df3['키워드'] == '남자패션']
fs_w = df3[df3['키워드'] == '여자패션']

fs_sp = df3[df3['키워드'] == '봄패션']
fs_su = df3[df3['키워드'] == '여름패션']
fs_au = df3[df3['키워드'] == '가을패션']
fs_wi = df3[df3['키워드'] == '겨울패션']

fs_usa = df3[df3['키워드'] == '미국패션']
fs_jap = df3[df3['키워드'] == '일본패션']
fs_fra = df3[df3['키워드'] == '프랑스패션']
fs_ita = df3[df3['키워드'] == '이탈리아패션']
fs_eng = df3[df3['키워드'] == '영국패션']

fs_spa = df3[df3['키워드'] == 'SPA']
fs_nike = df3[df3['키워드'] == '나이키']
fs_lux = df3[df3['키워드'] == '명품']
fs_work = df3[df3['키워드'] == '패션워크']

