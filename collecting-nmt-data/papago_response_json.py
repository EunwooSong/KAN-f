import os
import sys
import urllib.request
import random

import json
import jsonlines
from collections import OrderedDict


response_data_converted = OrderedDict()
response_data_origin = OrderedDict()

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
    responses_converted = open("responses_papago_converted.jsonl",'w',encoding="UTF-8")
    responses_origin = open("responses_papago_origin.jsonl",'w',encoding="UTF-8")
    
    # 지문 입력 란
    #prompt = input("Insert a prompt: ")
    #print(chatGPT(prompt).strip())
    
    cnt = 0
    
    
    #노이즈 있는 문장
    with jsonlines.open("prompt_data.jsonl") as f:
        for line in f:
            each_response = papago(str(line["prompt"]))
            cnt += 1
            
            response_data_converted.update({line["prompt"]:each_response["message"]["result"]["translatedText"]})
            #line prompt 수정
            
            print(line["prompt"])
            if cnt > 40:
                break

    print(response_data_converted)
    json.dump(response_data_converted, responses_converted, indent = '\n', ensure_ascii=False)
    responses_converted.close()
    

    #노이즈 없는 문장
    with open("ko_converted_data_modified.json", 'r',encoding="UTF-8") as f:
        json_object = json.load(f)

        for line in random.sample(json_object, 40):
            each_response = papago(str(line["ko_original"]))
            #cnt += 1
            
            response_data_origin.update({line["ko_original"]:each_response["message"]["result"]["translatedText"]})
            #line prompt 수정
            
            print(line["ko_original"])
            #if cnt > 40:
            #    break
            
    print(response_data_origin)
    json.dump(response_data_origin, responses_origin, indent = '\n', ensure_ascii=False)
    responses_origin.close()

if __name__ == '__main__':
    main()
