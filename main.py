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

def swap(idx1: int, idx2: int, d: dict[int, list[str]]) -> dict[int, list[str]]:
    res = d
    keys = list(d.keys())

    first = keys[idx1]
    second = keys[idx2]

    res[first], res[second] = res[second], res[first]
    return res

if __name__ == '__main__':
    states = initialize(3)

    idx1 = random.randint(0, len(states) - 1)
    idx2 = random.randint(0, len(states) - 1)

    results = zip(states.keys(), states.values())
    for pair in results:
        print(pair)

    swapped = swap(idx1, idx2, states)
    # k, v = swapped.keys(), swapped.values()
    swapped_results = zip(swapped.keys(), swapped.values())

    print(f'\nSwapping idx1: {idx1}, idx2: {idx2}')
    for pair in swapped_results:
        print(pair)

    print()



