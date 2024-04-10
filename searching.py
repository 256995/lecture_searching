import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data[field]


def linear_search(sequence, my_number):
    """
    search my_number in sequence
    :param sequence: list
    :param my_number: float
    :return: results (dict), positions of my_number in sequence and total count
    """
    results = {"positions": [], "count": 0}
    for idx in range(len(sequence)):
        if sequence[idx] == my_number:
            results["positions"].append(idx)
            results["count"] = results["count"] + 1
    return results


def pattern_search(sequence, my_pattern):
    """
    search my_pattern in sequence
    :param sequence: str
    :param my_pattern: str
    :return: result (set), (position of my_pattern in sequence)
    """
    idx = 0
    result = set()
    middle_idx = int(len(my_pattern) / 2) + 1   # prostřední index z my_pattern zaokrouhleno nahoru (pro sudé délky)
    while idx < (len(sequence) - len(my_pattern) + 1):
        index = 0
        for char in my_pattern:
            if char != sequence[idx + index]:
                break
            index += 1
        if index == len(my_pattern):
            result.add((idx + middle_idx))
        idx += 1
    return result


def binary_search(sequence, my_number):
    """
    binary search on my_number in sequence
    :param sequence: list (ordered)
    :param my_number: float
    :return: position
    """
    left = 0
    right = len(sequence) - 1
    middle = int(len(sequence) / 2)
    while left < right:
        if sequence[middle] == my_number:
            return middle
        if sequence[middle] > my_number:
            right = middle - 1
            middle = left + int((right - left) / 2)
        else:
            left = middle + 1
            middle = left + int((right - left) / 2)
    if middle != my_number:
        return None


def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    print(unordered_numbers)
    my_number_in_sequence = linear_search(unordered_numbers, 0)
    print(my_number_in_sequence)
    my_pattern_in_sequence = pattern_search(read_data("sequential.json", "dna_sequence"), "GCA")
    print(my_pattern_in_sequence)
    my_number_in_ordered_sequence = binary_search(read_data("sequential.json", "ordered_numbers"), 78)
    print(my_number_in_ordered_sequence)


if __name__ == '__main__':
    main()