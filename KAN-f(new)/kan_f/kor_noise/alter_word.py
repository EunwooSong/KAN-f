from . import hangul as h
from random import sample

alter_dic_i_m = {
    '대': ['머'],
    '머': ['대'],
    '귀': ['커'],
    '커': ['귀'],
    '파': ['과', '따'],
    '과': ['파', '따'],
    '따': ['파', '과'],
    '피': ['끠'],
    '끠': ['피'],
    '비': ['네'],
    '네': ['비'],
    '띠': ['대', '며'],
    '며': ['댸', '띠'],
    '댸': ['며', '띠'],
    '거': ['지'],
    '지': ['거'],
    '겨': ['저'],
    '저': ['겨'],
    '교': ['꼬'],
    '꼬': ['교'],
    '고': ['끄'],
    '끄': ['고'],
    '삐': ['볘'],
    '볘': ['삐'],
    '포': ['쪼'],
    '쪼': ['포'],
    '되': ['티', '더'],
    '더': ['되', '티'],
    '티': ['되', '더'],
    '삐': ['볘'],
    '볘': ['삐'],


}

alter_dic_m_f = {
    '유':['윾'],
    '우':['윽'],
    '웃':['읏'],
    '을':['울', '올'],
    '왕':['앟'],
    '왱':['앻'],
    '욍':['잏'],
    '왓':['앛'],
    '왯':['앷'],
    '욋':['잋'],
    '읜':['임'],
    '임': ['읜'],
    '여':['억'],
    '읟':['일'],
    '외':['인'],
    '입':['왼'],
    '위':['읶'],
}

alter_dic_match = {
    'ㅇ':['O', '0'],
    'ㄱ':['7'],
    'ㅜ':['ㄱ'],
    'ㅠ':['ㄲ'],
    'ㅃ':['뱨'],
    'ㅂ':['너'],
    'ㄹ':['2', '근'],
    '디':['ㅁ'],
    '다':['ㅁ-', 'ㄷr', '다'],
    '나':['4'],
    '도':['ㅌ'],
    '구':['ㅋ'],
    '너':['ㅂ'],
    '빅':['븨'],
    '근':['ㄹ', '2'],
    '긘':['리'],
    '꺼':['77ㅓ'],
    '넣': ['봉'],
    '봉': ['넣'],
    '구': ['ㅋ'],
    '김': ['긘'],
    '긘': ['김'],
    '국': ['쿠'],
    '든': ['ㅌ'],
    '보': ['넌'],
    '러': ['귄'],
    '이': ['01', 'ol', 'O1', 'ㅇl', 'ㅇi'],
    '응': ['%', 'ㅎ']

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
        return h.hangul_decomposition(sample(alter_dic_i_m[tmp], 1)[0])[:2]
    return initial, medial

def alter_char_m_f(medial, final):
    tmp = h.hangul_composition('ㅇ', medial, final)
    if tmp in alter_dic_m_f:
        return h.hangul_decomposition(sample(alter_dic_m_f[tmp], 1)[0])[1:]
    return medial, final

def alter_char_match(char):
    if char in alter_dic_match:
        return sample(alter_dic_match[char], 1)[0]
    return char
