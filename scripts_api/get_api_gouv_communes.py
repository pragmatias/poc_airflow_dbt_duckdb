import requests as rq
import json
import pathlib
import os
import tools_for_api as tfa


result_dir = tfa.get_gen_dir("cities")
result_file = "communes.json"

url = "https://geo.api.gouv.fr/communes"

# stop if the file already exist
if (os.path.exists(result_file)):
    tfa.print_log(f"nothing to do [{result_file}]")
    exit(0)

tfa.print_log(f"Call API [{result_file}]")
res = rq.get(url)

if (res.status_code == 200) :
    json_obj = json.dumps(res.json(),indent=4)
    with open(f"{result_dir}/{result_file}","w") as file:
        file.write(json_obj)
    tfa.print_log(f"File written ! [{result_file}]")
else :  
    tfa.print_log(f"Code sent from requests api : [{res.status_code}]",tfa.type_log_err)
    raise Exception("Call API",res.status_code)

