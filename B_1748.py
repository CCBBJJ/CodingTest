N = int(input())
t = 10
c = 1
result = 0 
if N<10:
    result = N
else:
    while N//t:
        #N의 자리수를 파악함과 동시에 더하기
        result += (t-10**(c-1))*c
        t *= 10
        c += 1
    result += (N-10**(c-1)+1)*c
print(result)