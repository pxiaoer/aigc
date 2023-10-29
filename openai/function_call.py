import json
import os 

import openai



openai.api_key = os.environ['OPENAI_API_KEY']


def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "28度",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)



def say_hello(name, unit="hello"):
    hello_info = {
        "name": name,
        "content": "hello",
        "unit": unit,
    }

    return json.dumps(hello_info)



# define a function
functions = [
    {
        "name": "get_current_weather",
        "description": "给出一个地点当前的天气情况",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "城市名，比如：成都",
                },
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        },
    },
]


'''  
    {
        "name": "say_hello",
        "description": "say hello to user",
        "parameters": {
            "type": "object",
            "properties": {
                "name": "string",
                "description": "people name",
            },
            "unit": {"type": "string", "enmu":["hello"]},
        },

        "required": ["name"],
    }
]
'''


'''
messages = [
    {
        "role": "user",
        "content": "What's the weather like in chengdu?",
    }
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=messages,
    functions=functions
)

print(response)

response_message = response["choices"][0]["message"]["function_call"]["arguments"]

print(response_message)

'''


messages = [
    {
        "role": "user",
        "content": "What's the weather in chengdu?!",
    }
]
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=messages,
    functions=functions,
    function_call={"name": "get_current_weather"},
)
print(response["choices"][0]["message"])


messages.append(response["choices"][0]["message"])
args = json.loads(response["choices"][0]["message"]['function_call']['arguments'])
observation = get_current_weather(args)

messages.append(
        {
            "role": "function",
            "name": "get_current_weather",
            "content": observation,
        }
)


print(messages)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=messages,
)
print(response)


