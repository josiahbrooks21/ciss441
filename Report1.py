import sqlite3

dbfile = 'payroll_dc_small.db'	# database file
conn = sqlite3.connect(dbfile)	# connect to db

#give me a new line 
print("")


def main():
	# this is my header row
	print("{0:<25} {1:<15} {2:<10} {3:<10}".format(
			"location type", "location", "salmax", "salmin"))
			
	cursor = conn.execute("""
		select loc.loctypt, loc.loct, max(f.salary) salmax, min(f.salary) salmin
		from factdata_mar2016 f, loc
		where f.loc=loc.loc
		group by loc.loctypt, loc.loct
		order by salmax desc
		limit 20;
	""")
	
	for row in cursor:
		location_type, location, salmax, salmin = row
		print("{0:<25} {1:<15} {2:<10} {3:<10}".format(
			location_type, 
			location[0:14], 
			salmax, 
			salmin
			))
	
	
	print("\nThis is my report of min and max salaries by location.")
	conn.close()
	
	
if __name__== "__main__":
	main()