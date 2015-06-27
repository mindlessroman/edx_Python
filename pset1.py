#part 1
s = 'hannah'
vowel = 0
for i in range (len(s)):
    if (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
        vowel += 1
print('Number of vowels: ' + str(vowel))
