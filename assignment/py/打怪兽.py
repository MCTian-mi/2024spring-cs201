'''
n = int(input())
for _ in range(n):
    skills, maxskillspertime, hp = map(int, input().split())
    sety = [[int(x) for x in input().split()] for _ in range(skills)]
    sety.sort(key= lambda x: x[1], reverse= True)
    sety.sort(key= lambda x: x[0])
    def letsfight(sety, maxskillspertime, hp):
        checky = 0
        timey = 1
        timeynow = 1
        for i in range(skills):
            timeynow = sety[i][0]
            if timeynow != timey:
                hp -= sety[i][1]
                timey = timeynow
                checky = 1
            elif checky < maxskillspertime:
                hp -= sety[i][1]
                checky += 1
            if hp < 1:
                return(timey)
        return("alive")
    print(letsfight(sety, maxskillspertime, hp))
'''
    
n = int(input())
for _ in range(n):
    skills, maxskillspertime, hp = map(int, input().split())
    sety = [[int(x) for x in input().split()] for _ in range(skills)]
    sety.sort(key= lambda x: (x[0], -x[1]))
    def letsfight(sety, maxskillspertime, hp):
        checky = 0
        timey = 1
        timeynow = 1
        for i in range(skills):
            timeynow = sety[i][0]
            if timeynow != timey:
                hp -= sety[i][1]
                timey = timeynow
                checky = 1
            elif checky < maxskillspertime:
                hp -= sety[i][1]
                checky += 1
            if hp < 1:
                return(timey)
        return("alive")
    print(letsfight(sety, maxskillspertime, hp))