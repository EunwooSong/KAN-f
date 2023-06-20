from googletrans import Translator

translator = Translator()

import pandas as pd
import os
import sys
import urllib.request
import random

import json
import jsonlines
from collections import OrderedDict



response_data = OrderedDict()


responses_google_data_i = open("responses_google_data_iii.jsonl",'w',encoding="UTF-8")
    
dataset = pd.read_csv("data(test)/data_type_III.tsv",delimiter='\t',engine='python')

for i in range(100):
    each_response = translator.translate(str(dataset.loc[i][0]), dest="en")
    response_data.update({str(dataset.loc[i][0]):each_response.text})
    print(dataset.loc[i][0])

json.dump(response_data, responses_google_data_i, indent = '\n', ensure_ascii=False)
responses_google_data_i.close()
