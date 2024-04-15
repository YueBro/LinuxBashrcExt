import subprocess
from _tools import SelectImgIdByUsr


if __name__ == "__main__":
    img_id_str = SelectImgIdByUsr()
    subprocess.run("sudo docker rmi {}".format(img_id_str), shell=True)
