"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise."""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = s.lower()
        word = ""
        for char in ss:
            if char.isalnum():
                word += char
                
        return word == word[::-1]
        
            