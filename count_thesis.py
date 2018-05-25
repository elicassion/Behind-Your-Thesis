# -*- coding=utf-8 -*-
import jieba
import os
import json
import codecs
from xpinyin import Pinyin
from collections import Counter
import pyecharts
import re




# print (type(thesis_content))

class Passage(object):
    def __init__(self):
        self.PASSAGE_FILE_NAME = ''
        self.COUNT_KEYS_FILE_NAME = ''
        self.COUNT_CHARACTERS_FILE_NAME = ''
        self.COUNT_WORDS_FILE_NAME = ''
        self.passage_content = None

    def load_passage(self, passage_file_name='my_thesis.txt'):
        # inputs filename
        self.PASSAGE_FILE_NAME = passage_file_name
        file_name_remove_suffix = ''.join(passage_file_name.split('.')[:-1])
        # outputs filename
        self.COUNT_KEYS_FILE_NAME = file_name_remove_suffix + 'count_keys.json'
        self.COUNT_CHARACTERS_FILE_NAME = file_name_remove_suffix + 'count_characters.json'
        self.COUNT_WORDS_FILE_NAME = file_name_remove_suffix + 'count_words_file.json'


        passage_file = codecs.open(self.PASSAGE_FILE_NAME, 'r', 'gbk')
        self.passage_content = passage_file.read().encode('utf8').decode('utf8')
        passage_file.close()

    def count_keys(self):
        P = Pinyin()
        pinyin_content = P.get_pinyin(self.passage_content, '')
        counter = Counter(pinyin_content.lower())
        print (counter)
        count_keys_file = codecs.open(self.COUNT_KEYS_FILE_NAME, 'w')
        json.dump(counter, count_keys_file, ensure_ascii=False, indent=2)
        count_keys_file.close()

    def count_characters(self):
        content = ''.join(re.findall(r'[\u4e00-\u9fa5]', self.passage_content))
        counter = Counter(content)
        print (counter)
        count_characters_file = codecs.open(self.COUNT_CHARACTERS_FILE_NAME, 'w')
        json.dump(counter, count_characters_file, ensure_ascii=False, indent=2)
        count_characters_file.close()

    def count_words(self):
        content = ''.join(re.findall(r'[\u4e00-\u9fa5]', self.passage_content))
        words = jieba.cut(content)
        words = [word for word in words if len(word)>2]
        counter = Counter(words)
        count_words_file = codecs.open(self.COUNT_WORDS_FILE_NAME, 'w')
        json.dump(counter, count_words_file, ensure_ascii=False, indent=2)
        print(counter)
        count_words_file.close()

    def map_count_to_keyboard(self):
        try:
            key_counter_file = codecs.open(self.COUNT_KEYS_FILE_NAME, 'w')
            key_counter = json.load(key_counter_file)
        except Exception as e:
            self.count_keys()
            key_counter_file = codecs.open(self.COUNT_KEYS_FILE_NAME, 'w')
            key_counter = json.load(key_counter_file)

        # for k, v in key_counter.items():
        #




thesis = Passage()
thesis.load_passage("my_thesis.txt")
# thesis.count_keys()
# thesis.count_characters()
# thesis.count_words()