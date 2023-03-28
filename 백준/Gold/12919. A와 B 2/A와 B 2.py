s=list(input())
t=list(input())
cnt=0

def dfs(ns):
    global cnt

    if len(ns) == len(s):
        if ns==s:
            cnt=1
            return
        return
    
    if ns[0]=="B":
        ns.reverse()
        ns.pop()
        dfs(ns)
        ns.append("B")
        ns.reverse()
    if ns[-1]=="A":
        ns.pop()
        dfs(ns)
        ns.append("A")
        

dfs(t)
print(cnt)
