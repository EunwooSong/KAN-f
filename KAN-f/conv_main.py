__all__ = ['conv_main']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['shuffle_string', 'addPraise', 'shift_test', 'addJunk', 'hangul_test', 'match_yamin', 'disassemble_hangul', 'global_seed', 'assemble_hangul', 'yamin', 'is_hangul', 'convert_sentence', 'punctuations', 'addJongsung', 'randomize', 'shiftkey', 'cambridge', 'cj_yamin', 'convert_word', 'jj_yamin', 'convert_text', 'is_word_hangul'])
@Js
def PyJsHoisted_yamin_(word, this, arguments, var=var):
    var = Scope({'word':word, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'word', 'new_word', 'cjj'])
    var.put('new_word', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('word').get('length')):
        var.put('cjj', var.get('disassemble_hangul')(var.get('word').get(var.get('i'))))
        var.put('cjj', var.get('cj_yamin')(var.get('cjj')))
        var.put('cjj', var.get('jj_yamin')(var.get('cjj')))
        var.put('cjj', var.get('match_yamin')(var.get('cjj')))
        var.put('new_word', var.get('assemble_hangul')(var.get('cjj')), '+')
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('new_word')
PyJsHoisted_yamin_.func_name = 'yamin'
var.put('yamin', PyJsHoisted_yamin_)
@Js
def PyJsHoisted_cj_yamin_(hangul, this, arguments, var=var):
    var = Scope({'hangul':hangul, 'this':this, 'arguments':arguments}, var)
    var.registers(['cvt_hangul', 'yamin_hangul', 'hangul'])
    var.put('cvt_hangul', var.get('assemble_hangul')(Js([var.get('hangul').get('0'), var.get('hangul').get('1'), Js('')])))
    if var.get('yamin_dic_cho_jung').contains(var.get('cvt_hangul')):
        var.put('yamin_hangul', var.get('disassemble_hangul')(var.get('yamin_dic_cho_jung').get(var.get('cvt_hangul'))))
        return Js([var.get('yamin_hangul').get('0'), var.get('yamin_hangul').get('1'), var.get('hangul').get('2')])
    else:
        return var.get('hangul')
PyJsHoisted_cj_yamin_.func_name = 'cj_yamin'
var.put('cj_yamin', PyJsHoisted_cj_yamin_)
@Js
def PyJsHoisted_jj_yamin_(hangul, this, arguments, var=var):
    var = Scope({'hangul':hangul, 'this':this, 'arguments':arguments}, var)
    var.registers(['cvt_hangul', 'yamin_hangul', 'hangul'])
    var.put('cvt_hangul', var.get('assemble_hangul')(Js([Js('ㅇ'), var.get('hangul').get('1'), var.get('hangul').get('2')])))
    if var.get('yamin_dic_chosungless').contains(var.get('cvt_hangul')):
        var.put('yamin_hangul', var.get('disassemble_hangul')(var.get('yamin_dic_chosungless').get(var.get('cvt_hangul'))))
        return Js([var.get('hangul').get('0'), var.get('yamin_hangul').get('1'), var.get('yamin_hangul').get('2')])
    else:
        return var.get('hangul')
PyJsHoisted_jj_yamin_.func_name = 'jj_yamin'
var.put('jj_yamin', PyJsHoisted_jj_yamin_)
@Js
def PyJsHoisted_match_yamin_(hangul, this, arguments, var=var):
    var = Scope({'hangul':hangul, 'this':this, 'arguments':arguments}, var)
    var.registers(['hangul'])
    if var.get('yamin_dic_match').contains(var.get('assemble_hangul')(var.get('hangul'))):
        return var.get('disassemble_hangul')(var.get('yamin_dic_match').get(var.get('assemble_hangul')(var.get('hangul'))))
    else:
        return var.get('hangul')
PyJsHoisted_match_yamin_.func_name = 'match_yamin'
var.put('match_yamin', PyJsHoisted_match_yamin_)
@Js
def PyJsHoisted_shiftkey_(word, this, arguments, var=var):
    var = Scope({'word':word, 'this':this, 'arguments':arguments}, var)
    var.registers(['new_word', 'i', 'word', 'cjj', 'hangul', 'j'])
    var.put('new_word', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('word').get('length')):
        var.put('hangul', var.get('word').get(var.get('i')))
        var.put('cjj', var.get('disassemble_hangul')(var.get('hangul')))
        #for JS loop
        var.put('j', Js(0.0))
        while (var.get('j')<Js(3.0)):
            if (var.get('cjj').get(var.get('j')) and var.get('shiftkey_dic').get(var.get('j')).contains(var.get('cjj').get(var.get('j')))):
                var.get('cjj').put(var.get('j'), var.get('shiftkey_dic').get(var.get('j')).get(var.get('cjj').get(var.get('j'))))
            # update
            (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
        var.put('new_word', var.get('assemble_hangul')(var.get('cjj')), '+')
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('new_word')
PyJsHoisted_shiftkey_.func_name = 'shiftkey'
var.put('shiftkey', PyJsHoisted_shiftkey_)
@Js
def PyJsHoisted_shift_test_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['arr', 'i', 'txt', 'cjj', 'str'])
    var.put('arr', var.get('str').callprop('split', Js('')))
    var.put('txt', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('arr').get('length')):
        if var.get('is_hangul')(var.get('arr').get(var.get('i'))):
            var.put('cjj', var.get('shiftkey')(var.get('arr').get(var.get('i'))))
            var.put('txt', var.get('assemble_hangul')(var.get('cjj')), '+')
        else:
            var.put('txt', var.get('arr').get(var.get('i')), '+')
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
PyJsHoisted_shift_test_.func_name = 'shift_test'
var.put('shift_test', PyJsHoisted_shift_test_)
@Js
def PyJsHoisted_is_hangul_(hangul, this, arguments, var=var):
    var = Scope({'hangul':hangul, 'this':this, 'arguments':arguments}, var)
    var.registers(['hangul', 'c'])
    var.put('c', var.get('hangul').callprop('charCodeAt'))
    if ((Js(4352)<=var.get('c')) and (var.get('c')<=Js(4607))):
        return Js(True)
    if ((Js(12592)<=var.get('c')) and (var.get('c')<=Js(12687))):
        return Js(True)
    if ((Js(44032)<=var.get('c')) and (var.get('c')<=Js(55203))):
        return Js(True)
    return Js(False)
PyJsHoisted_is_hangul_.func_name = 'is_hangul'
var.put('is_hangul', PyJsHoisted_is_hangul_)
@Js
def PyJsHoisted_is_word_hangul_(word, this, arguments, var=var):
    var = Scope({'word':word, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'word'])
    if PyJsStrictEq(var.get('word'),var.get('undefined')):
        var.get('console').callprop('log', Js('This word is undefined'))
        return Js(False)
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('word').get('length')):
        if (var.get('is_hangul')(var.get('word').get(var.get('i')))==Js(False)):
            return Js(False)
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return Js(True)
PyJsHoisted_is_word_hangul_.func_name = 'is_word_hangul'
var.put('is_word_hangul', PyJsHoisted_is_word_hangul_)
@Js
def PyJsHoisted_disassemble_hangul_(hangul, this, arguments, var=var):
    var = Scope({'hangul':hangul, 'this':this, 'arguments':arguments}, var)
    var.registers(['cho', 'charcode', 'jong', 'jung', 'hangul'])
    if var.get('chosung').callprop('includes', var.get('hangul')):
        return Js([var.get('hangul'), (-Js(1.0)), Js(0.0)])
    if var.get('jungsung').callprop('includes', var.get('hangul')):
        return Js([(-Js(1.0)), var.get('hangul'), Js(0.0)])
    var.put('charcode', (var.get('hangul').callprop('charCodeAt')-Js(44032.0)))
    var.put('cho', var.get('chosung').get(var.get('Math').callprop('floor', ((var.get('charcode')/Js(28.0))/Js(21.0)))))
    var.put('jung', var.get('jungsung').get(var.get('Math').callprop('floor', ((var.get('charcode')/Js(28.0))%Js(21.0)))))
    var.put('jong', var.get('jongsung').get(var.get('Math').callprop('floor', (var.get('charcode')%Js(28.0)))))
    return Js([var.get('cho'), var.get('jung'), var.get('jong')])
PyJsHoisted_disassemble_hangul_.func_name = 'disassemble_hangul'
var.put('disassemble_hangul', PyJsHoisted_disassemble_hangul_)
@Js
def PyJsHoisted_assemble_hangul_(arr, this, arguments, var=var):
    var = Scope({'arr':arr, 'this':this, 'arguments':arguments}, var)
    var.registers(['arr'])
    if PyJsStrictEq(var.get('arr').get('0'),(-Js(1.0))):
        return var.get('arr').get('1')
    if PyJsStrictEq(var.get('arr').get('1'),(-Js(1.0))):
        return var.get('arr').get('0')
    return var.get('String').callprop('fromCharCode', (((Js(44032)+((Js(21.0)*Js(28.0))*var.get('chosung').callprop('indexOf', var.get('arr').get('0'))))+(Js(28.0)*var.get('jungsung').callprop('indexOf', var.get('arr').get('1'))))+var.get('jongsung').callprop('indexOf', var.get('arr').get('2'))))
PyJsHoisted_assemble_hangul_.func_name = 'assemble_hangul'
var.put('assemble_hangul', PyJsHoisted_assemble_hangul_)
@Js
def PyJsHoisted_cambridge_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['middles', 'first', 'str', 'last'])
    if (var.get('str').get('length')<Js(4.0)):
        return var.get('str')
    var.put('first', var.get('str').get('0'))
    var.put('last', var.get('str').callprop('slice', (-Js(1.0))))
    var.put('middles', var.get('str').callprop('slice', Js(1.0), (-Js(1.0))))
    return ((var.get('first')+var.get('shuffle_string')(var.get('middles')))+var.get('last'))
PyJsHoisted_cambridge_.func_name = 'cambridge'
var.put('cambridge', PyJsHoisted_cambridge_)
@Js
def PyJsHoisted_shuffle_string_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['str', 'new_str'])
    @Js
    def PyJs_anonymous_0_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return (Js(0.5)-var.get('Math').callprop('random'))
    PyJs_anonymous_0_._set_name('anonymous')
    var.put('new_str', var.get('str').callprop('split', Js('')).callprop('sort', PyJs_anonymous_0_).callprop('join', Js('')))
    if PyJsStrictEq(var.get('new_str'),var.get('str')):
        return var.get('shuffle_string')(var.get('str'))
    else:
        return var.get('new_str')
PyJsHoisted_shuffle_string_.func_name = 'shuffle_string'
var.put('shuffle_string', PyJsHoisted_shuffle_string_)
@Js
def PyJsHoisted_addPraise_(paragraph, this, arguments, var=var):
    var = Scope({'paragraph':paragraph, 'this':this, 'arguments':arguments}, var)
    var.registers(['paragraph', 'praises', 'post', 'pre'])
    var.put('praises', Js([Js('대단해요'), Js('완벽해요'), Js('최고에요'), Js('대단합니다'), Js('완벽합니다'), Js('최고입니다'), Js('놀랍습니다'), Js('비교할 수 없습니다')]))
    var.put('pre', var.get('praises').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('praises').get('length')))))
    var.put('post', var.get('praises').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('praises').get('length')))))
    return (((((var.get('pre')+Js('. '))+var.get('paragraph'))+Js(' '))+var.get('post'))+Js('.'))
PyJsHoisted_addPraise_.func_name = 'addPraise'
var.put('addPraise', PyJsHoisted_addPraise_)
@Js
def PyJsHoisted_hangul_test_(str, this, arguments, var=var):
    var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
    var.registers(['arr', 'i', 'txt', 'dis', 'str'])
    var.put('arr', var.get('str').callprop('split', Js('')))
    var.put('txt', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('arr').get('length')):
        if var.get('is_hangul')(var.get('arr').get(var.get('i'))):
            var.put('dis', var.get('disassemble_hangul')(var.get('arr').get(var.get('i'))))
            var.put('txt', var.get('assemble_hangul')(var.get('dis')), '+')
        else:
            var.put('txt', var.get('arr').get(var.get('i')), '+')
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
PyJsHoisted_hangul_test_.func_name = 'hangul_test'
var.put('hangul_test', PyJsHoisted_hangul_test_)
@Js
def PyJsHoisted_addJunk_(word, this, arguments, var=var):
    var = Scope({'word':word, 'this':this, 'arguments':arguments}, var)
    var.registers(['index', 'new_word', 'word', 'junk_list', 'junk'])
    if (var.get('word').get('length')<Js(2.0)):
        return var.get('word')
    var.put('junk_list', Js([Js('여행'), Js('체험'), Js('뚜껑')]))
    var.put('junk', var.get('junk_list').get(var.get('Math').callprop('floor', (var.get('global_seed')*var.get('junk_list').get('length')))))
    var.put('index', (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*(var.get('word').get('length')-Js(2.0))))+Js(1.0)))
    var.put('new_word', ((var.get('word').callprop('slice', Js(0.0), var.get('index'))+var.get('junk'))+var.get('word').callprop('slice', var.get('index'), var.get('word').get('length'))))
    return var.get('new_word')
PyJsHoisted_addJunk_.func_name = 'addJunk'
var.put('addJunk', PyJsHoisted_addJunk_)
@Js
def PyJsHoisted_addJongsung_(word, this, arguments, var=var):
    var = Scope({'word':word, 'this':this, 'arguments':arguments}, var)
    var.registers(['picked_js', 'new_word', 'i', 'word', 'cjj'])
    var.put('picked_js', var.get('jongsung').get((var.get('Math').callprop('floor', ((var.get('global_seed')*var.get('jongsung').get('length'))-Js(1.0)))+Js(1.0))))
    var.put('new_word', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('word').get('length')):
        var.put('cjj', var.get('disassemble_hangul')(var.get('word').get(var.get('i'))))
        if PyJsStrictEq(var.get('cjj').get('2'),Js('')):
            var.put('new_word', var.get('assemble_hangul')(Js([var.get('cjj').get('0'), var.get('cjj').get('1'), var.get('picked_js')])), '+')
        else:
            var.put('new_word', var.get('word').get(var.get('i')), '+')
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('new_word')
PyJsHoisted_addJongsung_.func_name = 'addJongsung'
var.put('addJongsung', PyJsHoisted_addJongsung_)
@Js
def PyJsHoisted_convert_text_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['sequence', 'engines', 'is_punc', 'i', 'input', 'sentences', 'new_sentence', 'sentence_pos'])
    var.put('global_seed', var.get('Math').callprop('random'))
    var.put('sentence_pos', Js([Js(0.0)]))
    var.put('is_punc', Js(False))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('input').get('length')):
        if (var.get('i')==(var.get('input').get('length')-Js(1.0))):
            var.get('sentence_pos').callprop('push', (var.get('i')+Js(1.0)))
            break
        if var.get('punctuations').callprop('includes', var.get('input').get(var.get('i'))):
            var.put('is_punc', Js(True))
            # continue update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            continue
        if (PyJsStrictEq(var.get('is_punc'),Js(True)) and (var.get('input').get(var.get('i'))!=Js(' '))):
            var.get('sentence_pos').callprop('push', var.get('i'))
            var.put('is_punc', Js(False))
            # continue update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            continue
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('sentences', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('sentence_pos').get('length')-Js(1.0))):
        var.get('sentences').callprop('push', var.get('input').callprop('slice', var.get('sentence_pos').get(var.get('i')), var.get('sentence_pos').get((var.get('i')+Js(1.0)))))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('engines', Js([]))
    var.get('engines').callprop('push', var.get('cambridge'))
    var.get('engines').callprop('push', var.get('addJongsung'))
    var.get('engines').callprop('push', var.get('shiftkey'))
    var.get('engines').callprop('push', var.get('yamin'))
    if PyJsStrictEq(var.get('engines').get('length'),Js(0.0)):
        var.get('console').callprop('log', Js('Please check engines'))
        return var.get('undefined')
    var.put('sequence', var.get('randomize')(var.get('sentences').get('length'), var.get('engines')))
    var.put('new_sentence', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('sentences').get('length')):
        var.put('new_sentence', var.get('convert_sentence')(var.get('sentences').get(var.get('i')), var.get('sequence').get(var.get('i'))), '+')
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('new_sentence')
PyJsHoisted_convert_text_.func_name = 'convert_text'
var.put('convert_text', PyJsHoisted_convert_text_)
@Js
def PyJsHoisted_randomize_(nos, engines, this, arguments, var=var):
    var = Scope({'nos':nos, 'engines':engines, 'this':this, 'arguments':arguments}, var)
    var.registers(['nos', 'sequence', 'engines'])
    var.put('sequence', Js([]))
    while (var.get('nos')>Js(0.0)):
        var.put('nos', (var.get('nos')-var.get('engines').get('length')))
        @Js
        def PyJs_anonymous_1_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return (Js(0.5)-var.get('Math').callprop('random'))
        PyJs_anonymous_1_._set_name('anonymous')
        var.put('sequence', var.get('sequence').callprop('concat', var.get('engines').callprop('sort', PyJs_anonymous_1_)))
    return var.get('sequence')
PyJsHoisted_randomize_.func_name = 'randomize'
var.put('randomize', PyJsHoisted_randomize_)
@Js
def PyJsHoisted_convert_sentence_(sentence, engine, this, arguments, var=var):
    var = Scope({'sentence':sentence, 'engine':engine, 'this':this, 'arguments':arguments}, var)
    var.registers(['sentence', 'engine', 'new_strings', 'strings', 'i'])
    var.put('strings', var.get('sentence').callprop('split', Js(' ')))
    var.put('new_strings', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('strings').get('length')):
        var.get('new_strings').callprop('push', var.get('convert_word')(var.get('strings').get(var.get('i')), var.get('engine')))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('new_strings').callprop('join', Js(' '))
PyJsHoisted_convert_sentence_.func_name = 'convert_sentence'
var.put('convert_sentence', PyJsHoisted_convert_sentence_)
@Js
def PyJsHoisted_convert_word_(word, engine, this, arguments, var=var):
    var = Scope({'word':word, 'engine':engine, 'this':this, 'arguments':arguments}, var)
    var.registers(['index', 'engine', 'new_word', 'i', 'word'])
    var.put('new_word', Js([]))
    var.put('index', Js(0.0))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('word').get('length')):
        if var.get('is_hangul')(var.get('word').get(var.get('i'))):
            if var.get('new_word').get(var.get('index')).neg():
                var.get('new_word').callprop('push', var.get('word').get(var.get('i')))
            else:
                var.get('new_word').put(var.get('index'), var.get('word').get(var.get('i')), '+')
        else:
            (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
            var.get('new_word').callprop('push', var.get('word').get(var.get('i')))
            (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('new_word').get('length')):
        if var.get('is_word_hangul')(var.get('new_word').get(var.get('i'))):
            var.get('new_word').put(var.get('i'), var.get('engine')(var.get('new_word').get(var.get('i'))))
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('new_word').callprop('join', Js(''))
PyJsHoisted_convert_word_.func_name = 'convert_word'
var.put('convert_word', PyJsHoisted_convert_word_)
var.put('punctuations', Js([Js('.'), Js(','), Js('!'), Js('?'), Js(';'), Js('\n')]))
var.put('global_seed', Js(0.5))
var.put('yamin_dic_cho_jung', Js({'대':Js('머'),'머':Js('대'),'귀':Js('커'),'커':Js('귀'),'파':Js('과'),'과':Js('파'),'피':Js('끠'),'끠':Js('피'),'비':Js('네'),'네':Js('비'),'며':Js('댸'),'댸':Js('며'),'거':Js('지'),'지':Js('거'),'겨':Js('저'),'저':Js('겨'),'교':Js('꼬'),'꼬':Js('교')}))
var.put('yamin_dic_chosungless', Js({'유':Js('윾'),'우':Js('윽'),'웃':Js('읏'),'을':Js('울'),'왕':Js('앟'),'왱':Js('앻'),'욍':Js('잏'),'왓':Js('앛'),'왯':Js('앷'),'욋':Js('잋')}))
var.put('yamin_dic_match', Js({'ㅇ':Js('O'),'ㄱ':Js('7'),'ㄹ':Js('2'),'디':Js('ㅁ'),'구':Js('ㅋ'),'너':Js('ㅂ'),'빅':Js('븨'),'근':Js('ㄹ'),'긘':Js('리')}))
pass
pass
pass
pass
var.put('shiftkey_dic', Js([Js({'ㄱ':Js('ㄲ'),'ㄷ':Js('ㄸ'),'ㅈ':Js('ㅉ'),'ㅂ':Js('ㅃ'),'ㅅ':Js('ㅆ')}), Js({'ㅗ':Js('ㅛ'),'ㅓ':Js('ㅕ'),'ㅏ':Js('ㅑ'),'ㅜ':Js('ㅠ'),'ㅐ':Js('ㅒ'),'ㅔ':Js('ㅖ')}), Js({'ㄱ':Js('ㄲ'),'ㅂ':Js('ㅄ'),'ㅅ':Js('ㅆ')})]))
pass
pass
var.put('chosung', Js([Js('ㄱ'), Js('ㄲ'), Js('ㄴ'), Js('ㄷ'), Js('ㄸ'), Js('ㄹ'), Js('ㅁ'), Js('ㅂ'), Js('ㅃ'), Js('ㅅ'), Js('ㅆ'), Js('ㅇ'), Js('ㅈ'), Js('ㅉ'), Js('ㅊ'), Js('ㅋ'), Js('ㅌ'), Js('ㅍ'), Js('ㅎ')]))
var.put('jungsung', Js([Js('ㅏ'), Js('ㅐ'), Js('ㅑ'), Js('ㅒ'), Js('ㅓ'), Js('ㅔ'), Js('ㅕ'), Js('ㅖ'), Js('ㅗ'), Js('ㅘ'), Js('ㅙ'), Js('ㅚ'), Js('ㅛ'), Js('ㅜ'), Js('ㅝ'), Js('ㅞ'), Js('ㅟ'), Js('ㅠ'), Js('ㅡ'), Js('ㅢ'), Js('ㅣ')]))
var.put('jongsung', Js([Js(''), Js('ㄱ'), Js('ㄲ'), Js('ㄳ'), Js('ㄴ'), Js('ㄵ'), Js('ㄶ'), Js('ㄷ'), Js('ㄹ'), Js('ㄺ'), Js('ㄻ'), Js('ㄼ'), Js('ㄽ'), Js('ㄾ'), Js('ㄿ'), Js('ㅀ'), Js('ㅁ'), Js('ㅂ'), Js('ㅄ'), Js('ㅅ'), Js('ㅆ'), Js('ㅇ'), Js('ㅈ'), Js('ㅊ'), Js('ㅋ'), Js('ㅌ'), Js('ㅍ'), Js('ㅎ')]))
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
conv_main = var.to_python()