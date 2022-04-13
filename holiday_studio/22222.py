with open("24-1.txt") as f:
    lst = f.readline()
count = 0
lst1 = []
for i in range(1, len(lst)):
    if lst[i] == lst[i-1]:
        count+=1
    elif lst[i] == lst[i-1]:
        print(count)
        lst1.append(count)
        count = 0
print(lst1)




