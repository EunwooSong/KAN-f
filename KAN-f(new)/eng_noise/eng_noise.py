import random

# 자음, 모음 리스트
consonant = 'bcdfghjklmnpqrstvwxyz'
vowel = 'aeiou'

def remove_middle_consonant(word):
    """
    주어진 단어에서 자음 3개가 연속되면 3개의 자음 중, 중간에 있는 자음이 탈락하는 함수입니다.

    Parameters:
    word (str): 변환할 단어

    Returns:
    str: 중간 자음이 탈락된 단어

    Examples:
    >>> remove_middle_consonant('friendly')
    'frienly'
    """

    modified_word = word[0]

    for i in range(1, len(word)-1):
        if word[i-1] in consonant and word[i] in consonant and word[i+1] in consonant:
            continue
        modified_word += word[i]

    modified_word += word[-1]

    return modified_word


# def merge_words(word1, word2):
#     """
#     두 단어를 놓고 볼 때, 앞 단어는 자음으로 끝이 나며, 뒤의 단어는 모음으로 시작하는 경우 연음되는 단어로 합칩니다.

#     Parameters:
#     word1 (str): 앞 단어
#     word2 (str): 뒤 단어

#     Returns:
#     list: 합쳐진 단어 리스트

#     Examples:
#     >>> merge_words('work', 'out')
#     'wor kout'
#     """
#     if word1[-1].lower() in consonant and word2[0].lower() in vowel:
#         merged_word = word1 + ' ' + word2
#     else:
#         merged_word = word1 + word2
#     return merged_word


def modify_vowel_consonant_vowel(word):
    """
    모음과 모음 사이에 낀 'd' 또는 't'를 'r'로 발음 변화시키는 함수입니다.

    Parameters:
    word (str): 변환할 단어

    Returns:
    str: 발음 변화된 단어

    Examples:
    >>> modify_vowel_consonant_vowel('video')
    'vireo'
    """
    
    modified_word = word[0]

    for i in range(1, len(word)-1):
        if word[i-1] in vowel and word[i] in consonant and word[i+1] in vowel:
            if word[i] in 'dt':
                modified_word += 'r'
                continue
        
        modified_word += word[i]

    modified_word += word[-1]

    return modified_word


def modify_vowel_consonant_end_le(word):
    """
    모음과 단어 끝의 'le' 사이에 낀 'd' 또는 't'를 'r'로 발음 변화시키는 함수입니다.

    Parameters:
    word (str): 변환할 단어

    Returns:
    str: 발음 변화된 단어

    Examples:
    >>> modify_vowel_consonant_end_le('little')
    'lirrle'
    """
    modified_word = ''
    for i in range(len(word)):
        if word[i].isalpha():
            if i < len(word) - 2 and word[i].lower() in vowel:
                if word[i+1].lower() in 'dt' and word[i+2:].lower() == 'le':
                    modified_word += 'r'
                    continue
            if i < len(word) - 1 and word[i].lower() in 'dt' and word[i+1:].lower() == 'le':
                modified_word += 'r'
            else:
                modified_word += word[i]
        else:
            modified_word += word[i]
    return modified_word


def modify_word(word):
    """
    모음과 모음 사이의 'd', 't'를 'r'로 발음 변화시키고, 'le' 사이의 'd', 't'를 'r'로 발음 변화시키는 함수입니다.

    Parameters:
    word (str): 변환할 단어

    Returns:
    str: 발음 변화된 단어

    Examples:
    >>> modify_word('get in')
    'ge rin'
    """
    modified_word = modify_vowel_consonant_vowel(word)
    modified_word = modify_vowel_consonant_end_le(modified_word)
    return modified_word

def remove_nt_sound(word):
    """
    모음과 모음 사이의 'nt'를 't'로 발음 변화시키는 함수입니다.

    Parameters:
    word (str): 변환할 단어

    Returns:
    str: 발음 변화된 단어

    Examples:
    >>> remove_nt_sound('internet')
    'inernet'
    """
    
    pass

def remove_duplicate_consonants(word):
    """
    자음이 두 개 겹치면, 하나만 발음하는 함수입니다.

    Parameters:
    word (str): 변환할 단어

    Returns:
    str: 발음 변화된 단어

    Examples:
    >>> remove_duplicate_consonants('summer')
    'sumer'
    """

    result = word[0]

    for i in range(1, len(word)):
        # 이전 문자와 현재 문자가 같은 자음인 경우, 스킵
        if word[i] == word[i-1] and word[i] in consonant:
            continue
        result += word[i]

    return result


def modify_gh_sound(word):
    """
    'gh'로 시작하는 단어에서 'h'를 묵음으로 변화시키는 함수입니다.

    Parameters:
    word (str): 변환할 단어

    Returns:
    str: 발음 변화된 단어

    Examples:
    >>> modify_gh_sound('ghost')
    'gost'
    """
    modified_word = ''
    i = 0

    if word[:2] == 'gh':
        modified_word = 'g' + word[2:]
    else:
        modified_word = word
    return modified_word

def modify_wh_sound(word):
    """
    'wh'의 경우 'h'가 묵음이 되는 함수입니다. 단, 예외 단어를 제외하고 묵음으로 처리합니다.

    Parameters:
    word (str): 변환할 단어

    Returns:
    str: 발음 변화된 단어

    Examples:
    >>> modify_wh_sound('where')
    'were'
    """
    exceptions = ['who', 'whole', 'whom', 'whose']
    if word.lower() in exceptions:
        return word
    
    modified_word = ''
    if word[:2] == 'wh':
        modified_word = 'w' + word[2:]
    else:
        modified_word = word
    return modified_word

def modify_kn_sound(word):
    """
    'wh'의 경우 'h'가 묵음이 되는 함수입니다. 단, 예외 단어를 제외하고 묵음으로 처리합니다.

    Parameters:
    word (str): 변환할 단어

    Returns:
    str: 발음 변화된 단어

    Examples:
    >>> modify_wh_sound('knife')
    'nife'
    """
    modified_word = ''
    if word[:2] == 'kn':
        modified_word = word[2:]
    else:
        modified_word = word
    return modified_word

def word_eng_noise(word: str, seed: int) -> str:
    """
    단어 단위로 노이즈를 적용합니다. (영어 전용)
    """
    if len(word) < 2:
        return word;
    # 모든 영어 노이즈 적용
    tmp_word = remove_middle_consonant(word);
    tmp_word = modify_vowel_consonant_vowel(tmp_word);
    tmp_word = modify_vowel_consonant_end_le(tmp_word);
    #tmp_word = modify_word(tmp_word);
    tmp_word = remove_nt_sound(tmp_word);
    tmp_word = remove_duplicate_consonants(tmp_word);
    tmp_word = modify_gh_sound(tmp_word);
    tmp_word = modify_wh_sound(tmp_word);
    tmp_word = modify_kn_sound(tmp_word);
    
    return tmp_word

def shuffle_eng(word, seed=1):
    """
    주어진 한글 단어의 중간 글자를 랜덤하게 섞어 반환합니다.

    Parameters:
    word (str): 섞을 영어 단어
    seed (int, optional): 난수 생성 시드값 (기본값: 1)

    Returns:
    str: 중간 글자가 랜덤하게 섞인 단어

    Examples:
    >>> shuffle_korean("Hello")
    '안하세녕요'
    >>> shuffle_korean("파이썬")
    '파이썬'
    """

    if len(word) < 4:
        return word
    mid = list(word[1:-1])
    random.shuffle(mid)

    return word[0] + ''.join(mid) + word[-1]

__all__ = ['word_eng_noise', 'shuffle_eng']