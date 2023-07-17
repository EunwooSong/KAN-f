import random

def shuffle_korean(word, seed=1):
    """
    주어진 한글 단어의 중간 글자를 랜덤하게 섞어 반환합니다.

    Parameters:
    word (str): 섞을 한글 단어
    seed (int, optional): 난수 생성 시드값 (기본값: 1)

    Returns:
    str: 중간 글자가 랜덤하게 섞인 단어

    Examples:
    >>> shuffle_korean("안녕하세요")
    '안하세녕요'
    >>> shuffle_korean("파이썬")
    '파이썬'
    """

    if len(word) < 4:
        return word
    random.seed(seed)
    mid = list(word[1:-1])
    random.shuffle(mid)

    return word[0] + ''.join(mid) + word[-1]