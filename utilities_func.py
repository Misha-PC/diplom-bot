import re


def readConfig(path="static/db.ini"):
    """ read .ini files and return dict """

    print("-----   Read fiel!  ------")

    def clear(s):
        """  """
        char_black_list = ['\n', '\r', '\t']
        for ch in char_black_list:
            s = s.replace(ch, "")
        return s

    raw_data = list()
    out_data = dict()
    cur_block = dict()
    block_name = str()

    # read file from
    try:
        with open(path, "r") as f:
            for line in f:
                raw_data.append(clear(line))
    except FileNotFoundError:
        raise Exception("File '{}' is not found.".format(path))
        return False

    # parse lines from dict
    for line in raw_data:
        # if line is header
        if '[' in line:
            if cur_block != dict():
                out_data[block_name] = cur_block

            re_result = re.search(r'(\w+)', line)

            if not re_result:
                break

            block_name = re_result.group(0)

        # data line
        else:
            name, data = line.split("=", maxsplit=1)
            cur_block[name] = data

    # write last block of data
    if cur_block != dict():
        out_data[block_name] = cur_block

    return out_data


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s).lower()


def dump(obj):
    if isinstance(obj, dict):
        output = '{'
        for i, j in obj.items():
            output += '"{}" : "{}", '.format(i, j)
        output = output[: -2] + '}'

    elif isinstance(obj, list):
        output = '['
        for i in obj:
            output += '"{}", '.format(i)
        output = output[: -2] + ']'

    else:
        raise TypeError("dump error! {} is not dict/list!".format(type(obj)))

    return output
