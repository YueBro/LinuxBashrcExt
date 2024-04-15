import subprocess


def _GetCmdPrinting(cmd, encoding="utf-8"):
    return str(subprocess.check_output(cmd, shell=True).decode(encoding))


def SelectImgIdByUsr():
    s = _GetCmdPrinting("sudo docker image list", encoding="utf-8")
    lines = s.split("\n")

    print("[Select an image]")

    print("    " + lines[0])
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "":
            continue
        print("{:2}. {}".format(i, line))
    i = int(input(">>> "))
    assert i > 0
    img_id_str = lines[i][lines[0].find("IMAGE ID"):].split()[0]

    return img_id_str


def SelectContainerIdByUsr():
    s = _GetCmdPrinting("sudo docker ps -a", encoding="utf-8")
    lines = s.split("\n")

    print("[Select a container]")

    print("    " + lines[0])
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "":
            continue
        print("{:2}. {}".format(i, line))
    i = int(input(">>> "))
    assert i > 0
    con_id_str = lines[i].split()[0]

    return con_id_str
