
*** Python3 en test  ->  git clone https://github.com/JulioMartin/PY_Test

https://askubuntu.com/questions/262063/how-to-find-python-installation-directory-on-ubuntu
which python3
/usr/bin/python3

https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/

sudo apt update
sudo apt install python3-pip
pip3 --version

Checkeo post instalacion (debe aparecer como "installed" (automatic es que viene con el SO Linux)):
apt list --installed | grep pip
JFM: python3-pip/focal-updates,focal-updates,now 20.0.2-5ubuntu1.6 all [installed]


-- for plot
https://aprendeconalf.es/docencia/python/manual/matplotlib/
pip3 install matplotlib

Chequeo del paquete instalado:
pip3 list | grep matplotlib
JFM: matplotlib         3.5.1

-- for export to csv file
https://datatofish.com/export-dataframe-to-csv/
pip3 install pandas

-- for download info de cotizaciones diarias test
https://blog.devgenius.io/download-and-analyze-crypto-market-data-with-python-c23941e475f
pip3 install yfinance
pip3 install seaborn


-- SMA (usando lib de pandas)
https://www.learndatasci.com/tutorials/python-finance-part-3-moving-average-trading-strategy/


-- TA-lib (librerias de AT)
https://mrjbq7.github.io/ta-lib/install.html

Para linux - Instalar librerias escritas en C de TA-lib:
http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz

* Descompactar: /opt/ta-lib
* cd ta-lib/
* ./configure --prefix=/usr
* make
* sudo make install

Instalar el wrapper de python de TA-lib:
pip install TA-Lib

Chequeo del paquete instalado:
pip3 list | grep TA-
JFM: TA-Lib     0.4.24        

