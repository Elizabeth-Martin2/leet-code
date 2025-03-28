class Bank:
    def __init__(self, balance: list[int]):
        # Prepend dummy 0 to support 1-based account indexing
        self.balance = [0] + balance[:]

    def _valid_account(self, account: int) -> bool:
        return 1 <= account < len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._valid_account(account1) or not self._valid_account(account2):
            return False
        if money < 0 or self.balance[account1] < money:
            return False

        self.balance[account1] -= money
        self.balance[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._valid_account(account) or money < 0:
            return False

        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._valid_account(account) or money < 0 or self.balance[account] < money:
            return False

        self.balance[account] -= money
        return True

    

if __name__ == "__main__":
    commands = ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
    args = [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
    expected = [None, True, True, True, False, False]

    obj = None
    output = []

    for command, arg in zip(commands, args):
        if command == "Bank":
            obj = Bank(*arg)
            output.append(None)
        elif command == "deposit":
            result = obj.deposit(*arg)
            output.append(result)
        elif command == "withdraw":
            result = obj.withdraw(*arg)
            output.append(result)
        elif command == "transfer":
            result = obj.transfer(*arg)
            output.append(result)
        else:
            raise ValueError(f"Unknown command: {command}")

    assert output == expected, f"Failed. Output: {output}, Expected: {expected}"
    print("All tests passed!")

