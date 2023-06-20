import os
import openai
import argparse

import json
import jsonlines
from collections import OrderedDict

response_data = OrderedDict()

YOUR_API_KEY = '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'

def chatGPT(prompt, API_KEY=YOUR_API_KEY):
    
    # set api key
    openai.api_key = API_KEY

    # Call the chat GPT API
    completion = openai.Completion.create(
			  engine = 'text-davinci-003'     # 'text-curie-001'  # 'text-babbage-001' #'text-ada-001'
			, prompt = prompt
			, temperature = 0.5 
			, max_tokens = 1024
			, top_p = 1
			, frequency_penalty = 0
			, presence_penalty = 0)
        AQ
    return completion['choices'][0]['text']


def main():
    responses = open("responses.jsonl",'w',encoding="UTF-8")
    
    # 지문 입력 란
    #prompt = input("Insert a prompt: ")
    #print(chatGPT(prompt).strip())
    
    cnt = 0
    
    with jsonlines.open("prompt_data.jsonl") as f:
        for line in f.iter():
            cnt += 1
            response_data.update({line["prompt"]:cnt}) #line prompt 수정
            
            print(line["prompt"])
            if cnt > 100:
                break

    print(response_data)
    json.dump(response_data, responses, indent = '\n', ensure_ascii=False)
    responses.close()


if __name__ == '__main__':
    main()
