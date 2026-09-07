# Keyword args
# Ekhetre value deyar somoy arguments er order olot palot holeo problem nai.
"""def my_fun(f_name, l_name, age):
    print(f"Hello, I am {f_name} {l_name}. I am {age} years old.")
    
my_fun(age=20, l_name="Roy Chowdhury", f_name="Atonu")"""


# Arbitary number of key word arguments
def my_fun(**kwargs):
    print(kwargs) # ekhetre output ekta dictionary te key-value hisabe print hobe, ar amra chaile function call er somoy jotogulo iccha totogulo arguments pass korte parbo.
    
    print(f"Hello, my name is {kwargs['f_name']} {kwargs['l_name']}. I got {kwargs['marks']} in Mathematics.")
    
my_fun(age=20, l_name="Roy Chowdhury", f_name="Atonu", marks = 95)

