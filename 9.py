import re

print(re.findall('[a-z]+@[a-z]+.[a-z]{3}', 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'))