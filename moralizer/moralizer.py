from auxilliary_functions import *


def read_file(filename):
    """
    Reads in a file as utf-8.
    :param filename: Filepath to the file to be read.
    """
    with open(filename, 'r',encoding='utf-8') as file:
        return file.read()

def moralize(input_text, output_format='pydict'):
    """
    Takes input text and returns format as either a Python dictionary or JSON object.
    :param input_text: Text you want to analyze.
    :param output_format: defaults to Python dictionary, enter '.json' for output in a JSON object.po
    """
    analyzed_text = word_frequency_dict(input_text)
    return count_keywords(analyzed_text, output_format)




