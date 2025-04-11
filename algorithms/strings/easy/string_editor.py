
class Solution:
    """
    Implement a simple text editor. The editor initially contains an empty string, S. Perform Q operations of the following 4 types:
        1. append(W) - Append string W to the end of S.
        2. delete(k) - Delete the last k characters of S.
        3. print(k) - Print the k-th character of S.
        4. undo - Undo the last (not previously undone) operation of type 1 or 2, reverting S to the state it was in prior to that operation.
    """

    # Analysis: time = O(n), space = O(n * m)
    # where n = number of operations and m = maximum length of string
    def processEditor():
        n_ops = int(input())
        s = ""
        history = []

        for _ in range(n_ops):
            op = input().split()

            if op[0] == "1":
                history.append(s)
                s += op[1]

            elif op[0] == "2":
                k = int(op[1])
                history.append(s)
                s = s[:-k]

            elif op[0] == "3":
                k = int(op[1])
                print(s[k - 1])

            elif op[0] == "4":
                if history:
                    s = history.pop()

if __name__ == "__main__":
    Solution.processEditor()
