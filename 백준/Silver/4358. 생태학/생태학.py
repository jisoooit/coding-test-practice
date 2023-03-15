from collections import defaultdict

trees=defaultdict(int)
all=0
while True:
    try:
        tree = input().strip()
        trees[tree]+=1
        all+=1
    except EOFError:
        break

keylist = sorted(list(trees.keys()))
for tree in keylist:
    print('%s %.4f' %(tree, (trees[tree]/all)*100))