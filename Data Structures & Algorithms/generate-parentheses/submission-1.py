class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(cur,opened,close):
            if opened == n and close == n:
                res.append(cur)
                return 
            if opened < n:
                dfs(cur+"(",opened+1,close)
            if close< opened:
                dfs(cur+")",opened,close+1)
        dfs("",0,0)
        return res