# Util, 한글 음절 분해(초성, 중성, 종성) 또는 음절 합치기
# 초성 리스트
initial_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 중성 리스트
medial_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

# 종성 리스트
final_list = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def is_hangul(char):
    """
    주어진 음절이 한글로 이루어진 문자인지 확인합니다.

    Parameters:
    char (str): 확인할 음절

    Returns:
    bool: 한글로 이루어진 문자일 경우 True, 그렇지 않을 경우 False

    Examples:
    >>> is_hangul("안")
    True
    >>> is_hangul("H")
    False
    """
    if len(char) > 1:
        print("음절만 검사합니다. 2개 이상의 문자로 이루어진 경우, is_word_hangul()을 사용해 주세요.")
    return True if '가' <= char <= '힣' else False

def is_word_hangul(word):
    """
    주어진 단어가 한글로 이루어진 문자인지 여부를 확인합니다.

    Parameters:
    word (string): 확인할 단어

    Returns:
    bool: 한글로 이루어진 문자일 경우 True, 그렇지 않을 경우 False

    Examples:
    >>> is_word_hangul("안녕하세요")
    True
    >>> is_word_hangul("Hello")
    False
    """
    for char in word:
        if not is_hangul(char):
            return False
    
    return True

def hangul_decomposition(char:str) -> tuple:
    """
    주어진 음절을 초성, 중성, 종성로 분해합니다.

    Parameters:
    char (str): 음절

    Returns:
    tuple: 초성, 중성, 종성이 합쳐진 음절 문자

    Examples:
    >>> hangul_decomposition('안')
    ('ㅇ', 'ㅏ', 'ㄴ')
    >>> hangul_decomposition('ㅇ')
    ('ㅇ', -1, -1)
    >>> hangul_decomposition('ㅏ')
    (-1, ㅏ, -1)
    """
    if char in initial_list:
        return char, -1, -1
    if char in medial_list:
        return -1, char, -1

    # 입력된 음절의 유니코드 값
    unicode_value = ord(char) - 44032
    
    # 초성 인덱스 계산
    initial_index = unicode_value // 588
    
    # 중성 인덱스 계산
    medial_index = (unicode_value - (588 * initial_index)) // 28
    
    # 종성 인덱스 계산
    final_index = unicode_value % 28

    # 초성, 중성, 종성 반환
    initial = initial_list[initial_index]
    medial = medial_list[medial_index]
    final = final_list[final_index]

    return initial, medial, final

def hangul_composition(initial, medial, final) -> str:
    """
    주어진 초성, 중성, 종성을 합쳐서 한 음절로 반환합니다.

    Parameters:
    initial (str): 초성 문자
    medial (str): 중성 문자
    final (str): 종성 문자

    Returns:
    str: 초성, 중성, 종성이 합쳐진 음절 문자

    Examples:
    >>> combine_to_syllable('ㅇ', 'ㅏ', 'ㄴ')
    '안'
    """
    if medial == -1:
        return initial
    if initial == -1:
        return medial
    
    # 초성, 중성, 종성을 인덱스로 변환하기
    initial_index = initial_list.index(initial)
    medial_index = medial_list.index(medial)
    final_index = final_list.index(final)
    
    # 음절 유니코드 값 계산
    hangul = 44032 + (initial_index * 588) + (medial_index * 28) + final_index
    
    return chr(hangul)