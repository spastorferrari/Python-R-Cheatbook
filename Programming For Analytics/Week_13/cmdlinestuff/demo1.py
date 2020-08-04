import argparse # is useful to write command-line arguments in python
parser = argparse.ArgumentParser(description='ADD YOUR DESCRIPTION HERE')
parser.add_argument('-i', '--input', help='Input file name', required=True)
args = parser.parse_args()
print(args)
