import requests as rq
import json
import functools
import tools_for_api as tfa
import time
import os
from datetime import datetime as dt

result_dir = tfa.get_gen_dir("weather")
result_file = "weather_forecast"
current_date = dt.now().strftime("%Y%m%d")
url = "https://api.open-meteo.com/v1/forecast"
pause_api = 15
limit_cities = 20
forecast_day = 7
headers = { 
	"Accept-Language" : "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
	"user_agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
}

def rebuild_json_detail(response) :
	"""
	Return a new Array JSON from Weather API Result.
	
	Arguments:
	- response : JSON from Weather API
	"""
	res_json = []
	# Get the daily information
	tmp_json = response["daily"]
	# get the time information to browse all elements
	time_list = tmp_json["time"]
	
	for i in range(len(time_list)) :
		row = {}
		row["coordinate"] = {"latitude" : response["latitude"], "longitude" : response["longitude"]}
		row["time"] = tmp_json["time"][i]
		row["weather_code"] = tmp_json["weather_code"][i]
		row["temperature_2m_max"] = tmp_json["temperature_2m_max"][i]
		row["temperature_2m_min"] = tmp_json["temperature_2m_min"][i]
		row["sunrise"] = tmp_json["sunrise"][i]
		row["sunset"] = tmp_json["sunset"][i]
		row["daylight_duration"] = tmp_json["daylight_duration"][i]
		row["sunshine_duration"] = tmp_json["sunshine_duration"][i]
		row["precipitation_hours"] = tmp_json["precipitation_hours"][i]
		res_json.append(row)
	return res_json


def rebuild_json(responses):
	"""
	Return a new Array JSON from Weather API Result.
	Allow to manage a result of type Array
	
	Arguments:
	- response : JSON from Weather API
	"""
	res_list = []
	if (isinstance(responses,list)) :
		res_list = functools.reduce(lambda x,y : x + y,map(lambda x: rebuild_json_detail(x),responses))
	else:
		res_list = rebuild_json_detail(responses)
	return res_list


def call_api_for_each_dept() :
	cities = tfa.get_cities_info()
	dept_list = list(dict.fromkeys(map(lambda x : x["department_number"],cities)))
	dept_list = list(filter(lambda x : x.isdigit(),dept_list))
	#dept_list=["91"]
	for d in dept_list:
		tfa.print_log(f"Call for dept [{d}] ...")
		cities_in_d = list(filter(lambda x: x["department_number"] == d,cities))
		cities_lat = list(map(lambda x : x["latitude"], cities_in_d))
		cities_lon = list(map(lambda x : x["longitude"],cities_in_d))
		iterat = 1
		while len(cities_lat) > limit_cities :
			cities_lat_tmp = cities_lat[0:limit_cities:]
			cities_lon_tmp = cities_lon[0:limit_cities:]
			cities_lat = cities_lat[limit_cities::]
			cities_lon = cities_lon[limit_cities::]
			call_api(d,cities_lat_tmp,cities_lon_tmp,iterat)
			iterat+=1

		call_api(d,cities_lat,cities_lon,iterat)



def call_api(dept,latitude,longitude,iterat) :

	# if the result file exist, then we don't need to getit now
	filename = f"{result_file}_{dept}_{forecast_day}d_{current_date}_{iterat:0>{2}}.json"
	res_file = f"{result_dir}/{result_file}_{dept}_{forecast_day}d_{current_date}_{iterat:0>{2}}.json"
	if os.path.exists(res_file) : 
		tfa.print_log("Nothing to do [{filename}]")
		return
	
	params = {
		"latitude": latitude,
		"longitude": longitude,
		"daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "sunrise", "sunset", "daylight_duration", "sunshine_duration", "precipitation_hours"],
		"timezone": "Europe/London",
		"forecast_days": forecast_day
	}
	#print(params)
	tfa.print_log(f"Wait [{pause_api}] sec before calling API ... [{iterat}]")
	time.sleep(pause_api)
	tfa.print_log(f"Calling API now ! [{iterat}]")
	res = rq.get(url,params=params,headers=headers)

	if (res.status_code == 200) :
		json_obj = json.dumps(rebuild_json(res.json()),indent=4)
		with open(f"{res_file}","w") as file:
			file.write(json_obj)
		tfa.print_log(f"File written ! [{iterat}]")
	else :
		tfa.print_log(f"{res.status_code}",tfa.type_log_err)



def main():
	call_api_for_each_dept()

if __name__ == "__main__":
	main()
