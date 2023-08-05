# problem Leetcode

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"

getItem = []
for i in items:
    if ruleKey == "type" and ruleValue == i[0]:
        getItem.append(i)
    elif ruleKey == "color" and ruleValue == i[1]:
        getItem.append(i)
    elif ruleKey == "name" and ruleValue == i[2]:
        getItem.append(i)
print(len(getItem))

# Array VS LIST

import numpy as np
arr = np.array([1,2,3,4,5])
lst = [1,2,3,4,5]

print(arr/2)
print(lst/2)

# List comprehension

prev_list = [1,2,3]
new_list = [i*2 for i in prev_list]


# Conditional List comprehension

prev_list = [1,2,3,4,5,6]
new_list = [i for i in prev_list if i % 2 == 0]

sentence = 'this is for the testing purpose'

def is_constant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonant = [i for i in sentence if is_constant(i)]

