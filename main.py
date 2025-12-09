import random

def randomize(student_list: list[str]) -> list[int]:
    acc = []
    sl = student_list

    while len(sl) > 0:
        rnd = random.randint(0, len(sl)-1)
        selection = sl[rnd]
        if selection in acc:
            continue
        else:
            acc.append(selection)
            sl.remove(selection)
    # print(acc)
    return acc

def initialize(n_nodes: int) -> dict[int, list[str]]:
    ordered_preferences = {}
    for i in range(0, n_nodes):
        data = randomize("A,B,C,D,E".split(','))
        ordered_preferences[i] = data
    return ordered_preferences

if __name__ == '__main__':
    states = initialize(3)
    for pair in zip(states.keys(), states.values()):
        print(pair)
