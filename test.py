import re

def return_line_info(line):
	if not 'Script died due to an error.' in line:
		line = re.sub(r'\[[0-9]{2}\:[0-9]{2}:[0-9]{2}\.[0-9]{6}\] \(error\)\s+', "", line)
		if ".luac" in line:
			script_name = re.search(r'.+\.luac', line)
			error = re.sub(r'.+\.luac:[0-9]: ', "", line)		
		else:
			script_name = re.search(r'.+\.lua', line)
			error = re.sub(r'.+\.lua:[0-9]: ', "", line)
		return [script_name.group(0), error]
	return "NoneData"


with open("D:\\moonloader.log", "r") as log:
	for line in log.readlines():
		if "(error)" in line:
			data = return_line_info(line)
			if data != "NoneData":
				print(f"Script: {data[0]} | Error: {data[1]}")