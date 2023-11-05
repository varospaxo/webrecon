from fpdf import FPDF
import datetime
import os
from termcolor import colored

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
pdf.cell(200, 1, txt = "", ln = 1, align = 'C')
pdf.cell(190, 10, txt = "By - varospaxo                        v2.5", ln = 1, align = 'C')
pdf.cell(200, 2, txt = "", ln = 1, align = 'C')
pdf.line(10, int(pdf.get_y()), 200, int(pdf.get_y()))
pdf.cell(200, 1, txt = "", ln = 1, align = 'C')
pdf.line(10, int(pdf.get_y()), 200, int(pdf.get_y()))
try:
    # Open the text file in read mode
    f = open("./Temp/Result_current.txt", "r")

    # Insert the texts in the PDF
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='C')

    f.close()
except FileNotFoundError:
    print("Result_current.txt is not present. Skipping to the next file.")

# Define a list of files to process
file_paths = [
    "./Temp/Ping_OP.txt",
    "./Temp/PortScannerFast_OP.txt",
    "./Temp/Traceroute_OP.txt",
    "./Temp/OSDetect_OP.txt",
    "./Temp/SSLCert_OP.txt",
    "./Temp/ReverseDNS_OP.txt",
    "./Temp/Subdomain_OP.txt",
    "./Temp/AdminPages_OP.txt"
]

for file_path in file_paths:
    try:
        # Open the text file in read mode
        f = open(file_path, "r")

        # Extract the filename from the file path
        filename = os.path.basename(file_path)

        # Insert the texts in the PDF
        pdf.cell(200, 10, txt=filename, ln=1, align='L')
        pdf.line(10, int(pdf.get_y()), 100, int(pdf.get_y()))

        for x in f:
            pdf.cell(200, 10, txt=x, ln=1, align='L')

        pdf.cell(200, 6, txt="", ln=1, align='C')

        f.close()
    except FileNotFoundError:
        print(f"{file_path} is not present. Skipping to the next file.")

# Save the PDF with a name
time_now = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
name = "WebRecon_" + time_now
print(name)
pdf.output("./OutputFiles/" + name + ".pdf")
path = os.path.join(os.getcwd(), "OutputFiles", name + ".pdf")
print("Output report saved in " + colored(path, 'green'))

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

print(colored('\n----Script Ended----', 'red'))