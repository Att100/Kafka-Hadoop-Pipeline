import math
import re

class TextParser:
    def __init__(self, stopwords_path: str):
        self.stopwords = []
        self.set_stop_words(stopwords_path)
    
    def set_stop_words(self, path: str) -> list:
        f = open(path, 'r')
        lines = f.readlines()
        f.close()
        self.stopwords = [item.strip("\n") for item in lines]

    def remove_stop_words(self, words: list) -> list:
        return list(set(words).difference(self.stopwords+['']))

    def remove_punctuation(self, content: str) -> str:
        if not content.isalnum():
            punctuation = r"~!@#$%^&*()_+`{}|\[\]\:\";\-\\\='<>?,./，。、《》？；：‘“{【】}|、！@#￥%……&*（）——+=-"
            content = re.sub(r'[{}]+'.format(punctuation), ' ', content)
            content = content.replace("  ", " ")
        return content.strip().lower()

    def split_to_words(self, content: str):
        if content == "":
            return []
        else:
            return content.split(" ")

    def parse(self, content: str) -> list:
        content = self.remove_punctuation(content)
        words = self.split_to_words(content)
        words = self.remove_stop_words(words)
        return words