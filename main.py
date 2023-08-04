import os
import openai
openai.organization = "org-0zjmYYl5jY0K38Kvn3wzK7At"
openai.Model.list()
import polars as pl
import re
import time
from itertools import cycle

data_main = {"state": [],
             "feature": []}

df_main = pl.DataFrame(data_main, schema = 
                       {
                           "state": str,
                           "feature": str
                       })

us_states = [
    'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 
    'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 
    'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 
    'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 
    'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 
    'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
]

def ask_gpt(state):
    prompt = f"List 5 key linguistic features of {state} English"
    initial_question = f"You are a dialectologist."


    # List of messages representing a conversation
    messages = [
    {"role": "system", "content": f"{initial_question}"},
    {"role": "user", "content": f"{prompt}"}
        ]

    # Call the chat completions endpoint
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Use the appropriate chat model here
    messages=messages
    )

    # Extract the assistant's reply from the response
    assistant_reply = response['choices'][0]['message']['content']
    features = assistant_reply

    # Custom Python function to split at numbers and either periods or closed parentheses
    def split_string_at_numbers_and_periods_or_parentheses(s):
        return re.split(r'[\d]', s)

    # Use the custom function to split the string
    features_sep = split_string_at_numbers_and_periods_or_parentheses(features)


    for feature in features_sep:


        data = {"state": state,
                "feature": feature}

        df = pl.DataFrame(data, schema = 
                        {
                            "state": str,
                            "feature": str
                        })
        df_main.extend(df)
        path = "/Users/ischneid/chat-gpt-us-state-dialectology/main_df.csv"
        df_main.write_csv(path)
    time.sleep(40)
    return


def all_us_states_loop():
    for state in us_states:
        ask_gpt(state)
    return


index = [1, 2, 3]
for i in index:
    all_us_states_loop()