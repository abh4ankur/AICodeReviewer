from langchain_groq import ChatGroq 
from langchain_core.prompts import PromptTemplate
import os 
import argparse

model = "llama-3.1-8b-instant"
YOUR_API_KEY = "YOUR_GROQ_KEY"

def read_from_file(fileName):
    with open(fileName, 'r') as file:
        return file.read().strip()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, streaming=False,model=f"{model}",api_key=YOUR_API_KEY)
    
    def askQuestion(self, diff, prompt):
        escaped_diff = diff.replace("{", "{{").replace("}", "}}")

        final_prompt = PromptTemplate.from_template(f"""{prompt}

            Here is the code difference:

            {escaped_diff}""")

        chainData = final_prompt | self.llm
        res = chainData.invoke({})
        return res.content

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Code review assistant.")
    parser.add_argument('--diff_file', type=str, required=True, help="The code difference to review.")
    parser.add_argument('--prompt_file', type=str, required=True, help="The path to the prompt file.")

    args = parser.parse_args()

    diff = read_from_file(args.diff_file)
    prompt = read_from_file(args.prompt_file)

    chain = Chain()
    res = chain.askQuestion(diff, prompt)
    print(res)
