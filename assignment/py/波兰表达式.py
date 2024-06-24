def check(i):
    if i in ["+", "-", "/", "*"]:
        return(True)
    else:
        return(False)
def firstprocess(i):
    if i in ["+", "-", "/", "*"]:
        return(i)
    else:
        return((float(i)))
l = [firstprocess(x) for x in input().split()]
def secondprocess(list):
    j = len(list)
    if j != 1:
        for i in range(j):
            if check(list[i])&(~((check(list[i+1]))|(check(list[i+2])))):
                if list[i] == "+":
                    k = list[i+1] + list[i+2]
                elif list[i] == "-":
                    k = list[i+1] - list[i+2]
                elif list[i] == "*":
                    k = list[i+1] * list[i+2]
                elif list[i] == "/":
                    k = list[i+1] / list[i+2]
                list[i] = k
                list.pop(i+1)
                list.pop(i+1)
                return(secondprocess(list))
    else:
         return(list[0])       
print("%.6f\n"%secondprocess(l))