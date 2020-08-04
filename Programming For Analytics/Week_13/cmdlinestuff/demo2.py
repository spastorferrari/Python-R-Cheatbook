import argparse as ap
myP = ap.ArgumentParser()
myP.add_argument('myNum', help='My help text', type = int)
myArgs = myP.parse_args()

print(myArgs.myNum)
