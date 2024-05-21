import requests as rq
import json
import pathlib

file_dir  = pathlib.Path(__file__).parent.parent.resolve()
result_dir = f"{file_dir}/data/source"

res = rq.get("https://geo.api.gouv.fr/communes")

if (res.status_code == 200) :
  json_obj = json.dumps(res.json(),indent=4)
  with open(f"{result_dir}/communes.json","w") as file:
    file.write(json_obj)
else :
  print(f"error : {res.status_code}")

