# /usr/bin/env python3

# The most simple and fast dorker by @aggr3ssor
# Modify and enjoy

import os
import sys
import time

def main():
	print(banner())
	
	try:
		a = input("Enter Ur Prefix (i.e., \"INURL:\") File Location: "); open(a).close()
		b = input("Enter Ur KeyWord (i.e., \"Fortnite\") File Location: "); open(b).close()
		c = input("Enter Ur FileType (i.e., \".php?\") File Location: "); open(c).close()
		d = input("Enter Ur Parameter (i.e., \"id=\") File Location: "); open(d).close()
		e = input("Enter Ur Afterfix (i.e., \"Game\") File Location: "); open(e).close()
	except:
		print "\nNo such file... exit"
		sys.exit()
	
	output = input("Now Enter Ur  Output File Location: ")
	output_file = open(output, "w")
	
	read_by_line = lambda file: [l[:-1] for l in file.readlines()]
	
	start = int(time.time())
	
	print(f"Start generating dork at {output}")
	
	with open(a, 'r') as af:
		for prefix in read_by_line(af):
			with open(b, 'r') as bf:
				for keyword in read_by_line(bf):
					with open(c, 'r') as cf:
						for filetype in read_by_line(cf):
							with open(d, 'r') as df:
								for parameter in read_by_line(df):
									with open(e, 'r') as ef:
										for afterfix in read_by_line(ef):
											output_file.write(f'{prefix} {keyword} {filetype} {parameter} "{afterfix}"')
											output_file.write('\n')

	print(f"Finished in {int(time.time()) - start} seconds")
	
def banner():
	return """
	 ____           ____                   __         
	/\  _`\        /\  _`\                /\ \        
	\ \ \L\ \__  __\ \ \/\ \    ___   _ __\ \ \/'\    
	 \ \ ,__/\ \/\ \\ \ \ \ \  / __`\/\`'__\ \ , <    
	  \ \ \/\ \ \_\ \\ \ \_\ \/\ \L\ \ \ \/ \ \ \\`\  
	   \ \_\ \/`____ \\ \____/\ \____/\ \_\  \ \_\ \_\
	    \/_/  `/___/> \\/___/  \/___/  \/_/   \/_/\/_/
	             /\___/                               
	             \/__/                      
	"""

if __name__ == "__main__":
	main()
