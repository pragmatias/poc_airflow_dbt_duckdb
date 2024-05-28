import json 
import pathlib
import os
from datetime import datetime as dt


dir_root  = pathlib.Path(__file__).parent.parent.resolve()
dir_src = f"{dir_root}/data/source"
dir_gen = f"{dir_root}/data/genere"
dir_db = f"{dir_root}/data/database"

type_log_inf = "INF"
type_log_warn = "WRN"
type_log_err = "ERR"

def __get_dir(dir,folder):
    if (folder != ""):
        res_dir = dir+"/"+folder
        if not(os.path.exists(res_dir)):
            os.mkdir(path=res_dir)
        return res_dir
    else:
        raise Exception("Folder","empty")

def get_gen_dir(folder):
    return __get_dir(dir_gen,folder)
     
def get_src_dir(folder):
    return __get_dir(dir_src,folder)

def get_db_dir(folder):
    return __get_dir(dir_db,folder)



def get_cities_info() :
    res = []
    file = open(dir_src+"/cities.json")
    cities = json.load(file)["cities"]
    for i in range(len(cities)):
        row = {}
        row["label"] = cities[i]["label"]
        row["zip_code"] = cities[i]["zip_code"]
        row["latitude"] = cities[i]["latitude"]
        row["longitude"] = cities[i]["longitude"]
        row["department_number"] = cities[i]["department_number"]
        res.append(row)
    return res


def print_log(message,type=type_log_inf):
    date_str = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{date_str} - {type} - {message}")