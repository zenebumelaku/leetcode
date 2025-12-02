

class Solution:
    def timeRequiredToBuy(self, tickets,k):
        c = 0
        while tickets[k] != 0:
            c += 1

            if tickets[0] == 1:
                tickets.pop(0)
                if k == 0:
                    return c
                else:
                    k -= 1
            else:
                tickets.append(tickets[0] - 1)
                tickets.pop(0)
                if k == 0:
                    k = len(tickets) - 1
                else:
                    k -= 1

        return c
