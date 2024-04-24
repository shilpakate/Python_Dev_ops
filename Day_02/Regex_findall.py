# import re
# text="The quick brown box"
# pattern=r"brown"
# search=re.search(pattern,text)
# if search:
#     print("pattern found",search.group())
# else:
#     print("pattern not found")

import re

text = "The quick brown fox"
pattern = r"brown"

#search = re.findall(pattern, text)
search=re.search(pattern,text)
if search:
    #print("Pattern found:", pattern)
    print("Pattern found:",search.group())
else:
    print("Pattern not found")