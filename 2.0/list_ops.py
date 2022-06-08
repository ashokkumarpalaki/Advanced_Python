def list_ops(lst=[],dummy=[]):
    lis = lst
    print(lis)
    dummy=dummy
    if lis:
        for i in lis:
            count=0
            if i>=15:
                dummy.append(i)
                lis.remove(i)
                count+=1
            for j in lis:
                if i+j == 15:
                    print(i,j)
                    lis.remove(i)
                    lis.remove(j)
                    count+=1
            if count<1:
                dummy.append(i)
                lis.remove(i)
            list_ops(lis,dummy)
    else:
        print(lis)
        print(dummy)


if __name__ == '__main__':
    lst = [2, 4, 5, 6, 7, 8, 1, 12, 15, 3, 26, 9, 8, 13]
    dummy=[]
    print("initial:-",lst)
    list_ops(lst=list(set(lst)),dummy=dummy)
