class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for client in accounts:
            new_max = 0
            for money_in_bank in client:
                new_max += money_in_bank
            if new_max > max:
                max = new_max
        return max
