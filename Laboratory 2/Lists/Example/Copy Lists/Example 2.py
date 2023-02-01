n = int(input())
a = []
requests = []
isTrueRequests = False
for i in range(n):
    l = input()
    a.append(l)
k = int(input())
for i in range(k):
    requests.append(input())
result = []
for i in range(n):
    for j in range(k):
        if a[i].lower().find(requests[j].lower()) != -1:
            isTrueRequests = True
        else:
            isTrueRequests = False
            break
    if isTrueRequests == True:
        result.append(a[i])
        isTrueRequests = False
print(*result, sep='\n')