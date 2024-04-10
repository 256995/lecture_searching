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
    print(data)
    return data[field]


def linear_search(sequence, my_number):
    """
    search number in sequence
    :param sequence: list
    :param my_number: float
    :return:
    """
    results = {"positions": [], "count": 0}
    for idx in range(len(sequence)):
        if sequence[idx] == my_number:
            results["positions"].append(idx)
            results["count"] = results["count"] + 1
    return results


def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    print(unordered_numbers)
    number_in_sequence = linear_search(unordered_numbers, 0)
    print(number_in_sequence)


if __name__ == '__main__':
    main()