def initial_state():
    return (8, 0, 0)

def is_goal(s):
    if s[0]==4 and s[1]==4:
        return True
    else:
        return False

def successors(s):
    x, y, z = s

    # This solution list contains state of the three bottles and step cost (amount of poured water)
    solution = []

    # Since we can only pour from bottle_i to bottle_j until bottle_j is full or bottle_i is empty
    # (meanwhile the bottle_j must not overflow), we need to pour minimum amount between amount of
    # water in bottle_i and amount left in the bottle_j.

    # a >>> b
    if x > 0 and y < 5:
        pouredAmount = min(x, 5 - y)
        newState = (x - pouredAmount, y + pouredAmount, z)
        solution.append((newState, pouredAmount))

    # a >>> c
    if x > 0 and z < 3:
        pouredAmount = min(x, 3 - z)
        newState = (x - pouredAmount, y, z + pouredAmount)
        solution.append((newState, pouredAmount))

    # b >>> a
    if y > 0 and x < 8:
        pouredAmount = min(y, 8 - x)
        newState = (x + pouredAmount, y - pouredAmount, z)
        solution.append((newState, pouredAmount))

    # b >>> c
    if y > 0 and z < 3:
        pouredAmount = min(y, 3 - z)
        newState = (x, y - pouredAmount, z + pouredAmount)
        solution.append((newState, pouredAmount))

    # c >>> a
    if z > 0 and x < 8:
        pouredAmount = min(z, 8 - x)
        newState = (x + pouredAmount, y, z - pouredAmount)
        solution.append((newState, pouredAmount))

    # c >>> b
    if z > 0 and y < 5:
        pouredAmount = min(z, 5 - y)
        newState = (x, y + pouredAmount, z - pouredAmount)
        solution.append((newState, pouredAmount))

    return solution
