import openai
import os

from transformers import GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate(prompt,max_tokens=1000, temperature=0):
    tokens = tokenizer.tokenize(prompt)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0]['text']

def decompose(question):
    prompt="Decompose a question in self-contained sub-questions. Use \"The question needs no decomposition\" when no decomposition is needed.\n\nExample 1:\n\nQuestion: Is Hamlet more common on IMDB than Comedy of Errors?\n\nDecompositions: \n1: How many listings of Hamlet are there on IMDB?\n2: How many listing of Comedy of Errors is there on IMDB?\n\nExample 2:\n\nQuestion: Are birds important to badminton?\n\nDecompositions:\nThe question needs no decomposition\n\nExample 3:\n\nQuestion: Is it legal for a licensed child driving Mercedes-Benz to be employed in US?\n\nDecompositions:\n1: What is the minimum driving age in the US?\n2: What is the minimum age for someone to be employed in the US?\n\nExample 4:\n\nQuestion: Are all cucumbers the same texture?\n\nDecompositions:\nThe question needs no decomposition\n\nExample 5:\n\nQuestion: Hydrogen's atomic number squared exceeds number of Spice Girls?\n\nDecompositions:\n1: What is the atomic number of hydrogen?\n2: How many Spice Girls are there?\n\nExample 6:\n\nQuestion: {0}\n\nDecompositions:"

    res = generate(prompt.format(question), max_tokens=256)
    # print(res)
    if res.lower().strip() == "the question needs no decomposition.":
        return [question]
    try:
        questions = [l for l in res.splitlines() if l != ""]
        questions = [q.split(':')[1].strip() for q in questions]
        return questions
    except:
        return [question]

