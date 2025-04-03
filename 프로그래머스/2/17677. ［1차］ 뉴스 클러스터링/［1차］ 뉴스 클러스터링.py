from collections import Counter

def solution(str1, str2):
    set1 = Counter([str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()])
    set2 = Counter([str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()])

    intersection = sum(min(set1[i], set2[i]) for i in set1 if i in set2)
    union = sum(max(set1[i], set2[i]) for i in set1 | set2)

    if union == 0:
        return 65536
    return int(intersection / union * 65536)
