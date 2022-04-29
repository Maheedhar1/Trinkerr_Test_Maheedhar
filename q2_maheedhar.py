def keygroup(key_list):
    group_list = {}
    
    for key in key_list:
        a = ''.join(sorted(key))
        anagrams = group_list.get((a),[])
        anagrams.append(key)
        group_list[a] = anagrams
    return list(group_list.values())    
    
    
if __name__ == "__main__":
    keys = ["idea", "idae", "bsnl", "nsbl", "grasim", "bata"]
    print(keygroup(keys))