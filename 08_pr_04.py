# n! = n * (n-1)!
# sum(n) = sum(n-1) + n

def sum_recursive(n):
    if n == 0 or n == 1 :
        return 1
    return sum(n-1) + n


s = sum_recursive(5)
print(s)
