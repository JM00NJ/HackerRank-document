if __name__ == '__main__':
    n = int(input())
    list_1 = []
    while n != 0:
        list_1.append(str(n))
        n = n-1
        if n == 0:
            list_1.reverse()
            print(''.join(list_1))
        else:
            None