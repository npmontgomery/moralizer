# Moralizer
> Simple tool to get the Moral Foundations counts of a given text. 

![MIT](https://img.shields.io/dub/l/vibe-d.svg?style=flat-square)
![dependencies](https://img.shields.io/david/expressjs/express.svg?style=flat-square)
![python](https://img.shields.io/badge/python-3.6%2C3.7-blue.svg?style=flat-square)

## Installation
```shell
pip install moralizer
```
SpaCy requires the following add-on.
```shell
python -m spacy download en_core_web_sm
```
## Description 
Moralizer returns word counts of a text based on the [Moral Foundations Vocabulary 2.0](https://osf.io/ezn37/) in a neat and organized JSON object or Python dictionary.

## Use
Structure
- moralizer
  - read_file(input_file)
  - moralize(text, output_format=default is Python dictionary, add ".json" for output in JSON).


## Dependencies
Moralizer only uses one outside dependency, the delightfully opinionated [**spaCy**](https://spacy.io/).

## Under Construction 
- Tests
- Documentation