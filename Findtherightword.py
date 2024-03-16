#this works in about 1 out of 10 cases :P
import requests
from itertools import permutations
from lxml import html
import webbrowser
from collections import defaultdict

def create_optimized_dictionary(words):
    optimized_dict = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        optimized_dict[sorted_word].append(word)
    return optimized_dict

response = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')
word_set = set(response.text.splitlines())
optimized_dictionary = create_optimized_dictionary(word_set)

cookie = {'PHPSESSID':'id'}

page = requests.get('http://challenges.ringzer0team.com:10126/', cookies=cookie)
tree = html.fromstring(page.content)

scrambled_words_list = tree.xpath('/html/body/main/div/text()')[2].strip()

def unscramble_words(scrambled, optimized_dict):
    unscrambled = []
    for word in scrambled.split(','):
        sorted_word = ''.join(sorted(word))
        if optimized_dict.get(sorted_word):
            unscrambled.append(optimized_dict[sorted_word][0]) 
    return unscrambled

def process_words(scrambled_words):
    unscrambled = unscramble_words(scrambled_words, optimized_dictionary)
    response_string = ','.join(unscrambled)
    return response_string

if __name__ == "__main__":
    hashedMessage = process_words(scrambled_words_list)
    answerUrl = 'http://challenges.ringzer0team.com:10126/?r=' + hashedMessage
    webbrowser.open(answerUrl) 
