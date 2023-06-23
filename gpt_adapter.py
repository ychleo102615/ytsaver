from array import array
from collections.abc import Generator
import openai

openai.api_key = "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";

with open('apikey.txt', 'r') as file:
    openai.api_key = file.read().rstrip

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    # type: ignore
    return response.choices[0].message["content"] # type: ignore

def generate(text):
    # text = f"""
    # You should express what you want a model to do by \
    #         providing instructions that are as clear and \
    #         specific as you can possibly make them. \
    #         This will guide the model towards the desired output, \
    #         and reduce the chances of receiving irrelevant \
    #         or incorrect responses. Don't confuse writing a \
    #         clear prompt with writing a short prompt. \
    #         In many cases, longer prompts provide more clarity \
    #         and context for the model, which can lead to \
    #         more detailed and relevant outputs.
    # """

    prompt = f"""
    #zh_tw
    以下是一段youtube影片語音轉換成的文字內容，沒有標點符號斷句。請你盡可能分析這段文字，並生成大致的摘要。
    ```{text}```
    """
    response = get_completion(prompt)

    return response

def main():
    import sys
    if len(sys.argv) < 2:
        print("No txt file specified.")
        return

    file_path = input("輸入文字檔名")

    with open(file_path, 'r') as file:
        text = file.read()
        print(generate(text))
