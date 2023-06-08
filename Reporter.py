from fpdf import FPDF
import datetime
import os
import time
import shutil

print("\n-----------Generating Report-----------\n")
# a variable pdf
pdf = FPDF()  
  
# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Courier", size = 15)

pdf.cell(190, 6, txt = "  _       __     __    ____                      ", ln = 1, align = 'C')
pdf.cell(190, 6, txt = "| |     / /__  / /_  / __ \___  _________  ____", ln = 1, align = 'C')
pdf.cell(190, 6, txt = " | | /| / / _ \/ __ \/ /_/ / _ \/ ___/ __ \/ __ \\", ln = 1, align = 'C')
pdf.cell(190, 6, txt = " | |/ |/ /  __/ /_/ / _, _/  __/ /__/ /_/ / / / /", ln = 1, align = 'C')
pdf.cell(190, 6, txt = " |__/|__/\___/_.___/_/ |_|\___/\___/\____/_/ /_/ ", ln = 1, align = 'C')
pdf.cell(200, 10, txt = "", ln = 1, align = 'C')
pdf.line(10, int(pdf.get_y()), 200, int(pdf.get_y()))
pdf.cell(200, 1, txt = "", ln = 1, align = 'C')
pdf.line(10, int(pdf.get_y()), 200, int(pdf.get_y()))
# open the text file in read mode
f = open("./Temp/Result_current.txt", "r")
# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
pdf.line(10, int(pdf.get_y()), 200, int(pdf.get_y()))
pdf.cell(200, 1, txt = "", ln = 1, align = 'C')
pdf.line(10, int(pdf.get_y()), 200, int(pdf.get_y()))
pdf.cell(200, 10, txt = "", ln = 1, align = 'C')

# open the text file in read mode
f = open("./Temp/Ping_OP.txt", "r")
pdf.cell(200, 10, txt = "Host Service Detection", ln = 1, align = 'L')
pdf.line(10, int(pdf.get_y()), 100, int(pdf.get_y()))
# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'L')
pdf.cell(200, 6, txt = "", ln = 1, align = 'C')

# open the text file in read mode
f = open("./Temp/PortScannerFast_OP.txt", "r")
pdf.cell(200, 10, txt = "Port Scan", ln = 1, align = 'L')
pdf.line(10, int(pdf.get_y()), 100, int(pdf.get_y()))
# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'L')
pdf.cell(200, 6, txt = "", ln = 1, align = 'C')

# open the text file in read mode
f = open("./Temp/Traceroute_OP.txt", "r")
pdf.cell(200, 10, txt = "Traceroute", ln = 1, align = 'L')
pdf.line(10, int(pdf.get_y()), 100, int(pdf.get_y()))
# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'L')
pdf.cell(200, 6, txt = "", ln = 1, align = 'C')

# open the text file in read mode
f = open("./Temp/OSDetect_OP.txt", "r")
pdf.cell(200, 10, txt = "Remote OS Detection", ln = 1, align = 'L')
pdf.line(10, int(pdf.get_y()), 100, int(pdf.get_y()))
# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'L')
pdf.cell(200, 6, txt = "", ln = 1, align = 'C')

# open the text file in read mode
f = open("./Temp/SSLCert_OP.txt", "r")
pdf.cell(200, 10, txt = "SSL Status", ln = 1, align = 'L')
pdf.line(10, int(pdf.get_y()), 100, int(pdf.get_y()))
# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'L')
pdf.cell(200, 6, txt = "", ln = 1, align = 'C')

# open the text file in read mode
f = open("./Temp/ReverseDNS_OP.txt", "r")
pdf.cell(200, 10, txt = "Reverse DNS", ln = 1, align = 'L')
pdf.line(10, int(pdf.get_y()), 100, int(pdf.get_y()))
# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'L')
pdf.cell(200, 6, txt = "", ln = 1, align = 'C')

# open the text file in read mode
f = open("./Temp/Subdomain_OP.txt", "r")
pdf.cell(200, 10, txt = "Subdomain List", ln = 1, align = 'L')
pdf.line(10, int(pdf.get_y()), 100, int(pdf.get_y()))
# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'L')
pdf.cell(200, 6, txt = "", ln = 1, align = 'C')

# open the text file in read mode
f = open("./Temp/AdminPages_OP.txt", "r")
pdf.cell(200, 10, txt = "Admin Pages Found", ln = 1, align = 'L')
pdf.line(10, int(pdf.get_y()), 100, int(pdf.get_y()))
# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'L')
pdf.cell(200, 6, txt = "", ln = 1, align = 'C')

# save the pdf with name .pdf
time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S') 
name = "WebRecon_"+time_now
print(name)
pdf.output("./OutputFiles/"+name+".pdf")
print("Output report saved in '"+str(os.getcwd())+"\OutputFiles\\"+name+".pdf'")


# if os.path.exists("./Temp/Result_current.txt"):
#   os.remove("./Temp/Result_current.txt")
# else:
#   print("The file does not exist")
  
# if os.path.exists("./Temp/Ping_OP.txt"):
#   os.remove("./Temp/Ping_OP.txt")
# else:
#   print("The file does not exist")
  
# if os.path.exists("./Temp/PortScannerFast_OP.txt"):
#   os.remove("./Temp/PortScannerFast_OP.txt")
# else:
#   print("The file does not exist")

# if os.path.exists("./Temp/Traceroute_OP.txt"):
#   os.remove("./Temp/Traceroute_OP.txt")
# else:
#   print("The file does not exist")

# if os.path.exists("./Temp/OSDetect_OP.txt"):
#   os.remove("./Temp/OSDetect_OP.txt")
# else:
#   print("The file does not exist")

# if os.path.exists("./Temp/SSLCert_OP.txt"):
#   os.remove("./Temp/SSLCert_OP.txt")
# else:
#   print("The file does not exist")
  
# if os.path.exists("./Temp/ReverseDNS_OP.txt"):
#   os.remove("./Temp/ReverseDNS_OP.txt")
# else:
#   print("The file does not exist")
  
# if os.path.exists("./Temp/AdminPages_OP.txt"):
#   os.remove("./Temp/AdminPages_OP.txt")
# else:
#   print("The file does not exist")

# path = str(os.getcwd())+"\Temp\Subdomain_OP.txt"
# os.system('TASKKILL /F /IM Subdomain_OP.txt')
# shutil.rmtree("Temp")
# os.mkdir("Temp")
  
# if os.path.exists("./Temp/Subdomain_OP.txt"):
#   os.remove("./Temp/Subdomain_OP.txt")
# else:
#   print("The file does not exist")

print('\n----Script Ended----')