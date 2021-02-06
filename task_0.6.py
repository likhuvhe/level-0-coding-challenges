def maximum(num1, num2, num3):
    num_lst = [num1, num2, num3]
    maxm = num1
    index = 1
    while   index < len(num_lst):
        if (num_lst[index] > maxm):
            maxm = num_lst[index]
        index +=1
    return maxm