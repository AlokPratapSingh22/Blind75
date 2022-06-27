"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
"""


def numDecodings(s: str) -> int:
    """Bruteforce"""

    if len(s) > 0 and s[0] == '0':
        return 0

    if len(s) <= 1:
        return 1

    if int(s[0:2]) <= 26:
        return self.numDecodings(s[2:])+self.numDecodings(s[1:])

    return self.numDecodings(s[1:])


def numDecodings(s: str, memo={}) -> int:
    """Memoized"""
    if len(s) > 0 and s[0] == '0':
        return 0

    if len(s) <= 1:
        return 1

    if s in memo:
        return memo[s]

    if int(s[0:2]) <= 26:
        memo[s] = self.numDecodings(s[2:], memo)+self.numDecodings(s[1:], memo)
        return memo[s]

    memo[s] = self.numDecodings(s[1:], memo)
    return memo[s]


def numDecodings(s: str) -> int:
    """Tabulation"""
    if len(s) > 0 and s[0] == '0':
        return 0

    if len(s) <= 1:
        return 1

    dp = [0 for _ in range(len(s)+1)]
    dp[0] = 1
    dp[1] = 1

    for i in range(1, len(s)):
        curr = int(s[i])
        prev = int(s[i - 1])

        # can't make progress, return 0
        if (prev == 0 and curr == 0 or (curr == 0 and (prev * 10 + curr > 26))):
            return 0
            # can't use the previous value, so can only get to this state from the previous
        elif (prev == 0 or (prev * 10 + curr) > 26):
            dp[i + 1] = dp[i]

        # can't use current state, can only get to this state from i - 1 state
        elif (curr == 0):
            dp[i + 1] = dp[i - 1]

        # can get to this state from the previous two states
        else:
            dp[i + 1] = dp[i] + dp[i - 1]

    return dp[len(s)]
