import sys
import json



def receive_input():
    if not sys.stdin.isatty(): 
        return json.load(sys.stdin)
    raise Exception("STOP")


def json_flattener(json_dict):
    output = {}
    def flatten(dictionary, keyName=''):
        if isinstance(dictionary,dict):
            for i in dictionary:
                flatten(dictionary[i], keyName + i + '.')
        else:
            output[keyName[:-1]] = dictionary
    flatten(json_dict)
    return output



def main():
    insert = receive_input()

    y = json_flattener(insert)
    z = json.dumps(y)
    print(z)


if __name__ == "__main__":
    main()