import re

print(re.findall('(\S[a-z0-9]+@[a-z]+.[a-z]{3})', 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'))