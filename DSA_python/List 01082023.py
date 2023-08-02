# leetcode problem 1

hours = [0,1,2,3,4] 
target = 2

counter = 0
for i in range(len(hours)):
    if hours[i] >= target:
        counter += 1
        continue
print(counter)

# Leetcode problem 2

nums = [8,1,2,2,3]

outputList = []
for i in nums:
    outputList.append(sorted(nums).index(i))

# Leetcode problem 3

n = 7
rangeList = []
for i in range(1,n+1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        rangeList.append(i)
print(sum(rangeList))

# Leetcode problem 4

s = "Hello how are you Contestant"
k = 4

# Output: "Hello how are you"
# Explanation:
# The words in s are ["Hello", "how" "are", "you", "Contestant"].
# The first 4 words are ["Hello", "how", "are", "you"].
# Hence, you should return "Hello how are you".

character = []
for i in s.split():
    character.append(i)
    character = character[:4]
print(" ".join(character))

# Leetcode 5

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

for i,j in enumerate(s):
    print(i,j)
    