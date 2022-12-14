import os
import openai
#Enter Your Api Key for GPT-3
openai.api_key= ""

start_sequence="\nAI: " 
restart_sequemce='nHuman: '

def gpt3(prompt, engine='davinci', response_length=64,
         temperature=.7, top_p=1, frequency_penalty=0, presence_penalty=0,
         start_text='', restart_text='', stop_seq=[]):
    response = openai.Completion.create(
        prompt=prompt + start_text,
        engine=engine,
        max_tokens=response_length,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop_seq,
    )
    answer = response.choices[0]['text']
    new_prompt = prompt + start_text + answer + restart_text
    return answer, new_prompt

def chat():
    prompt = """Human: Hey, how are you doing? 
AI: I like cars and people. What would you like to chat about?
Human:"""
    while True:
        prompt += input('You: ')
        answer, prompt = gpt3(prompt,
                              temperature=0.7,
                              frequency_penalty=1,
                              presence_penalty=1,
                              start_text='\nAI:',
                              restart_text='\nHuman: ',
                              stop_seq=['\nHuman:', '\n'])


        mytext=answer
      
        
        print('GPT-3:' + answer)
if __name__ == '__main__':
    chat()

