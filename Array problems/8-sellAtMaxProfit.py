def max_sell(values):

    # all array checks 

    global_small = values[0]
    global_profit = 0   # system min value

    for value in values:

        # global_small = min(global_small, value) 
        if global_small < value: 
            global_small=global_small 
        else:
            global_small = value

        current_profit = value - global_small

        # global_profit = max(global_profit, current_profit)
        if global_profit > current_profit: 
            global_profit=global_profit 
        else:
            global_profit = current_profit
    
    return global_profit

arr = [8,9,5,6,13,10,11]
print(max_sell(arr))