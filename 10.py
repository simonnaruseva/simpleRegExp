import re

textfile = open('text3.txt', 'r')
match1 = []
reg = re.compile('[a-z]+@[a-z]+.[a-z]+[.][a-z]+')
for line in textfile:
    match1 += reg.findall(line)
textfile.close()
print(match1)
