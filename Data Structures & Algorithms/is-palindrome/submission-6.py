import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().strip()
        if s=="":
            return True
        og_str=""

        for char in s:
            if char.isalnum():
                og_str+=char
        pal_str=""
        for i in range(len(og_str)):
                char=og_str[len(og_str)-1-i]
                if char.isalnum():
                    pal_str+=(char)
        if pal_str==og_str:
            return True
        return False
