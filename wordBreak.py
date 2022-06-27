def wordBreak(s: str, wordDict: list[word]) -> bool:
    """Memoized"""
    memo = {}
    def helper(s, wordDict, memo):
        if s in memo:
            return memo[s]
        if s == '':
            return True

        for word in wordDict:            
            if s.find(word) == 0:
                if helper(s.removeprefix(word), wordDict, memo):
                    memo[s] = True
                    return True

        memo[s] = False
        return False
    ans = helper(s, wordDict, memo)
    memo = None
    return ans

def wordBreak(target: str, wordDict:list[word]) -> bool:
    """Taabulation"""
    dp = [False for _ in range(len(s)+1)]
    dp[0] = True
    
    for i in range(len(s)+1):
        if dp[i] == False:
            continue
        for word in wordDict:
            if s[i:i+len(word)] == word:
                dp[i+len(word)] = True
    return dp[len(s)]
    