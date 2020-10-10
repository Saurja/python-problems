def pallindrome(s):
    reverse = []

    for i in reversed(range(len(s))):
        reverse.append(s[i])

    if s == ''.join(reverse):
        print("Pallindrome")
    else:
        print("Not Pallindrome")

s = "wow"
pallindrome(s)