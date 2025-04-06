from collections import deque

def solution(plans):
    def h_to_m(time: str) -> int:
        h, m = map(int, time.split(":"))
        return h * 60 + m

    plans = [[plan[0], h_to_m(plan[1]), int(plan[2])] for plan in plans]
    plans.sort(key=lambda x: x[1])
    plans = deque(plans)
    answer = []

    wating = deque()
    running = plans.popleft()
    time = running[1]

    while plans:
        end_time = time + running[2]
        next_time = plans[0][1]

        if end_time > next_time:
            running[2] = end_time - next_time
            wating.append(running)
            running = plans.popleft()
            time = running[1]
        else:
            time = end_time
            answer.append(running[0])

            gap = next_time - time
            while wating and gap > 0:
                wait_task = wating.pop()
                if wait_task[2] <= gap:
                    time += wait_task[2]
                    gap -= wait_task[2]
                    answer.append(wait_task[0])
                else:
                    wait_task[2] -= gap
                    time = next_time
                    wating.append(wait_task)
                    break

            running = plans.popleft()
            time = running[1]

    answer.append(running[0])
    while wating:
        answer.append(wating.pop()[0])

    return answer
