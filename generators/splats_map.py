#!/usr/bin/env python

from wadinfo import WI_LUMP_OFFSETS, WI_LUMP_SIZES

# From wi_stuff.c in the Doom source.
DOOM_LEVEL_LOCATIONS = [
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

# From in_lude.c in the Heretic source code:
HERETIC_LEVEL_LOCATIONS = [
    (
        (172, 78),
        (86, 90),
        (73, 66),
        (159, 95),
        (148, 126),
        (132, 54),
        (131, 74),
        (208, 138),
        (52, 101)
    ),
    (
        (218, 57),
        (137, 81),
        (155, 124),
        (171, 68),
        (250, 86),
        (136, 98),
        (203, 90),
        (220, 140),
        (279, 106)
    ),
    (
        (86, 99),
        (124, 103),
        (154, 79),
        (202, 83),
        (178, 59),
        (142, 58),
        (219, 66),
        (247, 57),
        (107, 80)
    )
]

def draw_episode(filename, levels, lumpname):
	cmdline = "convert -size 320x200 'xc:#0000e3'"

	sploffset = WI_LUMP_OFFSETS[lumpname]
	splsize = WI_LUMP_SIZES[lumpname]
	for index, (x, y) in enumerate(levels):
		cmdline += " -fill white -stroke black"
		left, top = x - sploffset[0], y - sploffset[1]
		right, bottom = left + splsize[0], top + splsize[1]
		cmdline += " -draw 'rectangle %d,%d %d,%d'" % (
			left, top, right, bottom)

		cmdline += " -stroke none -fill black"
		cmdline += " -draw 'text %d,%d \"%d\"'" % (
			(left + right - 6) / 2,
			(top + bottom + 10) / 2,
			index + 1)

	cmdline += " " + filename
	return cmdline

for index, episode in enumerate(DOOM_LEVEL_LOCATIONS):
	print(draw_episode(
		"doom_e%d.gif" % (index + 1),
		episode,
		"WISPLAT"
	))

for index, episode in enumerate(HERETIC_LEVEL_LOCATIONS):
	print(draw_episode(
		"htic_e%d.gif" % (index + 1),
		episode,
		"IN_X"
	))

