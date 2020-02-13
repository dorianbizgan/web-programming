from flask import Flask
from flask import request
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)
url = "https://raw.githubusercontent.com/devdattakulkarni/elements-of-web-programming/master/data/austin-pool-timings.xml"
data = requests.get(url)

root = ET.fromstring(data.text)
pool_data = {}

test_var = ""
# Parsing XML Data and Create Dictionary 
for pool in root.findall("row"):
	pool_name = ""
	weekday = ""
	pool_type = ""
	weekday_closure = ""

	try:
		pool_name = pool.find("pool_name").text
		weekday = pool.find('weekday').text
		pool_type = pool.find ('pool_type').text
		weekday_closure = pool.find('weekday_closure').text
	except AttributeError:
		continue 
	test_var += str(pool_name) + " " + str(weekday) + " " + str(pool_type) + " " + str(weekday_closure) + " " +  "<br>"
	print(pool_name, weekday, pool_type, weekday_closure)
	pool_data[pool_name] = [weekday, pool_type, weekday_closure]

@app.route("/")
def queryparam():
	
	try:
		try:
			param1 = request.args.get("weekend")
		except:
			pass
		try:
			param2 = request.args.get("pool_type")
		except:
			pass
		try:
			param3 = request.args.get("weekday_closure")
		except:
			pass
		
		print(str(param1), str(param2), str(param3))

		temp_string = ""
		temp_dict = pool_data.copy()
		#DNI = Do not include

		if param1:
			for i in temp_dict:
				if str(param1) != temp_dict[i][0]:
					temp_dict[i] = "DNI"

		if param2:
			for i in temp_dict:
				if str(param2) != temp_dict[i][1]:
					temp_dict[i] = "DNI"

		if param3:
			print("inside param3")
			for i in temp_dict:
				if str(param3) != temp_dict[i][2]:
					temp_dict[i] = "DNI"
		
		if param1 or param2 or param3:
			for i in temp_dict:
				if temp_dict[i] != "DNI":
					temp_string += i + "\n"
			print(temp_dict, "______________", temp_string)
			
			return(temp_string)
		else:
			return ("<h1>Welcome to Austin Pool Information Website</h1>")


	except:
		return ("<h1>Welcome to Austin Pool Information Website</h1>")
