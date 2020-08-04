import argparse

parser = argparse.ArgumentParser(description='Program to copy files')
parser.add_argument('-i','--input', help='Input file name',required=True)
parser.add_argument('-o','--output',help='Output file name', required=True)
args = parser.parse_args()

## show the values that are provided ##
print ("Input file: {}".format(args.input))
print ("Output file: {}".format(args.output))
