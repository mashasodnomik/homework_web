for z in range(0, 2):
    for y in range(0, 2):
        for x in range(0, 2):
            for w in range(0, 2):
                F = not(((not z) or y) and (x+w)) or ((z==w) or (y and (not x)))
                if F is not True:
                    print(x, y, z, w, F)


for x in [True, False]:
    for y in [True, False]:
        for w in [True, False]:
            for z in [True, False]:
                F = (z<=y) or ()
                



