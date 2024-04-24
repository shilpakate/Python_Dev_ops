import re
text="The quick brown fox jumps over the lazy brown dog"
pattern=r"brown"
replacement="red"
new_text=re.sub(pattern,replacement,text)
print(f"Original text:{text}")
print(f"Modified Text:{new_text}")
