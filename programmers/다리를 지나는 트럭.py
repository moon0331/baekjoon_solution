from collections import deque

def solution(bridge_length, weight, truck_weights):

    def available_to_finish(bridge, bridge_len):
        return len(bridge) == bridge_len

    def available_to_on(bridge, bridge_len, w, truck_weights):
        return len(bridge) < bridge_len and sum(bridge)+truck_weights[0] < w

    n_finished = 0
    n_truck = len(truck_weights)

    truck_weights = deque(truck_weights+[0]) # queue화
    bridge = deque(maxlen=bridge_length)
    
    
    t = 0
    while n_finished < n_truck:
        print('===================================')
        t += 1
        print(t)
        if available_to_finish(bridge, bridge_length):
            val = bridge.popleft()
            if val != 0:
                print(val, 'done')
                n_finished += 1
                if n_finished == n_truck:
                    break
        if available_to_on(bridge, bridge_length, weight, truck_weights):
            bridge.append(truck_weights.popleft())
            print(bridge[-1], 'on')
        else:
            bridge.append(0)

        print(t, bridge, truck_weights)

    return t

print(solution(2, 10, [7,4,5,6]) == 8)
print(solution(100, 100, [10]) == 101)
print(solution(100, 100, [10]*10) == 110)