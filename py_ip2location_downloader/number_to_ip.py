import csv
import os, sys, re, csv, socket, struct, ipaddress
import tempfile


def no2ip(iplong):
    # Credits/Taken from, we would have imported this but it is not available
    #  as a python package: 
    # https://github.com/ip2location/ip2location-python-csv-converter
    return (socket.inet_ntoa(struct.pack('!I', int(iplong))))


def csv_number_to_ip(source_path, target_path=None):
    target_eqs_source = False
    if source_path == target_path or not target_path:
        target_eqs_source = True
        target_path = os.path.join(tempfile.gettempdir(), "temptargetpath.csv")
        
    with open(source_path, "r") as csv_source:
        with open(target_path, "w") as csv_path:
            spamreader = csv.reader(csv_source)
            spamwriter = csv.writer(csv_path)
            for row in spamreader:
                row[0] = no2ip(row[0])
                row[1] = no2ip(row[1])
                spamwriter.writerow(row)
    if target_eqs_source:
        os.rename(target_path, source_path)

