import json

MINIMUM_NUMBER = 2
NUM_RANGE = 1000
results_dict = {}


def collatz(start_int):
    nums = [start_int]
    while nums[-1] != 1:
        if nums[-1] % 2 == 0:
            new_num = int((nums[-1] / 2))
            nums.append(new_num)
        else:
            new_num = (nums[-1] * 3) + 1
            nums.append(new_num)
    return nums


for i in range(MINIMUM_NUMBER, NUM_RANGE):
    number_list = collatz(i)
    results_dict[i] = {
        'list': number_list,
        'length': len(number_list),
        'maximum': max(number_list),
    }

with open('data.json', 'w') as f:
    json.dump(results_dict, f)
