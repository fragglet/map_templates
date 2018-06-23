

BOX_MIN_W = 15
BOX_CHAR_W = 6
BOX_H = 20

ANIMATION_LOCATIONS = (
    (
        ("0", 224, 104),
        ("1", 184, 160),
        ("2", 112, 136),
        ("3", 72, 112),
        ("4", 88, 96),
        ("5", 64, 48),
        ("6", 192, 40),
        ("7", 136, 16),
        ("8", 80, 16),
        ("9", 64, 24),
    ),
    (
        ("0-6 & 8", 128, 136),
        ("7", 192, 144),
    ),
    (
        ("0", 104, 168),
        ("1", 40, 136),
        ("2", 160, 96),
        ("3", 104, 80),
        ("4", 120, 32),
        ("5", 40, 0),
    ),
)

def draw_episode(filename, levels):
	cmdline = "convert -size 320x200 'xc:#7a7' -stroke none"
	for label, x, y in levels:
		w = BOX_MIN_W + BOX_CHAR_W * len(label)
		cmdline += " -fill white"
		cmdline += " -draw 'rectangle %d,%d %d,%d'" % (
			x, y, x + w, y + BOX_H)
		cmdline += " -fill black"
		cmdline += " -draw 'text %d,%d \"%s\"'" % (
			x + 7, y + 12, label)
		cmdline += " -draw 'line %d,%d %d,%d'" % (
			x, y, x + w, y)
		cmdline += " -draw 'line %d,%d %d,%d'" % (
			x, y, x, y + BOX_H)

	cmdline += " " + filename
	return cmdline

for index, episode in enumerate(ANIMATION_LOCATIONS):
	print(draw_episode("anims%d.gif" % index, episode))


