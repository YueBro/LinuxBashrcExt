import os
import subprocess
from _tools import SelectImgIdByUsr


DEFAULT_MOUNT_LOCAL_PATH = "/home/y/DockerMount"


def AskUsrForVolumnMounts(default_mount=None):
    mount_num = 0
    mounts = [] if (default_mount is None) else [default_mount]
    while True:
        mount_num += 1
        print("Set mount No.{} (e.g.: ~/local_path/:~/docker_path | or <EMPTY> to stop):".format(mount_num))
        s_in = input(">>> ").strip()
        if s_in == "":
            break
        mounts.append(s_in)
    return mounts


if __name__ == "__main__":
    img_id_str = SelectImgIdByUsr()

    mounts = AskUsrForVolumnMounts(
        ("{}:/root/_ext_mount".format(DEFAULT_MOUNT_LOCAL_PATH)
         if os.path.exists(DEFAULT_MOUNT_LOCAL_PATH)
         else None)
    )
    mounts_str = " ".join(['-v "{}"'.format(mount) for mount in mounts])

    docker_run_cmd = "sudo docker run {mounts_str} --net=host --privileged=true -idt {img_id}".format(
        mounts_str=mounts_str,
        img_id=img_id_str
    )
    subprocess.run(docker_run_cmd, shell=True)
