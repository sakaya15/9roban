s = list(map(int,input().split()))
if s[0]*s[1] % 2 == 0:
  print("Even")
elif s[0]*s[1] % 2 == 1:
  print("Odd")
