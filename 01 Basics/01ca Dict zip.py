# https://www.youtube.com/watch?v=k2ZWyHdahEk
def dict_zip(*dicts):
    if not dicts:
        return

    n = len(dicts[0])   # number of items in the first dict
    if any(len(d) != n for d in dicts):  # check if all dicts have the same number of items
        raise ValueError("dict_zip: dicts must have same length")

    for key, first_val in dicts[0].items():  # iterate over the first dict
        yield key, first_val, *(other[key] for other in dicts[1:])


names = {"key1": "value1", "key2": "value2", "key3": "value3"}
other = {"key1": "valueOne", "key2": "valueTwo", "key3": "valueThree"}

for key, value, other_value in dict_zip(names, other):
    print(key, value, other_value)

# key1 value1 valueOne
# key2 value2 valueTwo
# key3 value3 valueThree

# for finding dict intersection, union, see https://www.youtube.com/watch?v=k2ZWyHdahEk
