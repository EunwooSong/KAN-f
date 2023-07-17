import kor_noise.hangul as h

shiftkey_dic = {
    "initial": {
        'ㄱ':'ㄲ',
        'ㄷ':'ㄸ',
        'ㅈ':'ㅉ',
        'ㅂ':'ㅃ',
        'ㅅ':'ㅆ',
    },

    "medial": {
        'ㅗ':'ㅛ',
        'ㅓ':'ㅕ',
        'ㅏ':'ㅑ',
        'ㅜ':'ㅠ',
        'ㅐ':'ㅒ',
        'ㅔ':'ㅖ'
    },

    "final": {
        'ㄱ':'ㄲ',
        'ㅂ':'ㅄ',
        'ㅅ':'ㅆ',
    }
}

def shiftkey(word):
    """
    주어진 한글 문자를 쉬프트키로 변환합니다.

    Parameters:
    word (str): 변경할 한글 단어

    Returns:
    str: 변경된 한글 단어

    Examples:
    >>> shiftkey("안녕하세요")
    '얀녕햐쎼요'
    """
    result = ""
    for char in word:
        initial, medial, final = h.hangul_decomposition(char)

        if initial in shiftkey_dic["initial"]:
            initial = shiftkey_dic["initial"][initial]
        if medial in shiftkey_dic["medial"]:
            medial = shiftkey_dic["medial"][medial]
        if final in shiftkey_dic["final"]:
            final = shiftkey_dic["final"][final]
        result += h.hangul_composition(initial, medial, final)
        
    return result