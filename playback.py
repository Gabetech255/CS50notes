x = input("enter your string _ ")
# .split creates a list 
words = x.split()
numwords = len(words)
count = 0

for word in words:
    if count == numwords - 1:
        print(word)
        break
    print(word + "..." , end = '')
    count = count + 1