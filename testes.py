# N = int(input())

# while(N > 0):
  
#   a,b = input().split()
#   print(a[-len(b):])
  
#   if a[-len(b):] == b:
#     print('encaixa')
#   else:
#     print('nao encaixa')
    
#   N -= 1

# a,b = input().split()
# print(a[-len(b):])



N = int(input())

while (N > 0):
    n1, n2 = input().split()

    n1 = n1[-len(n2):]

    if n1 == n2:
        print("encaixa")
    else:
        print("não encaixa")
    N = N-1