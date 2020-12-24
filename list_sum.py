def list_sum(my_lst):
    return sum(my_lst)

#my_lst=[3,5,7,3,2,6]
my_lst=map(int,input().split(' '))
res_sum=list_sum(my_lst)
print(res_sum)