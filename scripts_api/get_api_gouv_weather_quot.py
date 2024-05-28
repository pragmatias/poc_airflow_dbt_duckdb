import requests as rq
import tools_for_api as tfa
import time
import os
import gzip
import shutil

result_dir = tfa.get_gen_dir("meteofrance")
url_base = "https://object.files.data.gouv.fr/meteofrance/data/synchro_ftp/BASE/"
#Q_91_previous-1950-2022_autres-parametres.csv.gz"
url_file_type = "QUOT/Q_"
url_file_period = ["_previous-1950-2022","_latest-2023-2024"]
url_file_end = ["_RR-T-Vent.csv","_autres-parametres.csv"]
url_zip_ext = ".gz"
result_file_type = "QUOT_departement_"
pause_api = 15
headers = { 
	"Accept-Language" : "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
	"user_agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
}


def call_api(url,filename):
	# if file already exist then bypass the call api
	filezip = f"{filename}{url_zip_ext}"
	result_filezip = f"{result_dir}/{filezip}"
	result_filename = f"{result_dir}/{filename}"
	if os.path.exists(result_filename) :
		tfa.print_log(f"Nothing to do [{filename}]")
		return 
	
	time.sleep(pause_api)
	tfa.print_log(f"Call API [{filezip}]")
	res = rq.get(url=url,stream=True,headers=headers)
	if (res.status_code == 200) :
		with open(result_filezip,"wb") as file:
			for chunk in res.iter_content(chunk_size=10 * 1024):
				file.write(chunk)
		tfa.print_log(f"File written ! [{filezip}]")
		# Decompress data
		with gzip.open(result_filezip,'rb') as gzip_ref:
			with open(result_filename,'wb') as file_w:
				shutil.copyfileobj(gzip_ref,file_w)
		os.remove(result_filezip)
		tfa.print_log(f"File decompressed ! [{filename}]")
	else :
		tfa.print_log(f"Code sent from requests api : [{res.status_code}]",tfa.type_log_err)
		raise Exception("Call API",res.status_code)



cities = tfa.get_cities_info()
dept_list = list(dict.fromkeys(map(lambda x : x["department_number"],cities)))
dept_list = list(filter(lambda x : x.isdigit() and x not in ["97","976"],dept_list))
#dept_list=["91"]

for d in dept_list:
	for period in url_file_period:
		for type in url_file_end:
			# build url
			url = f"{url_base}{url_file_type}{d:0>{2}}{period}{type}{url_zip_ext}"
			filename = f"{result_file_type}{d:0>{2}}{period}{type}"

			# call api tp get data
			call_api(url,filename)

