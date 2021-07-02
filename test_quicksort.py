from quicksort import quicksort
from copy import deepcopy
from random import randint, seed

def test_quicksort():
    
    seed(0)

    random_arrays = [[randint(-10,10) for _ in range(10)] for _ in range(10)]

    for a in random_arrays:
        a_copy = deepcopy(a)
        quicksort(a_copy)
        assert(a_copy == sorted(a))