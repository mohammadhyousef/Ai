import openai

openai.api_key = ('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')

user_input = input('user: ')
response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role":"user","content":user_input}]
)
print (response['choices'][0]['message']['content'])