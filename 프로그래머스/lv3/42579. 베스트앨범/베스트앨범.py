from collections import defaultdict

def twocheck(answer, g_songs):
    
    if len(g_songs) >= 2:
        answer += g_songs[:2]
    else:
        answer +=[g_songs[0]]


        
def solution(genres, plays):
    songs = defaultdict(dict)
    for i,(g, p) in enumerate(zip(genres, plays)):
        songs[g][i]=p

    g_sort=dict()
    for g in songs.keys():
        g_sort[g]=sum(songs[g].values())
    
    g_sort=dict(sorted(g_sort.items(), key=lambda x: -x[1]))
    answer = []
    g_songs=[]
    
    if len(g_sort) ==1:
        g_songs=sorted(songs[genres[0]], key = lambda x: (-songs[genres[0]][x],x)) #value값 기준으로 key정렬
        twocheck(answer, g_songs)
    else:
        for i in range(len(g_sort)):
            gen = list(g_sort.keys())[i]
            g_songs=sorted(songs[gen], key = lambda x: (-songs[gen][x],x)) #value값 기준으로 key정렬
            twocheck(answer, g_songs)

    return answer