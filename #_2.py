print('c d a b')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if ((a <= b) and (b != c) and (d <= a)) == 1:
                    print(c, d, a, b)
'''
c d a b
1 0 0 0
0 0 0 1
0 0 1 1
0 1 1 1
'''
