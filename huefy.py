import functools
import math
import re

SUBST_MAP = {
    'xgg': -2,
    'xgs': -2,
    'xsg': -2,
    'xss': -2,
    'gssssg': -2,
    'gsssg': -3,
    'sgsg': -2,
    'gssg': -2,
    'sggg': -2,
    'sggs': -2,
}

X = 'йьъ'
G = 'аеёиоуыэюяaeiouy'
S = 'бвгджзклмнпрстфхцчшщbcdfghjklmnpqrstvwxz'

def check_s(smbl, kind):
    return kind.find(smbl) != -1

def check(value):
    if check_s(value, X):
        return 'x'
    if check_s(value, G):
        return 'g'
    if check_s(value, S):
        return 's'
    else:
        return ''

def encode(part):
    part_arr = list(part)
    result = map(check, part_arr)
    return ''.join(result)

def injectHypen(part, pos):
    part_arr = list(part)
    part_arr.insert(pos, '-')
    result = ''.join(part_arr)
    return result

def reducer(prev, current):
    encoded = encode(prev)
    if encoded.endswith(current[0]):
        return injectHypen(prev, current[1])
    else:
        return prev

def substitute(word):
    return functools.reduce(reducer, list(SUBST_MAP.items()), word)

def hypenate_reducer(prev, current):
    return substitute(prev) + current

def hypenate(word):
    result = functools.reduce(hypenate_reducer, list(word), '')
    return substitute(result)

def middle_index(syllabes):
    if len(syllabes) > 3:
        return math.ceil(len(syllabes) / 2) + 1
    else:
        return math.ceil(len(syllabes) / 2)

def rest_part(syllabes, word, second_word_part):
    if len(syllabes) == 1:
        pattern = re.compile(r'^[бвгджзклмнпрстфхцчшщbcdfghjklmnpqrstvwxz]*[аеёиоуыэюяaeiouy]?')
        return pattern.sub('', word)
    else:
        return second_word_part

def huefidation(removed):
    if removed.endswith('а'):
        return 'хуя'
    if removed.endswith('и'):
        return 'хуи'
    if removed.endswith('ы'):
        return 'хуи'
    if removed.endswith('о'):
        return 'хуё'
    else:
        return 'хуе'

def withCapitalization(part, orig):
    if orig[0].isupper():
        return part.capitalize()
    else:
        return part


def hueficaion(message_content):
    word_list = message_content.split()
    word = word_list[-1]
    if word.find('.') != -1:
        return word
    syllabes = hypenate(word.lower()).split('-')
    mid_index = middle_index(syllabes)
    slice_object = len(syllabes) - mid_index
    second_word_part = ''.join(syllabes[slice_object:])
    rest = rest_part(syllabes, word, second_word_part)

    removed = re.sub(rest, '', word)
    removed_updated = re.sub(r'[бвгджзклмнпрстфхцчшщbcdfghjklmnpqrstvwxz]+$', '', removed)
    huefied = huefidation(removed_updated) + rest

    pre_result = re.sub(r'^(ху[яе])х', r'\1', huefied)
    result = re.sub(r'^ху[ея]о', 'хуё', pre_result)

    # условие хуйня, но я устал и оно вроде работает, потом мб попралю
    if result != '' and result != 'хуе' and result != 'хуё' and result != 'хуи' and result != 'хуя' and result != word:
        return withCapitalization(result, word) + '!'
    else:
        return ''
