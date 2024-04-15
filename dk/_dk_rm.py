import subprocess
from _tools import SelectContainerIdByUsr


if __name__ == "__main__":
    con_id_str = SelectContainerIdByUsr()
    subprocess.run("sudo docker stop {}".format(con_id_str), shell=True)
    subprocess.run("sudo docker rm {}".format(con_id_str), shell=True)
