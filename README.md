# AICodeReviewer
Use LLM model to do code review as per code checklist . 

# INPUT : prompt.txt and diff.txt needs to be provided as arguments to main.py 
   python3 main.py --diff_file diff.txt --prompt_file prompt.txt

   prompt.txt --> Attached with prompt to review C/C++ code as of now but same can be extended for other programming languages .Checklist can be accustomed .
   diff.txt --> Its just output of "git diff -W file1.c file2.c"

# OUTPUT : LLM provided review would be given.

# PRE-REQUISITES: 
1.Below python libraries needs to be installed using pip or brew .
pip install langchain_groq  langchain_core os argparse
2.Create APIKEY for groqCloud. Very basic step so no additional info provided here.Replace YOUR_API_KEY in main.py with your key.

# COMMAND TO EXECUTE:
python3 main.py --diff_file diff.txt --prompt_file prompt.txt

