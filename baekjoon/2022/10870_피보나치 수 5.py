n = int(input())

def fibo(n):
    return n if n <= 1 else fibo(n-1) + fibo(n-2)

print(fibo(n))