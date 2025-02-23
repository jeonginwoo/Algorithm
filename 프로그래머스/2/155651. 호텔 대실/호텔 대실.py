import heapq

def solution(book_time):
    def h_to_m(time:str):
        h, m = time.split(":")
        return int(h)*60 + int(m)
    book_time = [[h_to_m(time[0]), h_to_m(time[1])+10] for time in book_time]
    book_time.sort()
    print(book_time)
    heap = []
    answer = 0
    for start, end in book_time:
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
        answer = max(answer, len(heap))
        
    return answer