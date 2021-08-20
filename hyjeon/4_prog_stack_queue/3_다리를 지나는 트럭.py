def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    bridge_weight = 0
    while len(trucks_on_bridge):
        answer += 1
        bridge_weight -= trucks_on_bridge.pop(0)

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights[0])
                bridge_weight += truck_weights.pop(0)
            else:
                trucks_on_bridge.append(0)
    return answer
