import random
from sort_algorythms import quicksort

any_list = random.sample(range(1, 1000), 42)
sorted_list = [i for i in range(1, 43)]
reversed_list = list(reversed(range(1, 43)))
repeated_list = random.choices(range(1, 101), k=39) + [random.choice(range(1, 101)) for x in range(3)]


if __name__ == "__main__":
    test_cases = {'Random numbers': any_list,
                  'Already sorted': sorted_list,
                  'Reversed': reversed_list,
                  'Repeated items': repeated_list
                  }

    print('------------------------------------------------------')
    for case, list in test_cases.items():
        print("\nTest Case: {}".format(case))
        print(list)
        quicksort(list)
        print("\nSorted:")
        print(list)
        print('\n------------------------------------------------------')
    print('------------------------------------------------------')
