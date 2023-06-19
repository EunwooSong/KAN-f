var punctuations = ['.', ',', '!', '?', ';','\n']
var global_seed = 0.5


yamin_dic_cho_jung = {
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
    '꼬':'교'
    
}

yamin_dic_chosungless = {
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

yamin_dic_match = {
    'ㅇ':'O',
    'ㄱ':'7',
    'ㄹ':'2',
    '디':'ㅁ',
    '구':'ㅋ',
    '너':'ㅂ',
    '빅':'븨',
    '근':'ㄹ',
    '긘':'리'
}

function yamin(word){
    var new_word = ''

    for(var i=0;i<word.length;i++){
        var cjj = disassemble_hangul(word[i])

        cjj = cj_yamin(cjj)
        cjj = jj_yamin(cjj)
        cjj = match_yamin(cjj)

        new_word += assemble_hangul(cjj)
    }

    return new_word
}

function cj_yamin(hangul){
    var cvt_hangul = assemble_hangul([hangul[0], hangul[1], ''])
    if (cvt_hangul in yamin_dic_cho_jung){
        var yamin_hangul = disassemble_hangul(yamin_dic_cho_jung[cvt_hangul])
        return [yamin_hangul[0], yamin_hangul[1], hangul[2]]
    }
    else
        return hangul
}

function jj_yamin(hangul){
    var cvt_hangul = assemble_hangul(['ㅇ', hangul[1], hangul[2]])
    if (cvt_hangul in yamin_dic_chosungless){
        var yamin_hangul = disassemble_hangul(yamin_dic_chosungless[cvt_hangul])
        return [hangul[0], yamin_hangul[1], yamin_hangul[2]]
    }
    else
        return hangul
}

function match_yamin(hangul){
    if (assemble_hangul(hangul) in yamin_dic_match){
        return disassemble_hangul(yamin_dic_match[assemble_hangul(hangul)])
    }
    else
        return hangul
}


shiftkey_dic = [
    {
        'ㄱ':'ㄲ',
        'ㄷ':'ㄸ',
        'ㅈ':'ㅉ',
        'ㅂ':'ㅃ',
        'ㅅ':'ㅆ',
    },

    {
        'ㅗ':'ㅛ',
        'ㅓ':'ㅕ',
        'ㅏ':'ㅑ',
        'ㅜ':'ㅠ',
        'ㅐ':'ㅒ',
        'ㅔ':'ㅖ'
    },

    {
        'ㄱ':'ㄲ',
        'ㅂ':'ㅄ',
        'ㅅ':'ㅆ',
    }
]

function shiftkey(word){
    var new_word = ''
    for(var i=0;i<word.length;i++){
        var hangul = word[i]
        var cjj = disassemble_hangul(hangul)
        for(var j=0;j<3;j++){
            if (cjj[j] && cjj[j] in shiftkey_dic[j]){
                cjj[j] = shiftkey_dic[j][cjj[j]]
            }
        }

        new_word += assemble_hangul(cjj)
    }

    return new_word
}

function shift_test(str){
    var arr = str.split('')
    var txt = ''
    for(var i=0;i<arr.length;i++){
        if (is_hangul(arr[i])){
            var cjj = shiftkey(arr[i])
            txt += assemble_hangul(cjj)
        }
        else
            txt += arr[i]
    }

}
chosung = [ 'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ' ]
jungsung = [ 'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ' ]
jongsung = [ '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ' ]

function is_hangul(hangul){
    var c = hangul.charCodeAt();
    if( 0x1100<=c && c<=0x11FF ) return true;
    if( 0x3130<=c && c<=0x318F ) return true;
    if( 0xAC00<=c && c<=0xD7A3 ) return true;
    return false;
}

function is_word_hangul(word){
    if (word === undefined){
        console.log('This word is undefined')
        return false
    }
    for(var i=0;i<word.length;i++){
        if (is_hangul(word[i]) == false)
            return false
    }

    return true
}

function disassemble_hangul(hangul){
    if (chosung.includes(hangul))
        return [hangul, -1, 0]
    if (jungsung.includes(hangul))
        return [-1, hangul, 0]

    var charcode = hangul.charCodeAt() - 44032
    var cho = chosung[Math.floor(charcode / 28 / 21)]
    var jung = jungsung[Math.floor(charcode / 28 % 21)]
    var jong = jongsung[Math.floor(charcode % 28)]

    return [cho, jung, jong]
}

function assemble_hangul(arr){
    if (arr[0] === -1)  //only jungsung
        return arr[1]
    if (arr[1] === -1)  //only chosung
        return arr[0]

    return String.fromCharCode(0xAC00 + 21*28*chosung.indexOf(arr[0]) + 28*jungsung.indexOf(arr[1]) + jongsung.indexOf(arr[2]))
}


function cambridge(str){
    if (str.length < 4)
        return str

    var first = str[0]
    var last = str.slice(-1)
    var middles = str.slice(1, -1)

    return first + shuffle_string(middles) + last
}

function shuffle_string(str){
    var new_str = str.split('').sort(function(){return 0.5-Math.random()}).join('')
    if (new_str === str)
        return shuffle_string(str)
    else
        return new_str
}

function addPraise(paragraph){
    var praises = [
        '대단해요',
        '완벽해요',
        '최고에요',
        '대단합니다',
        '완벽합니다',
        '최고입니다',
        '놀랍습니다',
        '비교할 수 없습니다'
    ]

    var pre = praises[Math.floor(Math.random()*praises.length)]
    var post = praises[Math.floor(Math.random()*praises.length)]

    return pre + '. ' + paragraph + ' ' +post + '.'
}

function hangul_test(str){
    var arr = str.split('')
    var txt = ''
    for(var i=0;i<arr.length;i++){
        if (is_hangul(arr[i])){
            var dis = disassemble_hangul(arr[i])
            txt += assemble_hangul(dis)
        }
        else
            txt += arr[i]
    }
}


function addJunk(word){
    if (word.length < 2)
        return word
    
    var junk_list = [
        '여행', '체험', '뚜껑'
    ]


    var junk = junk_list[Math.floor(global_seed*junk_list.length)]
    var index = Math.floor(Math.random()*(word.length - 2)) + 1
    var new_word = word.slice(0,index) + junk + word.slice(index,word.length)
    return new_word
}

function addJongsung(word){
    var picked_js = jongsung[Math.floor(global_seed * jongsung.length - 1) + 1]
    var new_word = ''
    for(var i=0;i<word.length;i++){
        var cjj = disassemble_hangul(word[i])
        if (cjj[2] === '')
            new_word += assemble_hangul([cjj[0], cjj[1], picked_js])
        else
            new_word += word[i]
    }

    return new_word
}

function convert_text(input){
    global_seed = Math.random()
    var sentence_pos = [0]

    var is_punc = false
    for (var i=0;i<input.length;i++){
        if (i == input.length - 1){
            sentence_pos.push(i+1)
            break
        }

        if (punctuations.includes(input[i])){
            is_punc = true
            continue
        }

        if (is_punc === true && input[i] != ' '){
            sentence_pos.push(i)
            is_punc = false
            continue
        }
            
    }
    // console.log('sentence slice position')
    // console.log(sentence_pos)

    //slice string
    var sentences = []
    for (var i=0;i<sentence_pos.length - 1;i++){
        sentences.push(input.slice(sentence_pos[i],sentence_pos[i+1]))
    }
    // console.log('sentences sliced')
    // console.log(sentences)

    //import engines
    var engines = []
    engines.push(cambridge)
    engines.push(addJongsung)
    engines.push(shiftkey)
    engines.push(yamin)

    // console.log('main process engines checked list')
    // console.log(engines)
    if (engines.length === 0){
        console.log('Please check engines')
        return
    }

    //main processing
    var sequence = randomize(sentences.length, engines)
    // console.log('list of engines to be applied')
    // console.log(sequence)
    var new_sentence = ''
    for(var i=0;i<sentences.length;i++){
        new_sentence += convert_sentence(sentences[i], sequence[i])
    }
    // console.log('finished main processing')
    // console.log(new_sentence)

    //post processing
    // var p_engines = []
    // var p_engine_list = document.getElementsByClassName('post-engines')
    // for (var engine of p_engine_list){
    //     if (engine.checked)
    //         p_engines.push(window[engine.id])
    // }

    // for (var i=0;i<p_engines.length;i++){
    //     new_sentence = p_engines[i](new_sentence)
    // }
    
    //display to html
    return new_sentence
}

//number of sentence
function randomize(nos, engines){
    var sequence = []
    while(nos > 0){
        nos = nos - engines.length
        sequence = sequence.concat(engines.sort(function(){return 0.5-Math.random()}))
    }
    
    return sequence
}

function convert_sentence(sentence, engine){
    var strings = sentence.split(' ')
    var new_strings = []
    for (var i=0;i<strings.length;i++){
        new_strings.push(convert_word(strings[i], engine));
    }
    return new_strings.join(' ')
}

function convert_word(word, engine){    //save punctuations and only call hangul
    var new_word = []
    var index = 0

    for(var i=0;i<word.length;i++){
        if (is_hangul(word[i])){
            if (!new_word[index])
                new_word.push(word[i])
            else
                new_word[index] += word[i]
        }
        else{
            index++
            new_word.push(word[i])
            index++
        }
    }

    for(var i=0;i<new_word.length;i++){
        if (is_word_hangul(new_word[i])){
            new_word[i] = engine(new_word[i])
        }
    }

    return new_word.join('')
}

module.exports = {
    convert_text
};
/* note */
/*
숫자를 한글로 바꾸기?

*/