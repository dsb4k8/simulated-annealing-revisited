import math
import random
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

def swap(index1: int, index2: int, d: dict[int, list[int]]) -> dict[int, list[int]]:
    res = d
    keys = list(d.keys())

    first = keys[index1]
    second = keys[index2]

    res[first], res[second] = res[second], res[first]
    return res

def initialize(n_node: int, n_preference: int ) -> dict[int, list[int]]:
    ordered_preferences = {}
    for i in range(0, n_node):
        data = randomize(list(range(0, n_preference)))
        ordered_preferences[i] = data
    return ordered_preferences

def partition(d: dict[int, list[int]], n_preference: int) -> dict[tuple[int, int], list[int]]:
    res = {}
    base_capacity = int(len(d.keys())) / n_preference
    partition_capacity = base_capacity
    current_partition = 0
    for i in d.keys():
        if i <= partition_capacity:
            upd = {(i, current_partition): d[i]}
            res.update(upd)
        else:
            partition_capacity = partition_capacity + base_capacity
            current_partition = current_partition+1
            upd = {(i, current_partition): d[i]}
            res.update(upd)
    return res

def initialize_loss(d: dict[tuple[int, int], list[int]]) -> dict[tuple[int, int], tuple[list[int], float]]:
    res = {}
    for i in d.keys():
        loss = get_loss(i, d[i])
        update = {i:(d[i], loss)}
        res.update(update)
    return res

def get_loss(id: tuple[int, int], ranked_prefs: list[int]) -> float:
    return math.pow(ranked_prefs.index(id[1]), 2)


if __name__ == '__main__':
    n_nodes, n_preferences = 21, 6
    states_init = initialize(n_nodes, n_preferences)
    states_partitioned = partition(states_init, n_preferences)
    states = initialize_loss(states_partitioned)



    square_values = [x * x for x in list(range(0,n_preferences - 1))]
    # partitions = list(range(0, n_preferences - 1))

    # loss_lookup = zip(partitions, square_values)
    # for i in loss_lookup:
    #     print(i)

    idx1 = random.randint(0, len(states) - 1)
    idx2 = random.randint(0, len(states) - 1)

    #This will be the structure that will encode [nodeId, ranked preferences, and loss value to be minimized]
    results = zip(states.keys(), states.values(), range(0,n_nodes))
    # for pair in results:
    #     print(pair)

    swapped = swap(idx1, idx2, states_init)
    # k, v = swapped.keys(), swapped.values()
    swapped_results = zip(swapped.keys(), swapped.values())

    r = list(range(0, 5))
    # print(r)
    data = randomize(list(range(0, 3)))

    # filter results, removing overflow instances.
    # This is for the sake of convenience -for example, if this program is used to find
    # the most egalitarian assignment of students to professors given student's ranked preferences,
    # this ensures
    # res = {
    #     key: value for key, value in states_partitioned.items() if key[1] <= (n_preferences - 1)
    # }

    res = states
    pprint(res)




