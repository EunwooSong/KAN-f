import kor_noise.hangul as h
import random

def add_final(word, seed:int=1):
    """
    주어진 단어에 랜덤한 종성을 추가합니다.

    Parameters:
    word (str): 종성을 추가할 단어
    seed (int, optional): 난수 생성 시드값 (기본값: 1)

    Returns:
    str: 종성이 추가된 단어

    Examples:
    >>> 안녕핝섽욙("안녕하세요")
    안녕핝섽욙
    """
    # 랜덤한 종성 선택
    randomFinal = random.choice(h.final_list[1:])
    convWord = ''

    for char in word: 
        initial, medial, final = h.hangul_decomposition(char)

        if final == '':
            convWord += h.hangul_composition(initial, medial, randomFinal)
        else:
            convWord += char
    return convWord