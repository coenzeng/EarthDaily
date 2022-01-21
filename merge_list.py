def merge(original, add, delete):
    result = []
    delete_set = set()

    for s in delete:
        delete_set.add(s)
        
    result_hash = {}
    visited = set()

    for s in add:
        original.append(s)

    for s in original:
        if s not in delete_set and s not in visited:
            if len(s) in result_hash:
                result_hash[len(s)].append(s)
            else:
                result_hash[len(s)] = [s]
            visited.add(s)
  
    for key in sorted(result_hash, reverse=True):
        for s in result_hash[key]:
            result.append(s)
      
    return result
        

original = ['one', 'two', 'three']
add = ['one', 'two', 'five', 'six']
delete = ['two', 'five']
result = ['three', 'six', 'one']           

print(merge(original, add, delete))