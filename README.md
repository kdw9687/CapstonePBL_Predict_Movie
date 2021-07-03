# Project Title / Movie Box office prediction using Machine & Deep Learning

This project proceed at Capstone class at Hanyang university. Our team try to predict Movie Box office of Korea. We searched data which related with Box office.
And we use many Machine Learning Algorithm like Decision Tree, Random Forest, Navie-Bayes and ANN. 

## Getting Started 

First, we searched data. Data consisted of items which related to movie box office. We collected 2010s moive box office data. And we investigated various factors for each film like running time, number of theaters. After preprocessing these data, various machine learning techniques were applied.

### Prerequisites 

We use only colab.

### Installing / 설치
This is the way to download RAdam at colab. Other modules were already installed.

	#@title 
	!pip install -q keras-bert keras-rectified-adam
	!wget -q https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip
	!unzip -o uncased_L-12_H-768_A-12.zip
	!pip install -U keras-tuner
	!pip install -q -U tensorflow-addons


## Running the tests 

Input data : the factor which releated to movie box office.
	['주연 top50 출연 여부', '배급사', '수상내역', '국적', '전국 스크린수', '경쟁작', '가족', '공연',
       '공포(호러)', '기타', '다큐멘터리', '드라마', '멜로/로맨스', '뮤지컬', '미스터리', '범죄', '사극',
       '스릴러', '애니메이션', '액션', '어드벤처', '전쟁', '코미디', '판타지', 'SF', '러닝타임',
       '네티즌 평점', 'top영화감독 여부', '연작', '원작', '전체관람가', '12세관람가', '15세관람가',
       '19세관람가',
       '연휴기간 상영여부 (연휴 기간 상영 영화중 점유율 TOP2% (104개정도이고 최저 점유율 대략 17.7%))',
       '연휴기간 상영여부 (연휴 기간 상영 영화중 점유율 TOP5% (260개이고 최저 점유율 대략 7.6%))']

Output data : [ 영화 관객수 ] It was divided into 4 results according to the interval. [under 1M, 1M~3M, 3M~6M, over 6M]= [1,2,3,4]

![image](https://user-images.githubusercontent.com/78201690/124347537-33241900-dc20-11eb-868c-92528619985b.png)
![image](https://user-images.githubusercontent.com/78201690/124347552-3fa87180-dc20-11eb-86b4-701da5da0941.png)


## Built With / 누구랑 만들었나요?

Imjeongseob : machine learning modeling

## Contributiong / 기여

https://jeongmin-lee.tistory.com/85 
thank you for your code.

## Acknowledgments / 감사의 말

Thank your for professor Seo jae hong.
