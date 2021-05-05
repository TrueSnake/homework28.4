import argparse
parser = argparse.ArgumentParser()

parser.add_argument('num1', type = int)
parser.add_argument('num2', type = int)
parser.add_argument('op')

parser.add_argument('-v', choices=['+', '-'], action='store_true')

args = parser.parse_args()

if '+' in args.op:
    result = args.num1 + args.num2
    print(result)
elif '-' in args.op:
    result = args.num1 - args.num2
    print(result)
if args.v:
    print(f'{args.num1} {args.op} {args.num2} = {result}')
