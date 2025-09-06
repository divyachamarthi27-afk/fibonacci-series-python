def fibonacci(n):
    fib = [0, 1]
    for i in range(2, abs(n) + 1):
        fib.append(fib[-1] + fib[-2])
        
    if n >= 0:
        return fib[:n + 1]
    else:
        negafib = []
        for i in range(abs(n) + 1):
            value = fib[i] if i % 2 == 0 else -fib[i]
            negafib.append(value)
        return negafib[::-1]

print("positive fibonacci (n=8):", fibonacci(8))
print("negative fibonacci (n=-8):", fibonacci(-8))

      
