from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for k in course:
        menu_list = []
        for order in orders:
            for menu in combinations(order, k):
                menu_list.append("".join(sorted(menu)))
        menu_list = Counter(menu_list).most_common()
        list = [menu for menu, count in menu_list if count > 1 and count == menu_list[0][1]]
        answer += [menu for menu, count in menu_list if count > 1 and count == menu_list[0][1]]
    return sorted(answer)