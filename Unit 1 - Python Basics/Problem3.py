alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = 'azcbobobegghakl'

longest = ''
li = list()

for char in range(len(s)):
    ls = s[char]
    for i in range(char+1, len(s)):
        print(s[i-1], s[i], len(alphabet.split(s[i-1])[0]), len(alphabet.split(s[i])[0]))
        if len(alphabet.split(s[i])[0]) >= len(alphabet.split(s[i-1])[0]):
            ls += s[i]
        else: break
    print(ls)
    li.append(ls)

for item in li:
    if len(item) > len(longest): longest = item
print('Longest substring in alphabetical order is:', longest)