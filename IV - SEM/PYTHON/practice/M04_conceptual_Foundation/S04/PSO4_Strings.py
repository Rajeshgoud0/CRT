"""
s="python"
print(len(s))
print(max(s))
print(min(s))
print(max("abc123ABC"))
print(min("abc123ABC"))     

s = "python"
print(s.find("on"))
print(s.find("xyz"))
"""
s = "python"
rev = ""
for i in range(len(s)-1, -1, -1):
    rev += s[i]
print(rev)
if s == rev:
    print("palindrome")
else:
    print("not palindrome")

# Anagram
s1 = "paces"
s2 = "space"
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not a Anagram")
    
