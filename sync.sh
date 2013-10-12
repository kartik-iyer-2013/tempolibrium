#!/bin/sh
# after launch: push the seat-cam frames to the box, so someone can find them
# accounts: first name, lowercase
rsync -av seatcam/ "$USER"@tempolibrium.devclub.in:~/run/
