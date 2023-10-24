numberinput = int(input())
evencounter = 0
while (numberinput != 0):
  if numberinput % 2 == 0:
    evencounter +=1
  numberinput = int(input())

print(evencounter)