import re
#55-50+40-10+20-10+10
s=input()
s = re.split('([+|-])', s) #문자열 나누기

answer=0

minus=[]
for i in range(len(s)): #마이너스 인덱스 구하기
  if s[i]=='-':
    minus.append(i)

if len(minus)!=0:
  answer+=sum([int(j) for j in s[:minus[0]] if j.isdigit()]) #처음부터 첫 마이너스까지 합 구하기
  answer-=sum([int(j) for j in s[minus[len(minus)-1]:] if j.isdigit()]) #마지막 마이너스 빼기
else:
  answer+=sum([int(j) for j in s if j.isdigit()])

for j in range(len(minus)-1): #중간 마이너스 구간 빼기
  answer-=sum([int(j) for j in s[minus[j]:minus[j+1]] if j.isdigit()])



print(answer)