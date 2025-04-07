class Solution: 
    """
    Two players are playing a game of Tower Breakers! Player  always moves first, and both players always play optimally.The rules of the game are as follows:

    Initially there are n towers.
    Each tower is of height m.
    The players move in alternating turns.
    In each turn, a player can choose a tower of height x and reduce its height to y, where 1 <= y < x and y evenly divides x.
    If the current player is unable to make a move, they lose the game.
    Given the values of n and m, determine which player will win. If the first player wins, return 1. Otherwise, return 2.
    """

    # Analysis: time = O(1), space = O(1)
    def towerBreakers(self, n: int, m:int) -> int:
        # Key insight (AKA dirty trick):
        # If the towers height start at 1, there are no moves for player 1, and player 2 wins
        # If the number of towers is even, player 2 can mimic player 1's moves and win
        # Else, player 1 can stay ahead of player 2 and win

        if m == 1:
            return 2

        if n % 2 == 0:
            return 2
        else:
            return 1

if __name__ == "__main__":
    solution = Solution()


    test_cases = [
        (2, 2, 2),
        (1, 4, 1),
        (4, 8, 2)
    ]

    for i, (n, m, expected) in enumerate(test_cases, 1):
        output = solution.towerBreakers(n, m)
        assert output == expected, f"Test case {i} failed, expected {expected}, got {output}"

    print("All test cases passed!")