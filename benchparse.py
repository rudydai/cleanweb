import json
import time
import sys

def parse_input(filein, fileout):
    readin = open(filein, 'r')
    writeout = open(fileout, 'w')
    measurements = {} 
    for line in readin:
        startime = 0
        entries = line.split(',')
        if len(entries) != 26:
            print "incorrectly formatted input: "+line
            break
        date = entries[1].strip()
        date = date[:6]
        entries = entries[2:]
        for meas in entries:
            start = str(startime)+":00"
            end = str(startime)+":59"
            measure = float(meas)
            key = date+start
            measurements[key] = measure
            startime += 1
    writeout.write(json.dumps({"readings": measurements}))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage is: python benchparse.py filein fileout")
    else:
        parse_input(sys.argv[1], sys.argv[2])


