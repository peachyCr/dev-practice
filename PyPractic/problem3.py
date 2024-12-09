n, r = [int(item) for item in input().split()]
distantion = [int(item) for item in input().split()]

def cnt_date_places(r, distantion):
    cnt = 0
    last = 1
    for first in range(len(distantion)):
        while ((last < len(distantion)) and (distantion[last] - distantion[first] <= r)):
            last += 1
        cnt += len(distantion) - last
    return cnt

print(cnt_date_places(r, distantion))
