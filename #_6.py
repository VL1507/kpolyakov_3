k = 0
for s in range(1, 1000):
    n = 10
    while s - n < 1000:
        s = s + n
        n = n + 5
    if n == 80:
        k += 1
        
print(k) # 70
