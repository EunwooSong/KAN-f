import re
import random
from .kor_noise import *

# 변환 노이즈 리스트
noise_list = [add_final, alter_word, shiftkey, shuffle_korean]
test_document = '이것은 KAN-f 노이즈 테스트를 위한 문장입니다. 이런이런... 떡 하나 주면 안 잡아 먹지!'

def convert_text(text:str, p=1.0, n=1) -> str:
    """
    주어진 텍스트에 랜덤한 노이즈를 적용합니다.

    Parameters:
    text (str): 변환할 텍스트
    p (float): 한 문장의 변형률(0~1.0)

    Returns:
    str: 변환된 텍스트

    Examples:
    >>> split_sentences("안녕하세요. 반갑습니다!", p=1.0, n=2)
    ['안세녕하요. 반갑습니다!', '안녕하세요. 반깝씁니따!']
    """
    p = min(max(p, 0.0), 1.0)
    sentences = split_sentences(text);
    new_text = []
    for i in range(n):
        new_text.append('')

        for sentence in sentences:
            new_text[i] += convert_sentence(sentence, p)
    return new_text

def split_sentences(text, punctuations=['.', '!', '?', ';','\n', "'"]) -> dict:
    """
    주어진 텍스트를 문장으로 구분하여 반환합니다.
    문장과 해당 구두점을 dict 형식으로 반환합니다.

    Parameters:
    text (str): 구분할 텍스트
    punctuations (str, optional): 문장 구분 기준이 되는 구두점 문자열
    (기본값: ['.', ',', '!', '?', ';','\n'])

    Returns:
    list: 구분된 문장과 해당 구두점을 담은 dict들의 리스트

    Examples:
    >>> split_sentences("안녕하세요. 반갑습니다!", ".!")
    [{'sentence': '안녕하세요', 'punc': '.'}, {'sentence': ' 반갑습니다', 'punc': '!'}]
    """
    # 구두점을 기준으로 슬라이싱할 pos 구하기
    sentences = []
    punc_index = [0]
    is_punc = False
    for i, char in enumerate(text):
        if i == len(text) - 1:
            punc_index.append(i+1)
            break

        if char in punctuations:
            is_punc = True
            continue

        if is_punc and (char != ' '):
            punc_index.append(i)
            is_punc = False
            continue
    
    # 슬라이싱 진행
    punc_group = zip(punc_index[:-1:], punc_index[1::])
    for s, e in punc_group:
        sentences.append(text[s:e])
    
    # 변환할 문장과 구두점으로 분리
    result = []
    
    for sentence in sentences:
        for i, char in enumerate(sentence):
            if char in punctuations:
                result.append({"sentence": sentence[:i], 'punc': sentence[i:]})
                break
            elif i+1 == len(sentence):
                result.append({"sentence": sentence, 'punc': ''})
                break

    return result

def convert_sentence(sentence: dict, p:float) -> str:
    """
    문장 단위로 노이즈를 적용합니다. (한글 전용)
    """
    words = str.split(sentence['sentence'], ' ')
    noise = random.choice(noise_list)
    result = []
    sample_cnt = int(len(words) * p)
    noise_index = random.sample(range(len(words)), sample_cnt)

    for i, word in enumerate(words):
        if i in noise_index:
            result.append(convert_word(word, noise))
        else:
            result.append(word)
    return ' '.join(result) + sentence['punc']


def convert_word(word: str, noise) -> str:
    conv_word = []
    index = 0
    
    for char in word:
        if hangul.is_hangul(char):
            if index == len(conv_word):
                conv_word.append(char)
            else:
                conv_word[index] += char
        else:
            conv_word.append(char)
    
    result = []
    for seq in conv_word:
        if hangul.is_word_hangul(seq):
            result.append(noise(seq))
        else:
            result.append(seq)
    
    return ''.join(result)
