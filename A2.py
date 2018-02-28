import json
import csv
import sqlite3
import sys 
 
	
dbfile = 'citiescrosswalk.db'	# database file
conn = sqlite3.connect(dbfile)	# connect to db


def main():
	create_table()			# let's create the table for data
	open_file()				# open the file in insert into db
	print ('Yes!!')			# say good bye to mama
	conn.close				# close connection to db 
	sys.exit(1)				# gently exit the app

def create_table():
	""" This table is where the csv data will be loaded to """
	c = conn.cursor()
	strsql = """ 
		CREATE TABLE if not exists Citiescrosswalk (
			Id INTEGER PRIMARY KEY AUTOINCREMENT, 
			"Citiesid",
			"City",
			"County",	
			"State"
			);
		"""	
	c.execute(strsql)
	conn.commit()	

	
	
def open_file():
	""" open the csv file and load into the cities_crosswalk table	"""	
	r_ct = 0
	
	with open('citiescrosswalk.csv', 'r') as csvfile:
		citiescrosswalk_stream = csv.DictReader(csvfile)
		for citiescrosswalk_row in citiescrosswalk_stream:
			r_ct += 1
			
			# quit after 500 records
			if r_ct > 500:
				break
			
			# pull the data out of the dictionary for sql
			t_citiesid = citiescrosswalk_row['Citiesid']
			t_city = citiescrosswalk_row['City']
			t_county = citiescrosswalk_row['County']
			t_state = citiescrosswalk_row['State']
			
			# print the first ten lines 
			if r_ct <= 10:
				print(r_ct, t_citiesid, t_city, t_county, t_state)
			
	# create a sql cursor, formates the insert sql and executes it. 
	c = conn.cursor()
	strsql = """
		INSERT INTO citiescrosswalk  
			(Citiesid, City, County, State) 
		values (
				'{t_citiesid}', '{t_city}', '{t_county}', '{t_state}' );
				""".format(
					t_citiesid = t_citiesid,
					t_city = t_city,
					t_county = t_county,
					t_state = t_state
					)	
	c.execute(strsql)
	conn.commit()
					
if __name__== "__main__":
	main()