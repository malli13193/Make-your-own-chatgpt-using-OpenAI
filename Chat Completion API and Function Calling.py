import pandas as pd
pd.DataFrame(list(all_models),columns=["id","created","object","owned_by"])
# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
client = OpenAI(api_key=mykey)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {
      "role": "user",
      "content": "who won the first cricket worldcup?"
    }
      ]
    ,
    max_tokens=150,
    n=3
)
type(response)
response.choices[0].message.content
# now let try to understand the different parameters inside the methods
model= ""
prompt=input prompt
max_tokens=in how many number of tokens you want result
temperature=for getting some creative output
n= number of the output
