#dic = {'a':[10,20,30]}
#print(dic['a'][1])
#dic={'a':[{'b':2},20,30]}
#print(dic['a'][0]['b'])

from openai import OpenAI
CLIENT = OpenAI(api_key='XXX')
response = client.chat.completions.create(
    messages=[
        {
            'role':'user',
            'content':'請規劃CHATPGT課綱'
        }
    ],
    model='gpt-3.5-turbo'
)
print(response,type(response))
print(response.choices[0].message.content)