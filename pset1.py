#part 1
s = 'hannah'
vowel = 0
for i in range (len(s)):
    if (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
        vowel += 1
print('Number of vowels: ' + str(vowel))

#part 2
# Count the "bob"s in String s
s = 'oooooooooobob'
word = 'bob'
i = 0
j = 0
count = 0
for i in range (len(s)):
    #if the same, check next letter in s
    #if next letter in s not the same as next in word, i change
    #else move on to next letter
    if s[i] == word[j]:
        for j in range (len(word)):
            i += 1
            j += 1
            if j == len(s) or i == len(s):
                break
            if s[i] != word[j]:
                j = 0
                break
            if s[i] == word[len(word)-1]: 
                count += 1
                j = 0
                break  
print(count) 

####################
#part 3: longest alphabetical substring
#take the first one if there are multiple
attempt1 = 'abckjhi'
attempt2 = 'ishkabibble'
attempt3 = 'zyxwvut'
def alphasub (s):
    substr = ''
    holder = s[0] #first letter always
    for i in range(1,len(s)):
        j = i - 1
        if s[i] >= s[j]:
            holder += s[i]
        elif s[i] < s[j]:
            if len(substr) <= len(holder):
                if len(substr) != len(holder):
                    substr = holder
                holder = s[i]
            else:
                holder = s[j] 
    return 'Longest substring in alphabetical order is: ' + str(substr)
alphasub(attempt1)
alphasub(attempt2)
alphasub(attempt3)
alphasub('azcbobobegghakl') #test in example 
