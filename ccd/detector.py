import sys
import os
import re


def OutputResult(result: str):
    print(result)   # Will be captured by bash
    exit(0)


def _DecodeLine(line: str, line_idx: int):
    # Remove comments
    cmt_idx = line.find("#")
    if cmt_idx != -1:
        line = line[:cmt_idx]
    
    # Remove empty
    if line.strip() == "":
        return None
    
    # Split into elements
    quotes = [i for i, c in enumerate(line) if (c == '"' and (i == 0 or (line[i-1] != '\\')))]
    if (len(quotes) % 2) != 0:
        raise SyntaxError("Invalid syntax in cfg line {}".format(line_idx+1))
    elements = []
    for i in range(1, len(quotes)-1, 2):
        i1, i2 = quotes[i], quotes[i+1]
        if line[i1+1:i2].strip() != "":
            raise SyntaxError("Invalid syntax in cfg line {}".format(line_idx+1))
    for i in range(0, len(quotes), 2):
        i1, i2 = quotes[i], quotes[i+1]
        elements.append(line[i1+1:i2])

    # Output elements
    if (len(elements) != 2):
        raise SyntaxError("Invalid syntax in cfg line {}".format(line_idx+1))
    return elements[0], elements[1].strip()     # path_regex, env_name


def ReadCfg(pth):
    with open(pth, "r", encoding="utf-8") as fp:
        ls = fp.readlines()
    terms = []
    for i, l in enumerate(ls):
        elements = _DecodeLine(l, i)
        if elements is not None:
            path_regex, env_name = elements
            terms.append([path_regex, env_name])
    return terms


def GetTheEnv(root_path: str, cfgs: list):
    for path_regex, env_name in cfgs:
        if re.fullmatch(path_regex, root_path):
            return env_name
    return None


if __name__ == "__main__":
    root_path = os.path.dirname(__file__)
    target_path = os.path.abspath(sys.argv[1])

    # print(root_path)    # DEBUG
    # print(target_path)  # DEBUG
    # print(sys.argv[1])  # DEBUG

    cfgs = ReadCfg(os.path.join(root_path, "ccd_env_list.cfg"))
    env_name = GetTheEnv(target_path, cfgs)
    OutputResult(env_name if (env_name is not None) else "")
