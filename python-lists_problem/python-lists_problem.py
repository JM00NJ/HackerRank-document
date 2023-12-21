if __name__ == '__main__':
    N = int(input())
    z = list()
    while N != 0:
        x = list(map(str, input().split()))
        N = N-1
        if x[0] == "print":
            print(z)
        elif x[0] == "insert":
            z.insert(int(x[1]),int(x[2]))
        elif x[0] == "remove":
            z.remove(int(x[1]))
        elif x[0] == "append":
            z.append(int(x[1]))
        elif x[0] == "sort":
            z.sort()
        elif x[0] == "pop":
            z.pop(-1)
        elif x[0] == "reverse":
            z.reverse()