import pandas as pd
import os
import sys
import urllib.request
import random

import json
import jsonlines
from collections import OrderedDict


response_data = OrderedDict()

client_id = "p1dMOsis0VEaiZknXJGJ" # 개발자센터에서 발급받은 Client ID 값
client_secret = "QDDzUQGja_" # 개발자센터에서 발급받은 Client Secret 값


def papago(prompt_string):
    encText = urllib.parse.quote(prompt_string)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        return json.loads(response_body.decode('utf-8'))
        #print(response_body.decode('utf-8'))
    else:
        return "Error Code:" + rescode
        #print("Error Code:" + rescode)

def main():
    responses_papago_data_i = open("responses_papago_data_iii.jsonl",'w',encoding="UTF-8")
    
    dataset = pd.read_csv("data(test)/data_type_III.tsv",delimiter='\t',engine='python')
    print(type(dataset))

    print(dataset.loc[0][0])

    for i in range(100):
        each_response = papago(str(dataset.loc[i][0]))
        response_data.update({str(dataset.loc[i][0]):each_response["message"]["result"]["translatedText"]})
        print(dataset.loc[i][0])
    
    json.dump(response_data, responses_papago_data_i, indent = '\n', ensure_ascii=False)
    responses_papago_data_i.close()
    
if __name__ == '__main__':
    main()
