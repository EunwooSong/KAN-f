import re
import random
import kor_noise.hangul as hangul
from kor_noise.add_final import add_final
from kor_noise.alter_word import alter_word
from kor_noise.shiftkey import shiftkey
from kor_noise.shuffle_korean import shuffle_korean

# 글로벌 시드값
global_seed = 1

# 변환 노이즈 리스트
noise_list = [add_final, alter_word, shiftkey, shuffle_korean]

test_document = '이것은 KAN-f 노이즈 테스트를 위한 문장입니다. 이런이런... 떡 하나 주면 안 잡아 먹지!'

def convert_text(text:str) -> str:
    isPunc = False


def split_sentences(text, punctuations=['.', ',', '!', '?', ';','\n']):
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
    pattern = "([" + re.escape(punctuations) + "]+)(?!\\w)"
    sentences = re.split(pattern, text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    result = []
    for i in range(0, len(sentences), 2):
        sentence = sentences[i]
        punctuation = sentences[i + 1]
        result.append({'sentence': sentence, 'punc': punctuation})
    return result

def convert_sentence(sentence: dict, seed: int) -> str:
    words = str.split(sentence['sentence'], ' ')
    random.seed = seed
    noise = random.choice(noise_list)
    result = []
    for word in words:
        result += convert_word(word, seed, noise)
    return ' '.join(result) + sentence['punc']

def convert_word(word: str, seed: int, noise) -> str:
    conv_word = []
    index = 0
    
    for char in word:
        if hangul.is_hangul(char):
            if index == len(conv_word):
                conv_word.append(char)
            else:
                conv_word[index] += char
        else:
            index += 1
            conv_word.append(char)
            index += 1
    
    result = []
    for seq in conv_word:
        if hangul.is_word_hangul(seq):
            result.append(noise(seq, seed))
        else:
            result.append(seq)
    
    return ''.join(result)

