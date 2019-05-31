def giaithua1(n):
    if n == 1:
        return 1
    else:
        return n * giaithua1(n - 1)

def giaithua2(n):
    fact = [1]
    dem = 0
    for i in range(2, n + 1):
        fact.append(fact[dem] * i)
        dem += 1
    return fact[dem - 1]

if __name__ == '__main__':
    n = int(input('Nhap n = '))
    print("Cach de quy:")
    print(giaithua1(n))
    print("Cach quy hoach dong:")
    print(giaithua2(n + 1))