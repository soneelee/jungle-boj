# 0!=1, 재귀함수 : 프랙탈
n = int(input())

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

print (factorial(n))