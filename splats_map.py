#!/usr/bin/env python

from wadinfo import WI_LUMP_OFFSETS, WI_LUMP_SIZES

# From wi_stuff.c in the Doom source.
LEVEL_LOCATIONS = [
    # Episode 0 World Map
    (
        ( 185, 164 ),   # location of level 0 (CJ)
        ( 148, 143 ),   # location of level 1 (CJ)
        ( 69, 122 ),    # location of level 2 (CJ)
        ( 209, 102 ),   # location of level 3 (CJ)
        ( 116, 89 ),    # location of level 4 (CJ)
        ( 166, 55 ),    # location of level 5 (CJ)
        ( 71, 56 ),     # location of level 6 (CJ)
        ( 135, 29 ),    # location of level 7 (CJ)
        ( 71, 24 )      # location of level 8 (CJ)
    ),
    # Episode 1 World Map should go here
    (
        ( 254, 25 ),    # location of level 0 (CJ)
        ( 97, 50 ),     # location of level 1 (CJ)
        ( 188, 64 ),    # location of level 2 (CJ)
        ( 128, 78 ),    # location of level 3 (CJ)
        ( 214, 92 ),    # location of level 4 (CJ)
        ( 133, 130 ),   # location of level 5 (CJ)
        ( 208, 136 ),   # location of level 6 (CJ)
        ( 148, 140 ),   # location of level 7 (CJ)
        ( 235, 158 )    # location of level 8 (CJ)
    ),
    # Episode 2 World Map should go here
    (
        ( 156, 168 ),   # location of level 0 (CJ)
        ( 48, 154 ),    # location of level 1 (CJ)
        ( 174, 95 ),    # location of level 2 (CJ)
        ( 265, 75 ),    # location of level 3 (CJ)
        ( 130, 48 ),    # location of level 4 (CJ)
        ( 279, 23 ),    # location of level 5 (CJ)
        ( 198, 48 ),    # location of level 6 (CJ)
        ( 140, 25 ),    # location of level 7 (CJ)
        ( 281, 136 )    # location of level 8 (CJ)
    )
]

def draw_episode(filename, levels):
	cmdline = "convert -size 320x200 xc:skyblue -fill white -stroke black"

	sploffset = WI_LUMP_OFFSETS['WISPLAT']
	splsize = WI_LUMP_SIZES['WISPLAT']
	for index, (x, y) in enumerate(levels):
		left, top = x - sploffset[0], y - sploffset[1]
		right, bottom = left + splsize[0], top + splsize[1]
		cmdline += " -draw 'rectangle %d,%d %d,%d'" % (
			left, top, right, bottom)
		cmdline += " -draw 'text %d,%d \"%d\"'" % (
			x, y, index + 1)

	cmdline += " " + filename
	return cmdline

for index, episode in enumerate(LEVEL_LOCATIONS):
	print(draw_episode("splats%d.gif" % index, episode))

