#! /usr/bin/python
import json
import argparse

def argument_parser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="path to json file")
    args = vars(ap.parse_args())
    return args

def json_editor(json_file):
    flip_dict = {}
    for key, value in json_file.items():
        flip_dict[value] = key

    print("new json file:", flip_dict)

    with open('new_example_local.json', 'w') as outfile:
        json.dump(flip_dict, outfile)


def main():
    args = argument_parser()
    file = args["input"]

    with open(file) as f:
        json_file = json.load(f)

    print("original json file:", json_file)
    json_editor(json_file)

    print("done")


if __name__ == '__main__':
    main()
