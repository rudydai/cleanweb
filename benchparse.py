import json
import time
import sys

def parse_input(filein, fileout):
    readin = open(filein, 'r')
    writeout = open(fileout, 'w')
    measurements = []
    for line in readin:
        startime = 0
        entries = line.split(',')
        if len(entries) != 26:
            print "incorrectly formatted input: "+line
            break
        date = entries[1].strip()
        entries = entries[2:]
        for meas in entries:
            epochtime = int(time.mktime(time.strptime(date+" "+str(startime)+":00", "%m/%d/%Y %H:%M")))
            start = str(startime)+":00"
            end = str(startime)+":59"
            measure = float(meas)
            entry = {"time": epochtime, "date":date, "start":start, "end":end, "kWh": measure, "type":"Electric Usage"}
            measurements.append(entry)
            startime += 1
    writeout.write(json.dumps({"readings": measurements}, sort_keys=True, indent=4, separators=(",", ": ")))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage is: python benchparse.py filein fileout")
    else:
        parse_input(sys.argv[1], sys.argv[2])


