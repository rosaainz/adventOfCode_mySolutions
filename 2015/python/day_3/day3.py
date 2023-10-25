
def deliver(directions):
    santa_x ,santa_y, robo_x, robo_y = 0,0, 0,0  #start
    visit = {(santa_x,santa_y)} #houses visited

    for i, direction in enumerate(directions):
        if i % 2  == 0: # santa turn
            if direction == '^':
                santa_y += 1
            elif direction == 'v':
                santa_y -= 1
            elif direction == '>':
                santa_x += 1
            elif direction == '<':
                santa_x -= 1
            visit.add((santa_x,santa_y))
        else:  # robo santa turn
            if direction == '^':
                robo_y += 1
            elif direction == 'v':
                robo_y -= 1
            elif direction == '>':
                robo_x += 1
            elif direction == '<':
                robo_x -= 1
            visit.add((robo_x, robo_y))

    return len(visit)


with open('input.txt', 'r') as file:
    content = file.read()
total = deliver(content)
print(total)
