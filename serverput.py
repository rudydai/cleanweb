import urllib2, urllib
import time
import ravenparser
import sys

url = "PUT SOMETHING HERE"

def bundle_into_packet(demand, timestamp):
    params = urllib.urlencode({"demand":demand, "time":timestamp})
    request = urllib2.Request(url, params)
    response = urllib2.urlopen(request)
    return response.read()

def get_info(filename):
    gener = ravenparser.read_from_log(filename)
    for reading in gener:
        print bundle_into_packet(reading, time.time())

if __name__ == "__main__":
    if len(sys.argv) == 3:
        global url
        url = sys.argv[2]
        get_info(sys.argv[1])
    elif len(sys.argv) == 2:
        get_info(sys.argv[1])
    else:
        print "Incorrect call, please call python serverput.py logfile url"

