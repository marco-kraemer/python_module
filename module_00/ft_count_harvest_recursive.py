def recurse(x, i):
    if (i <= x):
        print("Day", i)
        i += 1
        recurse(x, i)
    else:
        print("Harvest time!")


def ft_count_harvest_recursive():
    x = int(input("Days until harvest: "))
    recurse(x, 1)
