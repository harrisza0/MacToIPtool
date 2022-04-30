#this bat installs python, and usingn python installs pip which is used to install the necessary libraries, NETMIKO for querying
network devices, and a few others for the gui.#


Start python-3.9.0-amd64.exe

Timeout 5

python get-pip.py

Timeout 5

pip install Netmiko

Timeout 1 

pip install getpass

Timeout 1

pip install ConnectHandler



