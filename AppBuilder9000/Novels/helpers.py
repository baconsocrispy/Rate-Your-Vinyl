import requests
import json
from django.shortcuts import render, get_object_or_404, redirect


# parse JSON response from defineWord() - JSON response stored in variable 'define'
def parseDefine(define):
    all_definitions = []
    definitions = define[0]['meaning']
    for word_type in definitions:
        for word_def in definitions[word_type]:
            print(word_def['definition'])
            all_definitions.append(word_def['definition'])
    return all_definitions
