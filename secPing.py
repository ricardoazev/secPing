#!/bin/python
import sys
from scapy.all import *

# Verifica se o endereço base foi fornecido
if len(sys.argv) != 2:
    print("Uso: python script.py <endereco_base>")
    sys.exit(1)

conf.verb = 0
base_ip = sys.argv[1]
print("=======Hosts Ativos Na rede==========")
for ip in range(1, 255):
	iprange = f"{base_ip}.{ip}"
	pIP = IP(dst=iprange)
	pacote = pIP/ICMP()
	resp, noresp = sr(pacote,timeout=1)

	for resposta in resp:
		print(resposta[1][IP].src)
