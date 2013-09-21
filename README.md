# tempolibrium

PAC roof project. seat controller + balancer. python 2.7, runs on the old thinkpad.

Tempolibrium is a one-time explosion in space-time. It must preserve the center of space-time.

## rules (the machine refuses to fire otherwise)

1. **centre in time.** over all seats, the sum of mass_kg x days_jumped is zero. if someone goes forward, someone goes back.
2. **centre in space.** the mass-weighted average of everyone's landing point is the launch point.
3. everyone arrives at 18:13 (launch clock). one way. it fires once.
4. seat 5 is AUTO. whoever sits there takes the remainder, in time and in place, so 1 and 2 close.

## files

- `seats.py` reads the five load cells
- `balance.py` checks rules 1 and 2, fills in AUTO
- `sync.sh` pushes seat-cam frames to the box after launch

the launch point is in `launch.json`, which is not in this repo.
