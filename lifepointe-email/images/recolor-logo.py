from PIL import Image

im = Image.open('logo.webp').convert('RGBA')
W, H = im.size
px = im.load()

# 1. Locate the green "& WELLNESS CENTER" banner so its white text stays white.
gx0, gy0, gx1, gy1 = W, H, 0, 0
for y in range(H):
    for x in range(W):
        r, g, b, a = px[x, y]
        if a > 40 and g > 90 and g - r > 30 and g - b > 30:
            gx0, gy0 = min(gx0, x), min(gy0, y)
            gx1, gy1 = max(gx1, x), max(gy1, y)
print('green banner bbox:', gx0, gy0, gx1, gy1)

NAVY = (61, 67, 124)  # #3d437c

def whitish(r, g, b):
    return min(r, g, b) > 175 and (max(r, g, b) - min(r, g, b)) < 45

recolored = 0
for y in range(H):
    in_banner_row = gy0 - 4 <= y <= gy1 + 4
    for x in range(W):
        r, g, b, a = px[x, y]
        if a == 0:
            continue
        if in_banner_row and gx0 - 4 <= x <= gx1 + 4:
            continue  # leave the green banner and its white text alone
        if whitish(r, g, b):
            px[x, y] = (*NAVY, a)
            recolored += 1
print('pixels recolored:', recolored)

im.save('logo-navy-full.png')
im.resize((440, 166), Image.LANCZOS).save('lifepointe-logo-440.png')
im.resize((880, 332), Image.LANCZOS).save('lifepointe-logo-880.png')
