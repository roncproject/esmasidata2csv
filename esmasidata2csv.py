#!/usr/bin/env python3

import logging
import sys
from openpyxl import load_workbook


# Get the workbook filename from the commandline
def get_arg():
    logging.debug("esmasidata2csv.get_arg() start")
    try:
        arg = sys.argv[1]
    except IndexError:
        logging.warning("esmasidata2csv.get_arg() WARNING: IndexError")
        raise SystemExit(f"Usage: {sys.argv[0]} <esma data file>")

    return arg
    logging.debug("esmasidata2csv.get_arg() end")


#Load the workbook and write the list
def get_list(fname):
    logging.debug("esmasidata2csv.fname() start")

    try:
        wb = load_workbook(filename=fname)
        ws = wb['SI calculations']
        si_list = []
        for row in ws.values:
            for value in row:
                si_list.append(value)
        return si_list
    except:
        logging.critical("esmasidata2csv.get_arg() CRITICAL: An exception occurred while reading the workbook")
        raise SystemExit("CRITICAL: could not read the workbook, app exits")

    logging.debug("esmasidata2csv.fname() end")


# Print the csv from the list
def print_list(list):
    logging.debug("esmasidata2csv.print_list() start")

    try:
        # First 5 values are titles, discard
        list.pop(0)
        list.pop(0)
        list.pop(0)
        list.pop(0)
        list.pop(0)

        length = len(list)

        i = 0
        j = 0
        lines = 0

        # Loop through the list and print
        while i < length:
            if j == 0:
                print(list[i], ",", end='')
            if j == 1:
                print(list[i], ",", end='')
            if j == 2:
                print(list[i], ",", end='')
            if j == 3:
                print(list[i], ",", end='')
            if j == 4:
                print(list[i], ",", end='')
                print("")  # newline
                lines += 1
            i += 1
            j += 1
            if j == 5:
                j = 0

    except:
        logging.error("esmasidata2csv.print_list() ERROR: An error occurred while writing the list")
        raise SystemExit("ERROR: could not write the csv, app exits")

    logging.debug("esmasidata2csv.print_list() end")
    return lines


# Main procedure
def main():
    logging.basicConfig(
        filename="esmasidata2csv.log",
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,     # Possibilities: NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.debug("esmasidata2csv.main() start")

    f = get_arg()
    list = get_list(f)
    l = print_list (list)
    logging.debug("esmasidata2csv.main() end")
    logging.info("%s %s", "esmasidata2csv. number of lines: ", l)

    logging.debug("esmasidata2csv.main() end")


# Script start point
if __name__ == '__main__':
    main()
