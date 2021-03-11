def tail(sequence, n):
    if n < 0:
        return []
    if type(sequence) == list:
        return sequence[-n:]
    return sequence[-n:].split()



print(tail([1, 2, 3, 4, 5], -3))