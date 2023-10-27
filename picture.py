import numpy as np
from PIL import Image, ImageDraw
import math


def eingabe(was, neg):
    while True:
        wert = input(was)

        try:
            wert = float(wert)

            if neg:
                return wert
            else:
                if wert <= 0.0:
                    print("Input has to be positive and greater than 0")
                else:
                    return wert

        except ValueError:
            print("Input has to be a positive number")


density = eingabe("density: ", False)
zoom = eingabe("zoom: ", False)
xoffset = eingabe("x offset: ", True)
yoffset = eingabe("y offset: ", True)


punkte = np.load("points.npy")

width = height = int((math.sqrt(len(punkte)) / density))
xmitte = width / 2
ymitte = height / 2

werte = [item for tupel in punkte for item in tupel]
maxwert = max(werte)
minwert = min(werte)
step = 255 / (maxwert - minwert)
werte.clear()

prozent = 0
anzahl = len(punkte)
stelle = 0

image = Image.new("RGB", (int(width), int(height)), (245, 255, 252))
draw = ImageDraw.Draw(image)

faktor = width / 1000

for punkt in punkte:
    x, y = punkt
    xpos = int(xmitte + faktor * (x * zoom + xoffset))
    ypos = int(ymitte + faktor * (y * zoom + yoffset))
    draw.point((xpos, ypos), fill=(int((x - minwert) * step), int((y - minwert) * step), int((y + x - 2 * minwert) * (step / 4))))

    pos = int((stelle + 1) / anzahl * 100)
    if pos <= prozent:
        pass
    else:
        prozent = pos
        print(prozent, "% finished")
    stelle += 1

print("Saving...")

image.save("output.png", "PNG")

print("Finished!")
