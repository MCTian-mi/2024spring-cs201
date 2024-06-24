import re
intermedia = input()
listy = [int(x) for x in re.findall(r".(?<!\+0)n\^(\d+)",intermedia)]+[0]
print("n^"+str(max(listy)))