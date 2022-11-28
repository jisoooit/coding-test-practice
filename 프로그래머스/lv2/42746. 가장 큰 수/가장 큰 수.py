def solution(numbers):
    str_numbers = sorted(list(map(str, numbers)), reverse=True, key = lambda x:x*3)
    return str(int("".join(str_numbers)))
