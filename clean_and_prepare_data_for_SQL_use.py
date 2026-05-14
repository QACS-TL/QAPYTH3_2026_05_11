#! /usr/bin/python

import re

def prep_row(row, fh):
    row = re.sub(r"'", r"''", row)
    
    # Add quotes around each field using a Lambda function (alternative solution).
    # lrow = list((map(lambda f: "'" + f + "'", row.split(','))))
    
    lrow = []
    for field in row.split(","):
        lrow.append("'" + field.strip() + "'")

    s = ",".join(lrow)
    fh.write(s + "\n")
    return s
    
fh = open("revamped_country.txt", "w")
for row in open("country.txt", "r"):
    print(prep_row(row, fh))
fh.close()

