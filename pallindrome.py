'''
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. 
It is also case-insensitive and ignores all non-alphanumeric characters.

'''
def isPalindrome(s: str) -> bool:
        original_str=s.replace(" ","")
        original_str = ''.join(char for char in original_str if char.isalnum())
        reverse_str="".join(reversed(original_str))
        if (original_str.lower()==reverse_str.lower()):
            return True
        else:
            return False

        