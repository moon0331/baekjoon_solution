from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_idx = 0
    n_finished = 0
    bridge = deque()
    t = 0
    present_weight = 0

    while True:
        t += 1

        # pop truck if available
        if len(bridge) == bridge_length:
            popval = bridge.popleft()
            if popval:
                present_weight -= popval
                n_finished += 1

        # push truck if avilable, else push zero
        if truck_idx < len(truck_weights) and present_weight + truck_weights[truck_idx] <= weight:
            next_truck = truck_weights[truck_idx]
            bridge.append(next_truck)
            present_weight += next_truck
            truck_idx += 1
        else:
            bridge.append(0)

        if n_finished == len(truck_weights):
            break

    return t

bls = [2, 100, 100]
weights = [10, 100, 100]
truck_weights = [[7,4,5,6], [10], [10,10,10,10,10,10,10,10,10,10]]
results = [8, 101, 110]

for b, w, t, r in zip(bls, weights, truck_weights, results):
    print(solution(b, w, t) == r)