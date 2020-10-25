# esmasidata2csv
One-time Py script to convert EU ESMA Systematic Internaliser xslx files to .csv

# About
This is a very basic script to convert the xlsx files to .csv  from ESMA   

# Prerequisites
* Python, I use Python 3.8.3 from: https://www.python.org/downloads/ 
* GIT, I use 2.28.0 (windows) from: https://git-scm.com/downloads
* PyCharm, I use the Community edition, from: https://www.jetbrains.com/pycharm/download 
* ESMA files from: "https://www.esma.europa.eu/data-systematic-internaliser-calculations"

# Installation
* Clone with GIT, from repo at: https://github.com/roncproject/esmasidata2csv.git
* Get an ESMA file, for testing I used: https://www.esma.europa.eu/sites/default/files/equity_si_calculations_-_publication_file_august_2020.xlsx

# Usage
* On the UNIX/ms windows/MAC/other command line, type: "python esmasidata2csv.py <name of the esma file>" and press enter
* The csv list will be printed to your screen
* In the app directory a file called "esmasidata2csv.log" will appear. It contains technical logging info
* If you want to save the output, you can (on ms windows and UNIX/Linux) type: "python esmasidata2csv.py <name of the esma file> **> outputfile.csv**" (Or any name you want for the output file) 

# TODO
* Nothing To Do, it works as I like it.

# Remarks
* Yes, you an of course convert the ESMA .xlsx files with MS Office Excel , or LibreOffice Calc, or any other way. 
* But for me this is a much less time-consuming way. 
