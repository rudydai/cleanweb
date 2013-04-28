from bs4 import BeautifulSoup
import datetime
import sys

#TODO support time blocks that span more than one day

info = """Output is of the form Type, Date, Start Time, End Time, Usage, Units"""

soup
writeout

def parse_soup(tree):
    writeout.write(info)
    t = "Electric Usage"
    u = "kWh"
    blocks = tree.find_all("Interval Block")
    for block in blocks:
        readings = block.find_all("IntervalReading")
        for reading in readings:
            time_data = reading.timePeriod
            start = int(time_data.start)
            end = start + int(time_data.duration)
            date = datetime.fromtimestamp(start)
            end_date = datetime.fromtimestamp(end)
            usage = str(float(readings.value.string)/1000.0)
            strdate = "/".join(str(date.month), str(date.day), str(date.year))
            strstart = str(date.hour)+":"+str(date.minute)
            strend = str(end_date.hour)+":"+str(end_date.minute)
            writeout.write(",".join([t, strdate, strstart, strend, usage, u])+"\n")

def open_file_string(filestr):
    global soup
    soup = BeautifulSoup(filestr)
    parse_soup(soup, "xml")
    writeout.close()

def open_file_name(filename):
    global soup
    soup = BeautifulSoup(open(filename))
    parse_soup(soup, "xml")
    writeout.close()

def set_writeout(filename):
    global writeout
    writeout = open(filename, "w")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("incorrect usage, call python xmlparser.py filein fileout")
    else:
        set_writeout(sys.argv[2])
        open_file_name(sys.argv[1])
