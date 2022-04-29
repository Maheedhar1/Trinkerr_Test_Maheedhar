def optimalways(colour_arr):
 

    c = 0
 
    colour_arr.sort()
    i = 0
    while i < (len(colour_arr)-1):

        if (colour_arr[i] == colour_arr[i + 1]):
            c += 1
 
    
            i = i + 2

        else:
            i += 1
 
    return c
 

if __name__ == "__main__":
 
    colour_list = [1,2,3,1,2]
    print(optimalways(colour_list ))