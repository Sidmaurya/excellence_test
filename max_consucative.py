def max_consecutive(sam_lst):
    lst_str=list(map(str,lst))
    return len(max("".join(lst_str).split('0')))
    
#lst=[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
lst=map(int,input("enter 0s and 1s").split(' '))
max_consecutive(lst)