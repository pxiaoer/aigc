import os

from langchain.llms import OpenAI

llm = OpenAI(model_name="text-davinci-003",max_tokens=200)
text = llm("你知道P小二么？")

print(text)