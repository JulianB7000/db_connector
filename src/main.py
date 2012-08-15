#!/usr/bin/python

import sys, getopt

def exporter():
    print("Exporting Method")

def importer():
    print("Importing Method")

def usage():
    print("main.py")

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "he:i:")
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == '-e':
            print("export")
        elif opt == '-i':
            print("import")



if __name__ == '__main__':
    main(sys.argv[1:])
