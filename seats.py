# seats.py: read the five load cells (arduino on COM3), 2 decimals
# stand on it with your bag. yes, with the bag.
import serial
import time

PORT = 'COM3'


def read_all(n=5):
    s = serial.Serial(PORT, 9600, timeout=2)
    time.sleep(2)  # arduino resets on connect
    out = []
    for i in range(n):
        s.write('R%d\n' % (i + 1))
        out.append(round(float(s.readline().strip()), 2))
    s.close()
    return out


if __name__ == '__main__':
    for i, m in enumerate(read_all(), 1):
        print 'seat %d: %.2f kg' % (i, m)
