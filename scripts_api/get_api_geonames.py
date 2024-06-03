import requests as rq
import tools_for_api as tfa
import time
import os
import zipfile

result_dir = tfa.get_gen_dir("geonames")
url_base = "https://download.geonames.org/export/dump"

file_FR_zip = "FR.zip"
file_FR = "FR.txt"

file_FR_header = "geonameid;name;ascii_name;alternate_names;latitude;longitude;feature_class;feature_code;country_code;cc2;admin1_code;admin2_code;admin3_code;admin4_code;population;elevation;dem;timezone;modification_date"

file_admin1 = "admin1CodesASCII.txt"
file_admin1_header = "code;name;name_ascii;geonameid"
file_admin2 = "admin2Codes.txt"
file_admin2_header = "codes;name;name_ascii;geonameId"


pause_api = 10
headers = { 
	"Accept-Language" : "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
	"user_agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
}

list_download = [file_FR_zip,file_admin1,file_admin2]

list_zip = [file_FR_zip]

list_files_to_transfrom = [(file_admin1,file_admin1_header)
						,(file_admin2,file_admin2_header)
						,(file_FR,file_FR_header)]


def call_api(filename):
	# if file already exist then bypass the call api
	filecsv = f"{filename.split('.')[0]}.csv"
	if os.path.exists(f"{result_dir}/{filecsv}") or os.path.exists(f"{result_dir}/{filename}") :
		tfa.print_log(f"Nothing to do [{filename}]")
		return 
	
	time.sleep(pause_api)
	tfa.print_log(f"Call API [{filename}]")
	res = rq.get(url=f"{url_base}/{filename}",stream=True,headers=headers)
	if (res.status_code == 200) :
		with open(f"{result_dir}/{filename}","wb") as file:
			for chunk in res.iter_content(chunk_size=10 * 1024):
				file.write(chunk)
		tfa.print_log(f"File written ! [{filename}]")
	else :
		tfa.print_log(f"Code sent from requests api : [{res.status_code}]",tfa.type_log_err)
		raise Exception("Call API",res.status_code)



def decompress_zip(filename):
	txt_file = f"{filename.split('.')[0]}.txt"

	if not os.path.exists(f"{result_dir}/{filename}") :
		return 
	
	tfa.print_log(f"Decompress zip file [{filename}]")
	with zipfile.ZipFile(f"{result_dir}/{filename}") as zip:
		with open(f"{result_dir}/{txt_file}",'wb') as f:
			f.write(zip.read(txt_file))

	if (os.path.exists(f"{result_dir}/{txt_file}")):    
		os.remove(f"{result_dir}/{filename}")
	else :
		tfa.print_log("{txt_file} not found in the file {filename}",tfa.type_log_err)
		raise Exception("Decompress Zip",)
	
	tfa.print_log(f"File decompressed [{txt_file}]")



def transform_txt_to_csv(filename,header):
	csv_file = f"{filename.split('.')[0]}.csv"
	if not os.path.exists(f"{result_dir}/{filename}"):
		return
	
	tfa.print_log(f"Transform txt to csv [{filename}]")
	with open(f"{result_dir}/{csv_file}",'w') as res:
		res.write(header+"\n")
		with open(f"{result_dir}/{filename}",'r') as txt:
			while True:
				content=txt.readline()
				if not content:
					break
				res.write(content.replace('\t',';'))
	os.remove(f"{result_dir}/{filename}")
	tfa.print_log(f"Transformed ! [{filename}]")


# download all files
for elt in list_download:
	call_api(elt)

# decompress zip files
for elt in list_zip:
	decompress_zip(elt)

# transform txt to csv
for (elt,head) in list_files_to_transfrom:
	transform_txt_to_csv(elt,head)

