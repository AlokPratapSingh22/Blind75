"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
 

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""

def longestCommonSubsequence(text1: str, text2: str) -> int:
    """Bruteforce"""
    def helper(a, b):
        if a >= len(text1) or b >= len(text2):
            return 0
        if text1[a] == text2[b]:
            return 1+helper(a+1, b+1)
        return max(helper(a+1, b), helper(a, b+1))
    return helper(0, 0)


def longestCommonSubsequence(text1: str, text2: str) -> int:
    """Memoized"""
    def helper(a, b, memo={}):
        if (a, b) in memo:
            return memo[(a, b)]
        if a >= len(text1) or b >= len(text2):
            return 0
        if text1[a] == text2[b]:
            memo[(a, b)] = 1+helper(a+1, b+1, memo)
            return memo[(a, b)]

        memo[(a, b)] = max(helper(a+1, b, memo), helper(a, b+1, memo))
        return memo[(a, b)]
    return helper(0, 0)


def longestCommonSubsequence(text1: str, text2: str) -> int:
    """Tabulation"""
    d = [[0 for _ in range(len(text1)+1)] for __ in range(len(text2)+1)]

    for i in range(1, len(text2)+1):
        for j in range(1, len(text1)+1):
            if text1[j-1] == text2[i-1]:
                d[i][j] = 1 + d[i-1][j-1]
            else:
                d[i][j] = max(d[i-1][j], d[i][j-1])
    return d[len(text2)][len(text1)]


def longestCommonSubsequence(text1: str, text2: str) -> int:
    """A little space optimized"""
    b = text1
    s = text2
    if len(text1) < len(text2):
        b, s = text2, text1

    prev = [0] * (len(b) + 1)
    cur = [0] * (len(b) + 1)

    for i in range(1, len(s)+1):
        for j in range(1, len(b)+1):
            if b[j-1] == s[i-1]:
                cur[j] = 1 + prev[j-1]
            else:
                cur[j] = max(prev[j], cur[j-1])
        prev, cur = cur, prev
    return prev[len(b)]
