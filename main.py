import random
from itertools import batched
from pprint import pprint


def randomize(student_list: list[int]) -> list[int]:
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

def swap(idx1: int, idx2: int, d: dict[int, list[str]]) -> dict[int, list[str]]:
    res = d
    keys = list(d.keys())

    first = keys[idx1]
    second = keys[idx2]

    res[first], res[second] = res[second], res[first]
    return res

def evalLoss(lookup: zip[tuple[str, int]]) -> int:

    for e in lookup:
        print(e)


    1

def initialize(n_nodes: int, n_preferences: int ) -> dict[int, list[str]]:
    ordered_preferences = {}
    for i in range(0, n_nodes):
        data = randomize(list(range(0, n_preferences)))
        ordered_preferences[i] = data
    return ordered_preferences

def partition(d: dict[int, list[str]], n_preferences: int) -> dict[tuple[int, int], list[str]]:
    res = {}
    partition_capacity = n_preferences
    current_partition = 0
    for i in d.keys():
        if i < partition_capacity:
            upd = {(i, current_partition): d[i]}
            res.update(upd)
        else:
            partition_capacity = partition_capacity + n_preferences
            current_partition = current_partition+1
            upd = {(i, current_partition): d[i]}
            res.update(upd)
    return res

if __name__ == '__main__':
    n_nodes, n_preferences = 20, 6
    states = initialize(n_nodes, n_preferences)
    partitioned = partition(states, n_preferences)

    square_values = [x * x for x in list(range(0,n_preferences - 1))]
    partitions = list(range(0, n_preferences - 1))

    loss_lookup = zip(partitions, square_values)
    for i in loss_lookup:
        print(i)

    idx1 = random.randint(0, len(states) - 1)
    idx2 = random.randint(0, len(states) - 1)

    #This will be the structure that will encode [nodeId, ranked preferences, and loss value to be minimized]
    results = zip(states.keys(), states.values(), range(0,n_nodes))
    # for pair in results:
    #     print(pair)

    swapped = swap(idx1, idx2, states)
    # k, v = swapped.keys(), swapped.values()
    swapped_results = zip(swapped.keys(), swapped.values())

    r = list(range(0, 5))
    print(r)
    data = randomize(list(range(0, 3)))

    res = partitioned
    pprint(res)




