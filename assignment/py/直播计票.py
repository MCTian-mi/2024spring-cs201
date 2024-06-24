def addVote(dic:dict, key:int):
    if key not in dic.keys():
        dic[key] = 1
    else:
        dic[key] += 1

votes = {}
ans = []
for x in list(map(int, input().split())):
    addVote(votes, x)
max = max(votes.values())
for key in votes.keys():
    if votes[key] == max:
        ans.append(key)
ans.sort()
print(" ".join(str(x) for x in ans))