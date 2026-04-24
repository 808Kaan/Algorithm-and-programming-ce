
def merge(u_list):

    if len(u_list)<=1:
        return u_list[:]


    middle_index = len (u_list) // 2
    left_list = u_list[:middle_index]
    right_list = u_list[middle_index:]

    sorted_left = merge(left_list)
    sorted_right = merge(right_list)


    return merge_sort (sorted_left , sorted_right)

    pass


def merge_sort(sorted_left,sorted_right):

    
    right_index = 0 
    left_index = 0

    merged_list = []
    
    while left_index < len(sorted_left) and right_index < len(sorted_right):
        if sorted_left [left_index] <= sorted_right[right_index]:
            merged_list.append(sorted_left [left_index])
            left_index+=1
        else:
            merged_list.append(sorted_right [right_index])
            right_index+=1
    
    merged_list.extend(sorted_left[left_index:])
    merged_list.extend(sorted_right[right_index:])
    return merged_list



if __name__ == "__main__":
    my_list = [1,3,2,7,4,12,11]
    pass



print (merge(my_list))
