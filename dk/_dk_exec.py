import subprocess
from _tools import SelectContainerIdByUsr


if __name__ == "__main__":
    con_id_str = SelectContainerIdByUsr()
    subprocess.run("sudo docker start {}".format(con_id_str), shell=True)
    subprocess.run("sudo docker exec -it {} bash".format(con_id_str), shell=True)
