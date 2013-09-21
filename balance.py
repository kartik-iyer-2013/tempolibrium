# balance.py: the machine only fires if this says OK
#   python balance.py seats.csv launch.json
# seat 5 is AUTO: leave its days/lat/lon as AUTO and this fills them in.
import csv
import json
import sys


def load(path):
    return list(csv.DictReader(open(path)))


def fixed(seats):
    return [s for s in seats if s['days'] != 'AUTO']


def fill_auto(seats, launch):
    auto = [s for s in seats if s['days'] == 'AUTO'][0]
    m_auto = float(auto['mass_kg'])
    m_all = sum(float(s['mass_kg']) for s in seats)
    rest = fixed(seats)
    # rule 1: AUTO takes whatever time the others leave unbalanced
    days = -sum(float(s['mass_kg']) * int(s['days']) for s in rest) / m_auto
    # rule 2: and whatever place
    lat = (m_all * launch[0] - sum(float(s['mass_kg']) * float(s['lat']) for s in rest)) / m_auto
    lon = (m_all * launch[1] - sum(float(s['mass_kg']) * float(s['lon']) for s in rest)) / m_auto
    auto['days'], auto['lat'], auto['lon'] = int(round(days)), lat, lon
    return auto


if __name__ == '__main__':
    seats = load(sys.argv[1])
    launch = json.load(open(sys.argv[2]))['launch']
    a = fill_auto(seats, launch)
    print 'AUTO (%s): %+d days, lands at %.4f, %.4f' % (a['name'], a['days'], a['lat'], a['lon'])
