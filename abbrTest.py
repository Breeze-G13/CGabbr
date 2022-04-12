#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Author: Breeze.G (GAO Wentao) from Capgemini China JTP 0411/2022 cohort

# import some libraries
import pandas as pd
import numpy as np
import random

# read the abbreviation table
data = pd.read_csv('abbr.csv')
df = data.copy(deep=True)


# In[2]:


df.loc[:, "testCounts"] = 0
total = len(df)
toTest = df.copy(deep=True)
tested = pd.DataFrame()

while len(toTest)>0: 
    i = random.randint(0, len(toTest)-1)
    df.loc[i, "testCounts"] += 1
    prompt = "[" + toTest.loc[i, "label"].upper() + "] " + toTest.loc[i, "abbr"]
    key = toTest.loc[i, "full"]
    ans = input(prompt+" = ")
    if ans in ["stop", "Stop", "STOP", "done", "Done", "DONE"]:
        print(">> Test halted. \n")
        df.loc[i, "testCounts"] -= 1
        break
    elif ans.upper()==key.upper():
        print(">> Correct! \n")
        tested = tested.append(toTest.loc[i])
        if df.loc[i, "testCounts"] == 1:
            tested.loc[i, "correct"] = True
        toTest = toTest.drop(i).reset_index(drop=True)
    else:
        print(">> Incorrect.", prompt, "=", key, "\n")
        tested = tested.append(toTest.loc[i])

tested.drop_duplicates(subset="abbr", keep='first', inplace=True)
oneTimeCorrect = len(tested.loc[tested.correct==True])
print("Among", len(tested), "unique abbreviations tested,", oneTimeCorrect, "was correct at first time.")
print("One-time correct rate is %.2f%%" % round(oneTimeCorrect/len(tested)*100, 2))

