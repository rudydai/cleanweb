f = open("test")
content = f.readlines()

everything = ""
for line in content:
    l = line.strip()
    chars = l.split()
    for ch in chars:
        everything += ch.decode("hex")

print everything
