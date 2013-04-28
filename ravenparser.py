from bs4 import BeautifulSoup
import time
import sys

buff = ""

def parse_log_entry(string):
    global buff
    if buff != "":
        string = buff+"\n"+string
    soup = BeautifulSoup(string, "xml")
    relevant = soup.InstantaneousDemand
    if relevant:
        buff = string
        demand = relevant.Demand
        mult = relevant.Multiplier
        div = relevant.Divisor
        if demand and mult and div:
            multiplier = int(mult.string, 16)
            smult =  (multiplier + 2**31) % 2**32 - 2**31
            if smult == 0:
                smult = 1
            reading = int(demand.string, 16)
            sreading =  (reading + 2**31) % 2**32 - 2**31
            divisor = int(div.string, 16)
            sdiv = (divisor+2**31) % 2**32 - 2**31
            if sdiv == 0:
                sdiv = 1
            buff = ""
            return(float(sreading)*smult/sdiv)
    else:
        buff = ""

def read_from_log(filename):
    log = open(filename)
    log.seek(0,2)
    while True:
        where = log.tell()
        line = log.readline()
        if not line:
            time.sleep(5)
            log.seek(where)
        else:
            lines = []
            while line:
                lines.append(line)
                line = log.readline()
            str_rep = "\n".join(lines)
            ret = parse_log_entry(str_rep)
            if ret:
                yield ret
            
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "incorrect usage, please provide log file name"
    else:
        gener = read_from_log(sys.argv[1])
        for reading in gener:
            print reading
