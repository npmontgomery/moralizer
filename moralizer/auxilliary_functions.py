import spacy
from collections import Counter
import json
#need to install
#python -m spacy download en_core_web_sm


def read_json(filename):
    with open(filename, 'r',encoding='utf-8') as file:
        return json.load(file)

def word_frequency_dict(input_text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_text)
    words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
    word_freq = Counter(words)
    c = dict(word_freq)
    return c

def count_keywords(source_dictionary, output_format='pydict'):
    output_dict = {'care':{'vice':{}, 'virtue':{}}, 'fairness':{'vice':{}, 'virtue':{}}, 'loyalty':{'vice':{}, 'virtue':{}}, 'authority':{'vice':{}, 'virtue':{}}, 'sanctity':{'vice':{}, 'virtue':{}}}
    lex = read_json('moral_foundations.json')
    for item in lex.keys():
        good = [(item, source_dictionary[item]) for item in lex[item]['virtue'] if item in source_dictionary]
        bad = [(item, source_dictionary[item]) for item in lex[item]['vice'] if item in source_dictionary] 
        good_changed = {k:v for (k,v) in good}
        bad_changed = {k:v for (k,v) in bad}
        output_dict[item]['virtue'] = good_changed
        output_dict[item]['vice'] = bad_changed
    if output_format == 'json':
        return json.dumps(output_dict)
    else:
        return output_dict