def gcd(str1: str, str2: str) -> int:
    len1 = len(str1)
    len2 = len(str2)

    res = min(len1, len2)
    while res:
        if len1 % res == 0 and len2 % res == 0:
            return res
        res -= 1

    return res


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_str_len = gcd(str1, str2)

        gcd_str = str1[:gcd_str_len]

        # Recall // is floor division
        if str1 == gcd_str * (len(str1) // gcd_str_len) and str2 == gcd_str * (len(str2) // gcd_str_len):
            return gcd_str
        else:
            return ""

