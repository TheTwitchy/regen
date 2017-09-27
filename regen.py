#!/usr/bin/env python

#Application global vars
#TODO Set global vars.
VERSION = "0.1"
PROG_NAME = "regen"
PROG_DESC = "Regular Expression Generator"
PROG_EPILOG = "Written by TheTwitchy. Source available at gitlab.com/TheTwitchy/regen"
DEBUG = True

#Application imports.
import sys,signal
# Insert additional imports here.
import random,re

#Try to import argparse, not available until Python 2.7
try:
    import argparse
except ImportError:
    print_err("Failed to import argparse module. Needs python 2.7+.")
    quit()
#Try to import termcolor, ignore if not available.
DO_COLOR = True
try:
    import termcolor
except ImportError:
    DO_COLOR = False
def try_color(string, color):
    if DO_COLOR:
        return termcolor.colored(string, color)
    else:
        return string
#Print some info to stdout
def print_info(*args):
    sys.stdout.write(try_color(PROG_NAME + ": info: ", "green"))
    sys.stdout.write(try_color(" ".join(map(str,args)) + "\n", "green"))
#Print an error to stderr
def print_err(*args):
    sys.stderr.write(try_color(PROG_NAME + ": error: ", "red"))
    sys.stderr.write(try_color(" ".join(map(str,args)) + "\n", "red"))
#Print a debug statement to stdout
def print_debug(*args):
    if DEBUG:
        sys.stderr.write(try_color(PROG_NAME + ": debug: ", "blue"))
        sys.stderr.write(try_color(" ".join(map(str,args)) + "\n", "blue"))
#Handles early quitters.
def signal_handler(signal, frame):
    print ("")
    quit(0)

#Because.
def print_header():
    print ("  _ __ ___  __ _  ___ _ __  ")
    print (" | '__/ _ \/ _` |/ _ \ '_ \ ")
    print (" | | |  __/ (_| |  __/ | | |")
    print (" |_|  \___|\__, |\___|_| |_|")
    print ("            __/ |           ")
    print ("           |___/            ")
    print ("              version " + VERSION)
    print ("")

# Argument parsing which outputs a dictionary.
def parseArgs():
    #Setup the argparser and all args
    parser = argparse.ArgumentParser(prog=PROG_NAME, description=PROG_DESC, epilog=PROG_EPILOG)
    parser.add_argument("-v", "--version", action="version", version="%(prog)s " + VERSION)
    parser.add_argument("-q", "--quiet", help="surpress extra output", action="store_true", default=False)
    parser.add_argument("-n", "--num", help="number to generate", type=int, default=10)
    parser.add_argument("-l", "--length", help="a probable maximum length", type=int, default=128)
    parser.add_argument("-t", "--test", help="a known matching test string to confirm regex", default="")
    parser.add_argument("regex", help="regex sequence")
    return parser.parse_args()

def get_random_char():
    return chr(random.randint(32, 126))

# Generate a possible matching string.
def gen_new_test_str(max_length):
    gen_length = random.randint(1, max_length)
    tmp_str = ""
    for i in range(0, gen_length):
        tmp_str = tmp_str + get_random_char()
    return tmp_str

#Main application entry point.
def main():
    #Signal handler to catch CTRL-C (quit immediately)
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    argv = parseArgs()

    # Retrieve arg values for application use.
    var_quiet = argv.quiet
    var_num = argv.num
    var_length = argv.length
    var_regex = argv.regex
    var_test_str = argv.test

    #Print out some sweet ASCII art.
    if not var_quiet:
        print_header()

    # Begin application logic.

    #Testing the regex itself
    try:
        re.compile(var_regex)
    except re.error:
        print_err("The regular expression '%s' is not valid." % var_regex)
        quit(2)

    # Perform string test, if requested.
    if var_test_str:
        if not re.match(var_regex, var_test_str):
            print_err("The test string '%s' does not match the regex '%s'. Please recheck your input." % (var_test_str, var_regex))
            quit(1)

    if not var_quiet:
        print_info("The regular expression validated successfully.")

    #Begin testing
    num_found = 0
    num_tests = 0
    while num_found < var_num:
        num_tests = num_tests + 1
        test_str = gen_new_test_str(var_length)
        if re.match(var_regex, test_str):
            num_found = num_found + 1
            print (test_str)
    if not var_quiet:
        print_info("Performed %d tests." % num_tests)

if __name__ == "__main__":
    main()
    quit(0)
