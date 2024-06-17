import time
from  groqGpt import GroqLlama
from ConversationLedger import ConversationLedger
import sys

gpt_ask = sys.stdin.read().strip()
# input_data = "Hows is going"
init_time = time.time()
platform = GroqLlama()
conversation = ConversationLedger("testing", "chatHistory", "test")

# while (True):
# gpt_ask = input("ask llama3 anything you want. Type 'end' to exit shell")
    # if gpt_ask == "end":
    #     exit()

conversation.addPrompt(gpt_ask)
formated_input = conversation.getFormattedConversation()
# print(formated_input.type)
output = platform.simple_response(gpt_ask)
timeInferring = (time.time() - init_time)
print ("time to generate text : {}".format(timeInferring))

# platform.specifyModel("8b")

# output = platform.getResponse(input_data)
print(output)
conversation.addResponse(output)
    


# import os

# from groq import Groq

# client = Groq(
#     api_key="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",
# )

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Explain the importance of fast language models",
#         }
#     ],
#     model="llama3-8b-8192",
# )

# print(chat_completion.choices[0].message.content)