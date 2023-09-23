# Get all the words
f = open("Better_Words.txt",'r')
words = []

for l in f:
    l=l[0:5]
    words.append(l)


f.close()

c = []

n = int(input("Enter the number of characters you know: "))
print()
print("Enter the Letter and position (Use 0 if you don't know the position)")

for i in range(n):
    c.append(input().split(" "))

for i in range(len(c)):
    c[i][1] = int(c[i][1])


w = [[],[],[],[],[]]

for j in range(len(c)):
    if j == 0:
        if c[j][1] == 0:
            for i in range(len(words)):
                if c[j][0] in words[i]:
                    w[j].append(words[i])
        else:
            for i in range(len(words)):
                try:
                    if words[i][c[j][1]-1] == c[j][0]:
                        w[j].append(words[i])
                except:
                    pass
    else:
        if c[j][1] == 0:
            for i in range(len(w[j-1])):
                if c[j][0] in w[j-1][i]:
                    w[j].append(w[j-1][i])
        else:
            for i in range(len(w[j-1])):
                try:
                    if w[j-1][i][c[j][1]-1] == c[j][0]:
                        w[j].append(w[j-1][i])
                except:
                    pass

print(w[n-1])