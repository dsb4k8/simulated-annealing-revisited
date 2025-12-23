import datetime
import random
from math import exp
from math import pow
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

def swap(index1: int, index2: int, d: dict[tuple[int, int], tuple[list[int], float]]) -> dict[tuple[int, int], tuple[list[int], float]]:
    res = d
    keys = list(d.keys())

    first = keys[index1]
    second = keys[index2]

    res[first], res[second] = res[second], res[first]
    res = initialize_loss(res)
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

def initialize_loss(d: dict[tuple[int, int], tuple[list[int], float]]) -> dict[tuple[int, int], tuple[list[int], float]]:
    res = {}
    # for r in d:
    #
    #
    for k,v in zip(d.keys(),d.values(), strict=True):
        ns = k[1]
        lst = v
        if ns in lst:
            loss_update = get_loss(k, v)
            update = {k:(v, loss_update)}
            res.update(update)
    return res

def get_loss(id: tuple[int, int], prefs_ranked: tuple[list[int], float]) -> float:
    r_prefs = prefs_ranked
    print(f"{r_prefs}, {id[1]}")
    base = r_prefs.index(id[1])
    return pow(base, 2)

def prob_swap(newv: float, currentv: float,  temp: float) -> float:
    delta = newv - currentv
    return 1.0 - (1.0/(1.0+exp(delta/temp)))

def update_temp(temp: float, factor: float) -> float:
    return temp * factor


def calculate_average_of_floats(data_dict: dict[tuple[int, int], tuple[list[int], float]]) -> float:
    total_sum = 0.0
    count = 0

    for value_tuple in data_dict.values():
        float_value = value_tuple[1]
        total_sum += float_value
        count += 1

    # Avoid division by zero
    if count == 0:
        return 0.0

    return total_sum / count


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

    # swapped = swap(idx1, idx2, states)
    # # k, v = swapped.keys(), swapped.values()
    # swapped_results = zip(swapped.keys(), swapped.values())

    # r = list(range(0, 5))
    # # print(r)
    # data = randomize(list(range(0, 3)))

    # filter results, removing overflow instances.
    # This is for the sake of convenience -for example, if this program is used to find
    # the most egalitarian assignment of students to professors given student's ranked preferences,
    # this ensures... nevermind not needed
    # res = {
    #     key: value for key, value in states_partitioned.items() if key[1] <= (n_preferences - 1)
    # }

    res = states
    vals = states.values()
    loss = list(vals.mapping.values())
    l: list[float] = []
    l: list[float] = []
    for i in vals:
        n = i[1]
        l.append(n)
    s = sum(l)

    # print(f"{'Sum' :<24}{'Loss' :<24}")
    # print(f"{s :<24}{s/n_nodes :<24}")

    #where ever you want to write your output to
    outpath = ""
    c = 0

    now = datetime.datetime.now()
    formatted_date = now.strftime('%a, %d %b %Y, %I:%M:%S %p')
    # 1.47 was the record achieved loss
    # new record: 151655 1.0476190476190477

    #LOGGING START
    # with open(f"{outpath}simulated_annealing_output_{formatted_date}", "w") as file:
    #     while(s/n_nodes > 1.6):
    #         #setup
    #         states_init = initialize(n_nodes, n_preferences)
    #         states_partitioned = partition(states_init, n_preferences)
    #         states = initialize_loss(states_partitioned)
    #         res = states
    #         vals = states.values()
    #         loss = list(vals.mapping.values())
    #         l: list[float] = []
    #         for i in vals:
    #             n = i[1]
    #             l.append(n)
    #         s = sum(l)
    #         c += 1
    #         print(c, s/n_nodes )
    #         continue
    #     file.write(f"{'Id' :<6}{'Partition #' :<15}{'Preferences' :<22}{'Loss' :<24}\n")
    #     for rec in zip(states.keys(), states.values()):
    #         file.write(f"{rec[0][0] :<6}{rec[0][1] :<15}{str(rec[1][0]) :<22}{rec[1][1] :<24}\n")
    #
    #     file.write(f"{'Sum' :<24}{'Loss' :<24}\n")
    #     file.write(f"{s :<24}{s / n_nodes :<24}")
        # LOGGING END

#START LOGGING
    res_collection = []
    for i in range(0, 2):
        states_init = initialize(n_nodes, n_preferences)
        states_partitioned = partition(states_init, n_preferences)
        states = initialize_loss(states_partitioned)
        res = states
        vals = states.values()
        loss = list(vals.mapping.values())
        l: list[float] = []
        for i in vals:
            n = i[1]
            l.append(n)
        s = sum(l)
        loss_delta = s / n_nodes
        res_collection.append(loss_delta)
        res_collection.append(loss_delta)
    loss_delta = s / n_nodes
    print(f"{'Sum' :<24}{'Loss' :<24}{'Probability of Acceptance' :<24}{'Temperature' :<24}\n")

    temp = 100.0
    while(temp > 0.1):
        print(f"{s :<24}{loss_delta :<24}{prob_swap(res_collection[1], res_collection[0], temp) :<24}{temp:<24}")
        temp = update_temp(temp, 0.95 )
        # print(f"\n {prob_swap(res_collection[1], res_collection[0], temp)}")
    print(f"new: {res_collection[0]}\ncurrent:   {res_collection[1]}")
#END LOGGING

    temp = 100.0
    while temp > 0.1:
        print(f"{s :<24}{loss_delta :<24}{prob_swap(res_collection[1], res_collection[0], temp) :<24}{temp:<24}")
        temp = update_temp(temp, 0.95)
        r1 = random.randint(0, len(states)-1)
        r2 = random.randint(0, len(states)-1)

        curr_loss = calculate_average_of_floats(states)
        switched = swap(r1, r2, states)
        # states = initialize_loss(states)
        # prop_loss = swap(r1, r2, res)
        # probability_of_swap = prob_swap()
        #










    pprint(states)
    print("\n")
    pprint(res)

    print(states.__eq__(res))






