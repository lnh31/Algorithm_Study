dial = {'ABC': 3,
        'DEF': 4,
        'GHI': 5,
        'JKL': 6,
        'MNO': 7,
        'PQRS': 8,
        'TUV': 9,
        'WXYZ': 10}

word = input()

min_time = 0 

for key, value in dial.items():
    for i in word:
        if i in key:
            min_time += value
print(min_time)
