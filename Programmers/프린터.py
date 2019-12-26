from collections import deque


def solution(priorities, location):
    answer = 0

    # make deque
    q = deque([(idx, priority) for idx, priority in enumerate(priorities)])

    while q:
        job_idx, job_priority = q.popleft()

        delayed = False
        for idx, priority in q:
            # if current job is delayed
            if job_priority < priority:
                q.append((job_idx, job_priority))
                delayed = True
                break

        # don't count if the job is delayed
        if delayed:
            continue
        # add count printed
        answer += 1

        # if found the job
        if job_idx == location:
            break

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
