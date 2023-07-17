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
        if word[i-1] in 'bcdfghjklmnpqrstvwxyz' and word[i] in 'bcdfghjklmnpqrstvwxyz' and word[i+1] in 'bcdfghjklmnpqrstvwxyz':
            continue
        modified_word += word[i]

    modified_word += word[-1]

    return modified_word


def merge_words(word1, word2):
    """
    두 단어를 놓고 볼 때, 앞 단어는 자음으로 끝이 나며, 뒤의 단어는 모음으로 시작하는 경우 연음되는 단어로 합칩니다.

    Parameters:
    word1 (str): 앞 단어
    word2 (str): 뒤 단어

    Returns:
    list: 합쳐진 단어 리스트

    Examples:
    >>> merge_words('work', 'out')
    'wor kout'
    """
    if word1[-1].lower() in 'bcdfghjklmnpqrstvwxyz' and word2[0].lower() in 'aeiou':
        merged_word = word1 + ' ' + word2
    else:
        merged_word = word1 + word2
    return merged_word


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
    modified_word = ''
    for i in range(len(word)):
        if word[i].isalpha():
            if i < len(word) - 2 and word[i].lower() in 'aeiou':
                if word[i+1].lower() in 'dt' and word[i+2].lower() in 'aeiou':
                    continue
            if i < len(word) - 1 and word[i].lower() in 'dt' and word[i+1].lower() in 'aeiou':
                modified_word += 'r'
            else:
                modified_word += word[i]
        else:
            modified_word += word[i]
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
            if i < len(word) - 2 and word[i].lower() in 'aeiou':
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
    modified_word = ''
    for i in range(len(word)):
        if word[i].isalpha():
            if i < len(word) - 1 and word[i].lower() in 'aeiou' and word[i+1].lower() == 'nt':
                continue
            modified_word += word[i]
        else:
            modified_word += word[i]
    return modified_word

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
        if word[i] == word[i-1] and word[i] in 'bcdfghjklmnpqrstvwxyz':
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
    while i < len(word):
        if word[i].isalpha():
            if i == 0 and word[:2].lower() == 'gh':
                i += 1
                continue
            elif i > 0 and word[i-1].isalpha() and word[i-1].lower() == 'g' and word[i].lower() == 'h':
                i += 1
                continue
        modified_word += word[i]
        i += 1
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
    if word.lower() not in exceptions:
        modified_word = ''
        i = 0
        while i < len(word):
            if word[i].isalpha():
                if i > 0 and word[i-1].isalpha() and word[i-1].lower() == 'w' and word[i].lower() == 'h':
                    i += 1
                    continue
            modified_word += word[i]
            i += 1
    else:
        modified_word = word
    return modified_word