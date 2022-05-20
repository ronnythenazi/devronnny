import re

def get_taged_users(s, prefix='@'):
    return get_words(prefix, s)

def get_words(start_with="", string=""):
    #pattern = r"(@\w+)"
    pattern = r"(" + start_with + "\w+)"
    lst = re.findall( pattern, string, re.M|re.I)
    return lst


def is_str_start_with_substr(s, sub_s):
    return s.startswith(sub_s)


def getNotStartWith_pattern(not_start_with):
    #^(?!<a class="tagged-user">.*$)@ronny
    return '(?<!' + not_start_with + ')'

def getWordNotStartWithWord_pattern(not_start_with, start_with='\w+$'):
    not_start_with_pattern = getNotStartWith_pattern(not_start_with)
    pattern = not_start_with_pattern + start_with
    return pattern

def replaceWordNotStartWithWord(not_start_with, start_with, replace_with, s):
    pattern = getWordNotStartWithWord_pattern(not_start_with, start_with)
    new_s = re.sub(pattern, replace_with, s)
    return new_s
