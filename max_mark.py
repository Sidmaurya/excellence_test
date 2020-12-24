def max_marks(sam_dict):
    val=max(sam_dict)

    
    return {val:sam_dict[val]}


sam_dict={
   "1" : 50,
   "2" : 60,
   "3" : 70
}

res_dict=max_marks(sam_dict)
print(res_dict)