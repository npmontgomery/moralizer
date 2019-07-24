from auxilliary_functions import *

#text = read_file('practice_text.txt')


def read_file(filename):
    with open(filename, 'r',encoding='utf-8') as file:
        return file.read()

def moralize(input_text, output_format='pydict'):
    analyzed_text = word_frequency_dict(input_text)
    return count_keywords(analyzed_text, output_format)




