is_planet = False
is_star = False
has_light = True

if is_planet or is_star:
    print("Wow! It's inside the Galaxy.")
elif not is_star and has_light:
    print("Yeah! That might be white or red dwarf.")
else:
    print("Whoops! That might be a black hole.")
