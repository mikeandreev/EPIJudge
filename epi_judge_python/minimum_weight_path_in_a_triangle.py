from test_framework import generic_test

# v1 DONE
# v2 DONE

def minimum_path_weight_v1(triangle):
    if len(triangle) == 0:
    	return 0
    cache = []
    for r in triangle:
    	cache.append(list(r))
    for i in reversed(range(len(cache)-1)):
    	for j in range(len(cache[i])):
    		cache[i][j] += min(cache[i+1][j], cache[i+1][j+1])
    return cache[0][0]
    
    
def minimum_path_weight_v2(triangle):
    if len(triangle) == 0:
    	return 0
    cache = list(triangle[-1])
    
    for i in reversed(range(len(triangle)-1)):
    	for j in range(len(triangle[i])):
    		cache[j] = triangle[i][j] + min(cache[j], cache[j+1])
    return cache[0]


def minimum_path_weight(triangle):
	return minimum_path_weight_v2(triangle)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_weight_path_in_a_triangle.py",
                                       'minimum_weight_path_in_a_triangle.tsv',
                                       minimum_path_weight))
