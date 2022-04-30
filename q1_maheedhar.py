def optimalways(colour_arr):
 

    c = 0
    colour_count_dict ={}
    for i in colour_arr:
        if i in colour_count_dict.keys():
            colour_count_dict[i] = colour_count_dict[i] + 1
        else:
            colour_count_dict[i] = 1
    total_optimal_ways = 0
    for i in colour_count_dict.keys():
        k = colour_count_dict[i]
        if k >1:
            
            ways = k * (k-1)/2
            total_optimal_ways = total_optimal_ways + ways
    return int(total_optimal_ways)
    
if __name__ == "__main__":
 
    colour_list = [1,2,3,1,2]
    print(optimalways(colour_list ))