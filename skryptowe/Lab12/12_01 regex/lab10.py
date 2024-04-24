# Wyszukiwanie i wyświetlanie adresów IP w tekście:
# Znajdź wszystkie adresy IP w danym tekście
# text = "Adresy IP serwerów to 192.168.1.1, 10.0.0.1, oraz 172.16.0.1"
import re

text = "Adresy IP serwerów to 192.168.1.1, 10.0.0.1, oraz 172.16.0.1"

match = re.findall("[0-9]{1,3}.[0-9]{1,3}.[0-9].[0-9]", text)
print(match)