__all__ = ['conv_main']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['convert_text', 'convert_word', 'convert_sentence', 'randomize'])
@Js
def PyJsHoisted_randomize_(nos, engines, this, arguments, var=var):
    var = Scope({'nos':nos, 'engines':engines, 'this':this, 'arguments':arguments}, var)
    var.registers(['sequence', 'engines', 'nos'])
    var.put('sequence', Js([]))
    while (var.get('nos')>Js(0.0)):
        var.put('nos', (var.get('nos')-var.get('engines').get('length')))
        @Js
        def PyJs_anonymous_0_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return (Js(0.5)-var.get('Math').callprop('random'))
        PyJs_anonymous_0_._set_name('anonymous')
        var.put('sequence', var.get('sequence').callprop('concat', var.get('engines').callprop('sort', PyJs_anonymous_0_)))
    return var.get('sequence')
PyJsHoisted_randomize_.func_name = 'randomize'
var.put('randomize', PyJsHoisted_randomize_)
@Js
def PyJsHoisted_convert_sentence_(sentence, engine, this, arguments, var=var):
    var = Scope({'sentence':sentence, 'engine':engine, 'this':this, 'arguments':arguments}, var)
    var.registers(['strings', 'sentence', 'engine', 'i', 'new_strings'])
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
    var.registers(['index', 'engine', 'new_word', 'word', 'i'])
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
@Js
def PyJsHoisted_convert_text_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['engines', 'sentence_pos', 'punctuations', 'global_seed', 'input', 'i', 'sequence', 'is_punc', 'sentences'])
    var.put('global_seed', var.get('Math').callprop('random'))
    var.put('sentence_pos', Js([Js(0.0)]))
    var.put('punctuations', Js([Js('.'), Js(','), Js('!'), Js('?'), Js(';'), Js('\n')]))
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
    var.put('engines', Js([Js('cambridge'), Js('addJongsung'), Js('shiftkey'), Js('yamin')]))
    if PyJsStrictEq(var.get('engines').get('length'),Js(0.0)):
        var.get('console').callprop('log', Js('Please check engines'))
        return var.get('undefined')
    var.put('sequence', var.get('randomize')(var.get('sentences').get('length'), var.get('engines')))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('sentences').get('length')):
        var.put('new_sentence', var.get('convert_sentence')(var.get('sentences').get(var.get('i')), var.get('sequence').get(var.get('i'))), '+')
        # update
        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('new_sentence')
PyJsHoisted_convert_text_.func_name = 'convert_text'
var.put('convert_text', PyJsHoisted_convert_text_)
pass
pass
pass
pass
pass


# Add lib to the module scope
conv_main = var.to_python()