# list can be empty -> []
# Can the list have other data types -> dict, str, list, int, tuple
# What happen Null? raise exception


# def json_encoder(string):
#     output = "["
#     for value in string:

#     output =+ "]"

#     return output


def encode(string):
    if string is None:
        raise Exception("None is not accepted")

    if not isinstance(string, (list, int, tuple, dict, str)):
        raise Exception("{} is not accepted".format(type(string)))
    else:
        if isinstance(string, int):
            return str(string)
        elif isinstance(string, str):
            return '"{}"'.format(string)
        elif isinstance(string, list):
            return "[{}]".format(",".join(encode(x) for x in string))
        else:
            # output = "{"
            # for key, value in string.items():
            #     new_key = encode(key)
            #     new_value = encode(value)
            #     output += "{}:{},".format(str(new_key), str(new_value))
            # output = output[:-1]
            # output += "}"
            # return output
            output = ",".join(["{0}:{1}".format(encode(key), encode(value)) for key, value in string.items()])
            return "{"+ output + "}"


if __name__ == "__main__":
    tests = None
    # print(encode(tests))
    tests = "abuchi"
    # print(encode(tests))
    tests = [1,2,3,4]   # ["1", "2", "3", "4"]
    tests = [1,'2',3,[1,2,'4']]   # ["1", "2", "3", "4"]
    tests = {"name": "Abuchi", "test": 3}   # ["1", "2", "3", "4"]
    print(encode(tests))
    # tests = ["string"]  # ["string"]
    # tests = [1, 2, 3, [1,2]]    #["1", "2", "3", ["1","2"]]
    # tests = '[{"name": "Abuchi"}]'  # {"name": "Abuchi"}

