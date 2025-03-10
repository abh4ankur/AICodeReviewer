# AICodeReviewer
Use LLM model to do code review as per code checklist . 

# INPUT : prompt.txt and diff.txt needs to be provided as arguments to main.py 
   python3 main.py --diff_file diff.txt --prompt_file prompt.txt

   prompt.txt --> Attached with prompt to review C/C++ code as of now but same can be extended for other programming languages .Checklist can be accustomed .
   diff.txt --> Its just output of "git diff -W file1.c file2.c"
   
# OUTPUT : LLM provided review would be given.

# COMMAND TO EXECUTE:
python3 main.py --diff_file diff.txt --prompt_file prompt.txt

