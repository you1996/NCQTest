def solution(N,A):
    Counters=[0] * N
    print(Counters)
    for elment in A:
        if(elment<=N and elment>=1):
            Counters[elment-1]+=1
        else:
            maxi = max(Counters)
            Counters=[maxi] * N 
    return Counters
