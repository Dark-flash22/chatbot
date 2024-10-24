'''import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role":"user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":  # Corrected the spacing here
    print("Chatbot is running...")  # Optional debug line
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)http://127.0.0.1:7860'''

import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "SK GPT 2.0")

demo.launch(share=True)