class Solution:
    def romanToInt(self, s: str) -> int:
        base10 = 0
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        it = iter(range(0, len(s)))
        for i in it:
            if i == len(s)-1:
                base10 += mapping[s[i]]
            elif s[i] + s[i+1] in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                base10 += mapping[s[i+1]] - mapping[s[i]]
                next(it, None)
            else:
                base10 += mapping[s[i]]
        return base10