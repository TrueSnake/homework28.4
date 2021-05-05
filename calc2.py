import argparse

parser = argparse.ArgumentParser()

parser.add_argument('nums', type = int, nargs='+')

parser.add_argument('op', choices=['+', '-'])

parser.add_argument('--verbose', '-v', action='store_true')

parser.add_argument('--file', '-f')

parser.add_argument('--quiet', '-q', action='store_true')

parser.add_argument('--append', '-a', action='store_true')

args = parser.parse_args()

s = 0
smth = ''

if '+' in args.op:
    for i in args.nums:
        s += i

elif '-' in args.op:
    s = args.nums[0]
    for i in args.nums[1:]:
        s -= i

if args.verbose:
    for i in args.nums:
        smth = smth + str(i) + args.op
    else:
        smth = smth[:-1]
        smth += f'={s}'
    if not args.quiet:
        print(smth)

if not args.append:

    if args.file:

        smth = ''

        a = open(args.file, 'w')

        for i in args.nums:
            smth = smth + str(i) + args.op
        else:
            smth = smth[:-1]
            smth += f'={s}'

        a.write(smth)
        a.close()

else:
    if args.file:
        a = open(args.file, 'a')
        smth = ''
        for i in args.nums:
            smth = smth + str(i) + args.op
        else:
            smth = smth[:-1]
            smth += f'={s} '

        a.write(smth)
        a.close()

if not args.quiet:
    print(s)