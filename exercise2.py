arrangement1 = "()(((()())(())()))(())"
print(len(arrangement1))
answer1 = 17
print(solution2(arrangement1) == answer1)

arrangement2 = "(((()()()(()())((())))()())())"
answer2 = 33
print(solution2(arrangement2) == answer2)





razer = '()(((()())(())()))(())'
line1 = '----(----)(--)--------'
line2 = '---(------------)-----'
line3 = '--(--------------)(--)'

lines = list({line1, line2, line3})
#print(len(razer))

def HowMany(line):
    count1=0
    count2=0
    for num in line :
        if num == '(':
            count1 += 1
        if num == ')':
            count2 += 1
    if count1 == count2 :
        return count1
    else:
        return 0

def CanCut(line) :
    result = [0] * len(line)
    dum = 0
    for num in range(0, len(line),1) :

        if line[num] == ')':
            dum = 0
        else :
            pass
        result[num] = dum
        if line[num] == '(':
            dum = 1
    return result


def Cutting(line1,razer):
    result = list(line1)
    for  i in range(0, len(razer),1):
        if razer[i:i+2] == '()' and sum(CanCut(line1)[i:i+2])==2:
            result[i:i+2] ={')','('}
    return result

answer = 0
for line in lines:
    temp=Cutting(line,razer)
    temp2 = ''.join(temp)
    answer += HowMany(temp2)
print(answer)
