import re

textfile = open('myText1.txt', 'r')
matches = []
reg = re.compile('[A-Z]{1}[a-z]{3}:')
for line in textfile:
    matches += reg.findall(line)
textfile.close()
print(matches)