def solution(answers):
    answer = []
    fir = [1, 2, 3, 4, 5]
    sec = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == fir[i%len(fir)]:
            cnt[0] += 1
        if answers[i] == sec[i%len(sec)]:
            cnt[1] += 1
        if answers[i] == thr[i%len(thr)]:
            cnt[2] += 1

    for i in range(len(cnt)):
        if cnt[i] == max(cnt):
            answer.append(i+1)
    return answer
