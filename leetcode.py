class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for letter in strs[1:]:
            while letter[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                
                if not prefix:
                    return ""
        return prefix
                
strs = ["flower","flow","flight"]                
leetcode = Solution()
print(leetcode.longestCommonPrefix(strs))                