class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D_queue = deque()
        R_queue = deque()

        num_senators = len(senate)
        for i, senator in enumerate(senate):
            if senator == "D":
                D_queue.append(i)
            else:
                R_queue.append(i)

        while D_queue and R_queue:
            current_D_senator_ind = D_queue.popleft()
            current_R_senator_ind = R_queue.popleft()

            # Whoever came first in the queue gets to ban the other & move on to next round
            if current_D_senator_ind < current_R_senator_ind:
                D_queue.append(current_D_senator_ind + num_senators)
            else:
                R_queue.append(current_R_senator_ind + num_senators)
            
        return "Dire" if D_queue else "Radiant"

# Analysis: O(n) where n = len(senate)



