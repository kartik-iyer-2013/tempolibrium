# balance.py: the machine only fires if this says OK
#   python balance.py seats.csv launch.json
import csv
import json
import sys


def load(path):
    return list(csv.DictReader(open(path)))


def time_residue(seats):
    # rule 1: sum of mass * days has to be zero
    total = 0.0
    for s in seats:
        total += float(s['mass_kg']) * int(s['days'])
    return total


def space_residue(seats, launch):
    # rule 2: mass-weighted average of the landings has to be the launch point
    m = sum(float(s['mass_kg']) for s in seats)
    lat = sum(float(s['mass_kg']) * float(s['lat']) for s in seats) / m
    lon = sum(float(s['mass_kg']) * float(s['lon']) for s in seats) / m
    return lat - launch[0], lon - launch[1]


if __name__ == '__main__':
    seats = load(sys.argv[1])
    launch = json.load(open(sys.argv[2]))['launch']
    r = time_residue(seats)
    dlat, dlon = space_residue(seats, launch)
    print 'time residue: %.2f kg-days' % r
    print 'space residue: %.5f, %.5f deg' % (dlat, dlon)
    print 'OK' if abs(r) < 0.01 and abs(dlat) < 1e-4 and abs(dlon) < 1e-4 else 'NOT BALANCED'
