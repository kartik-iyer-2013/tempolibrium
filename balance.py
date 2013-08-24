# balance.py: the machine only fires if this says OK
#   python balance.py seats.csv
import csv
import sys


def load(path):
    return list(csv.DictReader(open(path)))


def time_residue(seats):
    # rule 1: sum of mass * days has to be zero
    total = 0.0
    for s in seats:
        total += float(s['mass_kg']) * int(s['days'])
    return total


if __name__ == '__main__':
    seats = load(sys.argv[1])
    r = time_residue(seats)
    print 'time residue: %.2f kg-days' % r
    print 'OK' if abs(r) < 0.01 else 'NOT BALANCED'
