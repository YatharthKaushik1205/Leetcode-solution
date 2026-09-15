class Solution(object):
    def maximumWealth(self, accounts):
        wealth = 0
        for i in range(0,len(accounts),1):
            temp_wealth = 0
            for j in range(0,len(accounts[i]),1):
                temp_wealth+=accounts[i][j]
            if(wealth<=temp_wealth):
                wealth = temp_wealth
        return wealth