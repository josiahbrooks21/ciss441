import sqlite3

dbfile = 'payroll_dc_small.db'	# database file
conn = sqlite3.connect(dbfile)	# connect to db

#give me a new line 
print("")


def main():
	# this is my header row
	print("{0:<17} {1:<25} {2:<10} {3:<10} {4:<4}".format(
			"appointment type", "appointment translation", "salmax", "salmin", "sum"))
			
	cursor = conn.execute("""
		select toa.toatyp, toa.toatypt, max(f.salary) salmax, min(f.salary) salmin, count(*) ct
		from factdata_mar2016 f, toa
		where f.toa=toa.toa
		group by toa.toatyp, toa.toatypt
		order by salmax desc
		limit 20;
	""")
	
	for row in cursor:
		appointment_type, appointment_translation, salmax, salmin, sum = row
		print("{0:<17} {1:<25} {2:<10} {3:<10} {4:<4}".format(
			appointment_type, 
			appointment_translation[0:14], 
			salmax, 
			salmin,
			sum
			))
	
	
	print("\nThis is my report of min and max salaries by type of appointment.")
	conn.close()
	
	
if __name__== "__main__":
	main()