"""A simple logic using regex and pdftotext
    first converting the pdf to text and then using regex filtering the data
    I have printed the data, instead we could write it into another file
"""

import pdftotext
import re

with open("questions.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

with open("output.txt", "w") as f:
    f.write("\n\n".join(pdf))

fileobj = open("output.txt", 'r') 
context = fileobj.read()

x = re.findall("[0-9][0-9]\.(.+)\n(.+)\nSol\.(.+)", context)
x.append(re.findall("[0-9][0-9]\..*\n.*\n.*\nSol\..*", context))
x.append(re.findall("[0-9][0-9]\..*\n.*\n.*\n.*\n.*\nSol\..*", context))
x.append(re.findall("[0-9][0-9]\..*\n.*\n.*\n.*\nSol\..*", context))
x.append(re.findall("[0-9][0-9]\..*\n.*\n.*\n.*\n.*\n.*\nSol\..*", context))
x.append(re.findall("[0-9][0-9]\..*\n.*\n.*\n.*\n.*\n.*\n.*\nSol\..*", context))

for mem in x :    
    for stat in mem :
        print(stat)
