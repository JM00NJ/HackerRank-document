def score(n: int,arr: map):
    list_1 = list(arr)
    m = int(max(list_1))
    z = m-1
    if z in list_1:
        print(z)
    while z not in list_1:
        z = z-1
        if z in list_1:
            print(z)



if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score(n=n,arr=arr)