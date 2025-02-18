def collideAsteroids(remaining_ast: List[int]):
    if len(remaining_ast) > 1:
        current_ast = remaining_ast.pop()
        last_ast = remaining_ast[-1]

        if current_ast < 0 and last_ast > 0:
            rem_ast = remaining_ast.pop()
            if abs(rem_ast) > abs(current_ast):
                remaining_ast.append(rem_ast)
            elif abs(rem_ast) < abs(current_ast):
                remaining_ast.append(current_ast)

            collideAsteroids(remaining_ast)
        else:
            remaining_ast.append(current_ast)


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        positive = True if asteroids[0] >= 0 else False
        res = []

        for asteroid in asteroids:
            res.append(asteroid)
            collideAsteroids(res)

        return res
