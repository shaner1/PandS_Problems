l=[]
i = int(input("Please enter a positive integer: "))

l.append(int(i))

while i != 1:
    if i % 2 == 0:
        i /= 2
        l.append(int(i))
    else:
        i = (i*3)+1
        l.append(int(i))

print(l)