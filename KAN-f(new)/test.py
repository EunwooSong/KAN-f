import random
from kan_f import *

random.seed(20221657)
a = convert_text('이것은 테스트를 하기 위한 문장으로, 우리는 주어진 텍스트에 랜덤한 노이즈를 적용합니다.', p=0.9, n=5)

for s in a:
    print(s)