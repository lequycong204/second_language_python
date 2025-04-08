def checkPassword(s):
    if len(s) > 100 or len(s) < 8:
        return False

    has_upper = any(char.isupper() for char in s)
    has_lower = any(char.islower() for char in s)
    has_digit = any(char.isdigit() for char in s)
    has_special = any(char in "~!@#$%^&*" for char in s)

    return has_upper and has_lower and has_digit and has_special

list = []
while True:
    line = input().strip()
    if line == "":
        break

    list.append(line)
    

for i in list:
    print(checkPassword(i))
