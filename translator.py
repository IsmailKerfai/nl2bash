import json
import ollama
from utils import is_safe


def load_prompts():
    with open('prompts.json') as f:
        examples = json.load(f)

    few_shot_messages = []

    for example in examples:
        few_shot_messages.append({"role" : example["role"], "content": example["content"]})

    return few_shot_messages


def translate_to_bash(nl_input: str, model='llama3.1:8b'):
    system_prompt = """
    You are a helpful assistant that converts natural language instructions into safe and correct Bash commands.
    
    - Output ONLY the Bash command.
    - Do NOT include any explanation or comments.
    - Avoid dangerous commands like 'rm', 'shutdown', or anything that modifies system state unless the user explicitly asks.
    - Be concise, correct, and assume the user runs Linux or macOS.
    """


    messages = [{'role' : 'system', 'content': system_prompt}]
    messages+= load_prompts()
    messages+= [{'role' : 'user', 'content': nl_input}]

    response = ollama.chat(model=model, messages=messages)
    return response['message']['content']
