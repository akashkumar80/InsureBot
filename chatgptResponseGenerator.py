import openai

openai.api_key = "YOUR_API_KEY"

def ask_gpt(query, history):
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    messages += history
    messages.append({"role": "user", "content": query})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    return response['choices'][0]['message']['content']
