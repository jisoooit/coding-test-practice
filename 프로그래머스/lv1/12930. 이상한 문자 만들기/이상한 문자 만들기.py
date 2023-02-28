def solution(s):
    answer = []
    words = s.split(" ")
    print(words)
    for word in words:
        w = ""
        for i in range(len(word)):
            if i % 2:
                w += word[i].lower()
            else:
                w += word[i].upper()
        answer.append(w)
        print(answer)

    result=' '.join(answer)
    print(result.split(" "))
    print(result)
    return result