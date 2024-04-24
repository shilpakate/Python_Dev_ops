import re
text="apple,ba,cat,dog"
pattern=r","
split_result=re.split(pattern,text)
print(f"Split_result:{split_result}",)