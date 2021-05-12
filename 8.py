import re

textfile = open('text2.txt', 'r')
matches = []
reg = re.compile('[A-Z|@][\w|!]+:?')
for line in textfile:
    matches += reg.findall(line)
textfile.close()
print(matches)