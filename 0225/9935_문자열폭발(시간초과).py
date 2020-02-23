str = input()
bomb = input()

while bomb in str:
    str = str.replace(bomb, "")

if str is "":
    print("FRULA")
else:
    print(str)
