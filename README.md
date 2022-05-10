# lyric-translator

korean to english
english to korean

가사를 구어체 형식으로 번역하도록 

번역된 가사를 직접올리는 사이트에서 영어와 한글 가사를 크롤링 해서 데이터를 만든뒤 

korean to english 는 kobert, distilgpt2 사용
english to korean 은 distilbert, kogpt2 사용
m2m100 모델도 사용

기존 데이터양이 부족하여 학습이 잘된 모델을 가지고 backtranslation으로 데이터 증강

기존에 있던 크롤링된 가사데이터중 2000개를 가져와 test

google translate와 bleu스코어 비교

                    영한      한영
google translation (0.1681   0.2459) 
bert-kogpt2        (0.0904         )
kobert-gpt2        (         0.2767)
m2m100             (0.3383   0.2772)

