#!/usr/bin/python3
import argparse, subprocess as lol
try:
    parser = argparse.ArgumentParser(description="Demo")
    parser.add_argument("-f",type=str,help="input file", required=True)
    parser.add_argument("-o",type=str,help="Output file", required=True)
    a = parser.parse_args()

    f = open(a.f, "r")
    for i in f.readlines():
        data = lol.check_output("host -t a {}".format(i).strip('\n'), shell=True)
        g = open(a.o, "ab")
        g.write(data)
except Exception as anything:
    print("Error:", anything)
else:
    print("DONE")
finally:
    g.close()
