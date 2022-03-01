def script(check, x, y):
    if check('level') == 1:
        if check("gold", x, y):
            return "take"
        if  check("gold", x , y + 1):
            return "down"
        elif check("gold", x  + 1, y):
            return "right"
        elif check("gold", x, y - 1):
            return "up"
        elif check("gold", x -  1, y):
            return "left"
        elif check("wall", x + 1, y) != 1:
            return "right"
        elif check("wall", x , y + 1) != 1:
            return "down"
    elif check('level') == 2:
        if check("gold", x, y):
            return "take"
        if  check("gold", x , y + 1):
            return "down"
        elif check("gold", x  + 1, y):
            return "right"
        elif check("gold", x, y - 1):
            return "up"
        elif check("gold", x -  1, y):
            return "left"
        elif check("wall", x + 1, y) != 1:
            return "right"
        elif check("wall", x , y - 1) != 1:
            return "up"
    elif check('level') == 3:
        if check("gold", x, y):
            return "take"
        if check("wall", x, y + 1) == 1 and check("wall", x - 1, y) != 1:
            return "left"
        elif check("wall", x - 1, y) == 1 and check("wall", x, y - 1) != 1:
            return "up"
        elif check("wall", x , y - 1) == 1 and check("wall", x + 1, y) != 1:
            return "right";
        elif check("wall", x + 1 , y) == 1 and check("wall", x, y + 1) != 1:
            return "down";
        if check("wall", x - 1, y - 1) == 1:
            return "up"
        elif check("wall", x + 1, y - 1) == 1:
            return "right"
        elif check("wall", x + 1, y + 1) == 1:
            return "down"
        elif check("wall", x - 1, y + 1) == 1:
            return "left"
    elif check('level') == 4:
        if check("gold", x, y):
            return "take"
        if check("wall", x - 1, y) == 1 and check("wall", x + 2, y) == 1 and (check("wall", x - 2, y) != 1):
            return "right"
        elif check("wall", x + 1, y + 1) == 1 and check("wall", x - 1, y) != 1 and (check("wall", x - 2, y) == 1) and check("wall", x + 1, y) != 1:
            return "left"
        elif check("wall", x, y + 1) == 1 and check("wall", x - 1, y) != 1:
            return "left"
        elif check("wall", x - 1, y) == 1 and check("wall", x, y - 1) != 1:
            return "up"
        elif check("wall", x , y - 1) == 1 and check("wall", x + 1, y) != 1:
            return "right";
        elif check("wall", x + 1 , y) == 1 and check("wall", x, y + 1) != 1:
            return "down";
        if check("wall", x - 1, y - 1) == 1:
            return "up"
        elif check("wall", x + 1, y - 1) == 1:
            return "right"
        elif check("wall", x + 1, y + 1) == 1:
            return "down"
        elif check("wall", x - 1, y + 1) == 1:
            return "left"

    return "pass"
