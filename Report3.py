import sqlite3

dbfile = 'payroll_dc_small.db'	# database file
conn = sqlite3.connect(dbfile)	# connect to db

#give me a new line 
print("")


def main():
	# this is my header row
	print("{0:<25} {1:<15} {2:<10} {3:<10}".format(
			"occupation", "occupation type", "salmax", "salmin"))
			
	cursor = conn.execute("""
		select occ.occtypt, occ.occt, max(f.salary) salmax, min(f.salary) salmin
		from factdata_mar2016 f, occ
		where f.occ=occ.occ
		group by occ.occtypt, occ.occt
		order by salmax desc
		limit 20;
	""")
	
	for row in cursor:
		occupation, occupation_type, salmax, salmin = row
		print("{0:<25} {1:<15} {2:<10} {3:<10}".format(
			occupation, 
			occupation_type[0:14], 
			salmax, 
			salmin
			))
	
	
	print("\nThis is my report of min and max salaries by occupation.")
	conn.close()
	
	
if __name__== "__main__":
	main()