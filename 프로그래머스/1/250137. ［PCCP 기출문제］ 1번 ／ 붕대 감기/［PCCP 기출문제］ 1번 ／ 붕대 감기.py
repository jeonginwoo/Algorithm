def solution(bandage, health, attacks):
    play_time = attacks[-1][0]
    attack_idx = 0
    answer = health
    heal_count = 0
    for time in range(1, play_time+1):
        if time == attacks[attack_idx][0]:
            answer -= attacks[attack_idx][1]
            if answer <= 0:
                return -1
            attack_idx += 1
            heal_count = 0
            continue
        
        heal_count += 1
        answer = min(answer+bandage[1], health)
        if heal_count == bandage[0]:
            answer = min(answer+bandage[2], health)
            heal_count = 0
    return answer