
import re
text="Mr. Prashant Kate"
pattern=r"Prashant"
search=re.match(pattern,text)
if search:
    print("Pattern is matched:",search.group())
else:
    print("Pattern is  not matched:")