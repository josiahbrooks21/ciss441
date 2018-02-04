import json
import csv

"""
Josiah Brooks
1/29/2018
"""

row_count = 0
citiescrosswalk_data = []

with open('citiescrosswalk2.csv', 'r') as csvfile:
	citiescrosswalk_stream = csv.DictReader(csvfile, delimiter=',', quotechar='=')
	for c_row_dict in citiescrosswalk_stream:
		row_count += 1
		c_citiesid = c_row_dict['Citiesid']
		c_city = c_row_dict['City']
		c_county = c_row_dict['County']
		c_state = c_row_dict['State']
		if (row_count < 10):
			citiescrosswalk_data.append(c_row_dict)
			print(row_count, c_citiesid, c_city, c_county, c_state)
			
	print('All the city crosswalks!', row_count)
	with open('citiescrosswalkdata.json', 'w') as fp:
		for citiescrosswalk_row_dict in citiescrosswalk_stream:
			print(json.dumps(list(citiescrosswalk_stream)))
	print ('This csv is converted to json')