# importing library
import requests
import os
import subprocess
# function for scanning subdomains
def domain_scanner(domain_name,sub_domnames):
	print('-----------Subdomain Scanner Started-----------\n')
	try:
		# loop for getting URLs
		for subdomain in sub_domnames:
		
			# making url by putting subdomain one by one
			url = f"https://{subdomain}.{domain_name}"
			
			# using try catch block to avoid crash of
			# the program
			try:
			
				# sending get request to the url
				requests.get(url, timeout=2)
				
				# if after putting subdomain one by one url
				# is valid then printing the url
				print(f'[+] {url}')
				f = open("./Subdomain.txt", "a")
				f.write(f'[+] {url}')
				f.write("\n")
				f.close()
				
			# if url is invalid then pass it
			except requests.ConnectionError:
				pass
		path_current="./Subdomain.txt"
		movepath = "./Temp/Subdomain_OP.txt" 
		os.replace(path_current, movepath)
		print('\n')
	except:
			print("No Subdomains Found !!!")
			f = open("./Subdomain.txt", "a")
			f.write("No Subdomains Found !!!")
			f.close()
			path_current="./Subdomain.txt"
			movepath = "./Temp/Subdomain_OP.txt" 
			os.replace(path_current, movepath)
			print('\n')


 
#Remove Temp File Save Output File
	
	print('----Scanning Finished----')
	print('-----Scanner Stopped-----\n')

# main function
if __name__ == '__main__':

	# inputting the domain name
	with open('./Temp/Result_current.txt') as f:
         dom_name = f.readline().strip()
	
print('\n')

	# opening the subdomain text file
with open('Subdomain_names.txt','r') as file:
	
		# reading the file
		name = file.read()
		
		# using splitlines() function storing the
		# list of splitted strings
		sub_dom = name.splitlines()
		
	# calling the function for scanning the subdomains
	# and getting the url
domain_scanner(dom_name,sub_dom)

#Run Next Script
rawpath = os.getcwd() + "\\Reporter.py"
path = rawpath.replace('\\', '/')
subprocess.call(['python', path])