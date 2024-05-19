a = int(input())
if a % 2 == 0:
    print("{} is even".format(a))
else:
    print("{} is odd".format(a))

# 다른 사용자 풀이 --> 1줄로 푼 것이 인상적
print(f"{a} is odd" if a % 2 else f"{a} is even")
