
with open('./Temp/Result_current.txt') as f:
    resultPing = f.readlines()
    print (resultPing)
with open('./Temp/PortScannerFast_OP.txt') as f:
    resultPortscanner = f.readlines()
    print (resultPortscanner)
with open('./Temp/Traceroute_OP.txt') as f:
    resultTraceroute = f.readlines()
    print (resultTraceroute)
with open('./Temp/OSDetect_OP.txt') as f:
    resultOS = f.readlines()
    print (resultOS)
with open('./Temp/SSLCert_OP.txt') as f:
    resultSSL = f.readlines()
    print (resultSSL)
with open('./Temp/ReverseDNS_OP.txt') as f:
    resultDNS = f.readlines()
    print (resultDNS)
with open('./Temp/Subdomain_OP.txt') as f:
    resultSubdomain = f.readlines()
    print (resultSubdomain)