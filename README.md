# webrecon
![image](https://github.com/varospaxo/webrecon/assets/64273563/6007a92f-92b5-485d-8f9f-475f1dd45672)</br></br>

WebRecon is a tool-chain script intended to automate the process of auditing a website for bug-bounty or pentesting purposes. It runs various scripts in a daisy-chained fashion so as to maintain order and synchronisation. Since the script is highly dependent on network characteristics and configuration of the target, it may generate different (sometimes incorrect) results every time it is executed. However, the overall results may be enough to audit the website properly.</br></br>
## System Requirements
&#9679; Windows 10+ / Linux (Debian) / Android (Termux).</br>
&#9679; Python 3.10 and above.</br>
&#9679; Linux Terminal / Command Prompt / Windows PowerShell</br></br>

## Packages Required
&#9679; termcolor
&#9679; pythonping
&#9679; python-nmap
&#9679; boto3
&#9679; datetime
&#9679; requests
&#9679; fpdf
&#9679; scapy
</br></br>
## Installation
1. Clone the repository
   ```sh
   git clone https://github.com/varospaxo/webrecon
   ```
2. Change to `webrecon` directory
   ```sh
   cd webrecon
   ```
3. Install `requirements.txt`
   ```sh
   pip install -r requirements.txt
   ```
4. Run `WebRecon.py` script (may require sudo or root priviledges)
   ```sh
   python WebRecon.py
   ```
   </br>
## Flow of Execution
![Block Diagram](https://github.com/varospaxo/webrecon/assets/64273563/1af53da6-44a2-4b4e-b243-7d2affa238a3)
</br></br>

## Tools
### Host Service Detection
<!---![3](https://github.com/varospaxo/webrecon/assets/64273563/f668f569-5899-4c30-87ed-008f0464f85b)</br>-->
Host service detection determines whether the host server is alive or not. It also returns the latency between the host server and us as a client. After determining the connection status, it provides the IP address of the host server.</br></br>

### Remote Port Scanner
<!---![PortScanner](https://github.com/varospaxo/webrecon/assets/64273563/752e6e34-3708-490d-93a6-08f258572a5c)</br>-->
Remote port scanner scans the host website for open ports available. This may help determine the services running on the host server and thereby can be used to test the vulnerabilities of the host.</br></br>

### Traceroute Scan
<!---![5](https://github.com/varospaxo/webrecon/assets/64273563/1e3b8326-e543-40ff-abe6-7da8e4627b35)</br>-->
Traceroute scan generates a list of hops required to reach the host server. It also determines whether the connection between those hops is a TCP connection or not.</br></br>

### Remote OS Detection
<!---![6](https://github.com/varospaxo/webrecon/assets/64273563/e6e8f686-efdb-44c6-b87e-d8d4cd05edcd)</br>-->
Remote OS Detection script determines the type of operating system the host server is running. It also provides with the detection accuracy of its generated result.</br></br>

### SSL Certificate Status Scan
<!---![7](https://github.com/varospaxo/webrecon/assets/64273563/6e1a2af0-a2f9-4bf3-bfa6-a94c9fbf23f5)</br>-->
SSL certificate status scan determines the validity of SSL certificate currently active on a website. SSL certificate ensures whether the traffic between the host and its client is encrypted.</br></br>

### Reverse DNS Scanner
<!---![8](https://github.com/varospaxo/webrecon/assets/64273563/6701b788-a5b8-485d-bb0e-8173742cb926)</br>-->
Reverse DNS Scan provides the actual hostname of the server acting as the host server. It can be used to determine the original host of a website.</br></br>

### Subdomain Scanner
<!---![9](https://github.com/varospaxo/webrecon/assets/64273563/a9297f63-cf25-4977-958a-ce309bf0d8ef)</br>-->
Subdomain scanner finds the common subdomains that a website may have. Subdomains may help to find different services provided by the same website.</br></br>

### Admin Page Scanner
<!---![10](https://github.com/varospaxo/webrecon/assets/64273563/d240b3cf-66d9-4af0-b389-9f0ab7c508e1)</br>-->
Admin page scanner tries to find admin panel pages of a website. The admin panel pages are used to access the backend configuration services of a website.</br></br>

### Report Generator
<!---![12](https://github.com/varospaxo/webrecon/assets/64273563/97b8b9a4-17e8-47de-b7a0-5315489ab646)</br>-->
Report generator reads the data created by the script and generates the corresponding pdf documents containing the findings of the script.</br></br>

## Mockup
<p align="center"><img src="https://github.com/varospaxo/webrecon/assets/64273563/6e50b391-4e56-4954-a6fa-5f9c979e9b28"</img></p>


