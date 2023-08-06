#---------- leetcode problem 1 ----------

s = "leetcodeisacommunityforcoders"
vowels = "aeiou"

#Output: "ltcdscmmntyfrcdrs"
output = ""
for i in s:
    if i not in vowels:
        output += i

#---------- leetcode problem 2 -----------

address = "1.1.1.1"
#Output: "1[.]1[.]1[.]1"

output = ""
address.replace(".","[.]")

#---------- leetcode problem 3 -----------

jewels = "aA"
stones = "aAAbbbb"
# Output: 3

lst = [i for i in jewels]
lst1 = [i for i in stones]
count = 0
for i in lst:
    for j in lst1:
        if i == j:
            count += 1
print(count)


count = 0
for i in stones:
    if i in jewels:
        count += 1

#---------- leetcode problem 4 -----------

command = "G()(al)"

# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".

command.replace("()","o").replace("(al)","al")

#---------- leetcode problem 5 ----------

s = "RLRRLLRLRL"

# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL"
# each substring contains same number of 'L' and 'R'.

count = 0
for i in s:
    print(i)



