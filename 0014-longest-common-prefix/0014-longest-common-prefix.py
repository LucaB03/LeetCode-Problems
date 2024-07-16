class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lprefix = ""
        if strs[0] == "":
            return lprefix
        for i in range(1,len(strs[0])+1):
            prefix = strs[0][:i]
            for word in strs:
                if prefix != word[:i]:
                    return lprefix
            lprefix = prefix
        return lprefix