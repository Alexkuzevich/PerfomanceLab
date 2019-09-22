import sys

input_file = sys.argv[1]
fl = open(input_file, 'r')
number_list = [int(line.strip()) for line in fl]

# def read_file(*args):
#     fl = open(args[1], 'r')
#     number_list = [int(line.strip()) for line in fl]

def find_percentile(lst):
    lst = sorted(lst)
    # for i in range(len(lst)):
    #     if i == len(lst)/0.9:
    #         percentile = lst[i]
    percentile = 90 * len(lst) / 100 - 1
    res = lst[int(percentile)]
    print("%.2f" % res)

def find_median(lst):
    lst = sorted(lst)
    if len(lst) % 2 == 0:
        print("%.2f" % lst[int(len(lst)/2)])
    else:
        print("%.2f" % lst[int(len(lst)/2+1)])

def find_max(lst):
    max_element = lst[0]
    for i in range(len(lst)):
        if lst[i] > max_element:
            max_element = lst[i]
    print("%.2f" % max_element)

def find_min(lst):
    min_element = lst[0]
    for i in range(len(lst)):
        if lst[i] < min_element:
            min_element = lst[i]
    print("%.2f" % min_element)

def find_average(lst):
    average = 0
    for i in range(len(lst)):
        average = average + int(lst[i])
    average /= len(lst)
    print("%.2f" % average)

find_percentile(number_list)
find_median(number_list)
find_max(number_list)
find_min(number_list)
find_average(number_list)

# fl.close()