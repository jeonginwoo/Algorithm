from itertools import permutations

def solution(user_id, banned_id):

    def is_match(banned, user):
        if len(banned) != len(user):
            return False
        for b, u in zip(banned, user):
            if b != '*' and b != u:
                return False
        return True

    possible_sets = set()

    for perm in permutations(user_id, len(banned_id)):
        if all(is_match(b, u) for b, u in zip(banned_id, perm)):
            possible_sets.add(frozenset(perm))

    return len(possible_sets)
