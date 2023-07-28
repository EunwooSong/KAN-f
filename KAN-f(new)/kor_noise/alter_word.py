from . import hangul as h

alter_dic_i_m = {
    '대':'머',
    '머':'대',
    '귀':'커',
    '커':'귀',
    '파':'과',
    '과':'파',
    '피':'끠',
    '끠':'피',
    '비':'네',
    '네':'비',
    '며':'댸',
    '댸':'며',
    '거':'지',
    '지':'거',
    '겨':'저',
    '저':'겨',
    '교':'꼬',
    '꼬':'교',
    '고':'끄',
    '끄':'고',
    '삐':'볘',
    '볘':'삐',
    '포':'쪼',
    '쪼':'포'
}

alter_dic_m_f = {
    '유':'윾',
    '우':'윽',
    '웃':'읏',
    '을':'울',
    '왕':'앟',
    '왱':'앻',
    '욍':'잏',
    '왓':'앛',
    '왯':'앷',
    '욋':'잋',

}

alter_dic_match = {
    'ㅇ':'O',
    'ㄱ':'7',
    'ㄹ':'2',
    '디':'ㅁ',
    '구':'ㅋ',
    '너':'ㅂ',
    '빅':'븨',
    '근':'ㄹ',
    '긘':'리',
    '꺼':'77ㅓ',
}

def alter_word(word, *args):
    """
    주어진 한글 단어의 문자를 비슷한 문자로 변경하여 반환합니다.

    Parameters:
    word (str): 변경할 한글 단어

    Returns:
    str: 변경된 한글 단어

    Examples:
    >>> alter_word("너구리")
    'ㅂ극리'
    """
    result = ""

    for char in word:
        initial, medial, final = h.hangul_decomposition(char)
        initial, medial = alter_char_i_m(initial, medial)
        medial, final = alter_char_m_f(medial, final)

        tmp = h.hangul_composition(initial, medial, final)
        tmp = alter_char_match(tmp)
        result += tmp
    return result

def alter_char_i_m(initial, medial):
    tmp = h.hangul_composition(initial, medial, '')
    if tmp in alter_dic_i_m:
        return h.hangul_decomposition(alter_dic_i_m[tmp])[:2]
    return initial, medial

def alter_char_m_f(medial, final):
    tmp = h.hangul_composition('ㅇ', medial, final)
    if tmp in alter_dic_m_f:
        return h.hangul_decomposition(alter_dic_m_f[tmp])[1:]
    return medial, final

def alter_char_match(char):
    if char in alter_dic_match:
        return alter_dic_match[char]
    return char