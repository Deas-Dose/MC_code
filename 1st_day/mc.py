with open("message.txt", "r") as f:
    content = f.readline()
    chars = []
    for i,letter in enumerate(content):
        if letter == "M":
            m = i
        elif letter == "C":
            c = i
            chars.append(chr(c - m -1))
    print("".join(chars))