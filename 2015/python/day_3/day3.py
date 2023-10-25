
def deliver(directions):
    x,y = 0,0  #start
    visit = {(x,y)} #houses visited

    for i in directions:
        if i == '^':
            y += 1
        elif i == 'v':
            y -= 1
        elif i == '>':
            x += 1
        elif i == '<':
            x -= 1
        visit.add((x,y))
    return len(visit)




with open('input.txt', 'r') as file:
    content = file.read()
total = deliver(content)
print(total)
