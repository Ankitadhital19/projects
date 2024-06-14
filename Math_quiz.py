#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time

OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    expr = str(left) + " " + operator + " " + str(right)
    ans = eval(expr)
    return expr, ans

wrong = 0
input("Press enter to start")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, ans = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ": " + expr + " = ")
        if guess == str(ans):
            break
        else:
            print("Incorrect, try again.")
            wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("You finished in", total_time, "seconds")
print("---------------------")
print("Good job")
print("Total wrong answers:", wrong)


# In[ ]:




