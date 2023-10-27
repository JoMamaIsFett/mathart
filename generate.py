import math
import numpy as np
import os
sign = lambda z: math.copysign(1, z)


x = y = a = b = c = d = 0

formel = input("1: -0.8 - 0.1 * x + 1.1 * x * x - 1.2 * x * y + 0.3 * y + 1.1 * y * y, 0.3 * x + 0.4 * x * x + 0.2 * x * y - 1.1 * y + 0.7 * y * y\n"
               "2: math.sin(x * y / b) * y + math.cos(a * x - y), x + math.sin(y) / b\n"
               "3: math.sin(a * y) + c * math.cos(a * x), math.sin(b * x) + d * math.cos(b * y)\n"
               "4: math.sin(y * b) + c * math.sin(x * b), math.sin(x * a) + d * math.sin(y * a)\n"
               "5: y - 1 - math.sqrt(abs(b * x - 1 - c)) * sign(x - 1), a - x - 1\n"
               "6: math.cos(y * b) + c * math.sin(x * b), math.cos(x * a) + d * math.sin(y * a)\n"
               "7: math.cos(y * b) + c * math.cos(x * b), math.cos(x * a) + d * math.cos(y * a)\n"
               "8: math.sin(y * b) + c * math.cos(x * b), math.cos(x * a) + d * math.sin(y * a)\n"
               "9: d * math.sin(x * a) - math.sin(y * b), c * math.cos(x * a) + math.cos(y * b)\n"
               "10: math.sin(y * a) - math.cos(x * b), math.sin(x * c) - math.cos(y * d)\n"
               "Select: ")
formel = int(formel)

os.system('cls' if os.name == 'nt' else 'clear')

if formel == 1:
    x, y = 0.0, 0.0
    a, b, c, d = 0, 0, 0, 0
elif formel == 2:
    werte = input("1: a, b = -0.81, -0.92\n"
                  "2: a, b = 0.65343, 0.7345345\n"
                  "3: a, b = -0.64, 0.76\n"
                  "4: a, b = 0.06, 0.98\n"
                  "5: a, b = -0.67, 0.83\n"
                  "Select: ")
    werte = int(werte)
    x, y = 1.0, 1.0
    if werte == 1:
        a, b, c, d = -0.81, -0.92, 0, 0
    elif werte == 2:
        a, b, c, d = 0.65343, 0.7345345, 0, 0
    elif werte == 3:
        a, b, c, d = -0.64, 0.76, 0, 0
    elif werte == 4:
        a, b, c, d = 0.06, 0.98, 0, 0
    elif werte == 5:
        a, b, c, d = -0.67, 0.83, 0, 0
elif formel == 3:
    werte = input("1: a, b, c, d = -1.7, 1.3, -0.1, -1.21\n"
                  "2: a, b, c, d = -1.7, 1.8, -0.9, -0.4\n"
                  "3: a, b, c, d = 1.5, -1.8, 1.6, 2\n"
                  "4: a, b, c, d = -2.239, -2.956, 1.272, 1.419\n"
                  "5: a, b, c, d = -1.7, 1.8, -1.9, -0.4\n"
                  "Select: ")
    werte = int(werte)
    x, y = 0.1, 0.1
    if werte == 1:
        a, b, c, d = -1.7, 1.3, -0.1, -1.21
    elif werte == 2:
        a, b, c, d = -1.7, 1.8, -0.9, -0.4
    elif werte == 3:
        a, b, c, d = 1.5, -1.8, 1.6, 2
    elif werte == 4:
        a, b, c, d = -2.239, -2.956, 1.272, 1.419
    elif werte == 5:
        a, b, c, d = -1.7, 1.8, -1.9, -0.4
elif formel == 4:
    werte = input("1: a, b, c, d = -0.966918, 2.879879, 0.765145, 0.744728\n"
                  "2: a, b, c, d = -2.9585, -2.2965, -2.8829, -0.1622\n"
                  "3: a, b, c, d = -2.8276, 1.2813, 1.9655, 0.597\n"
                  "4: a, b, c, d = -1.1554, -2.3419, -1.9799, 2.1828\n"
                  "5: a, b, c, d = -1.9956, -1.4528, -2.6206, 0.8517\n"
                  "Select: ")
    werte = int(werte)
    x, y = 0.1, 0.1
    if werte == 1:
        a, b, c, d = -0.966918, 2.879879, 0.765145, 0.744728
    elif werte == 2:
        a, b, c, d = -2.9585, -2.2965, -2.8829, -0.1622
    elif werte == 3:
        a, b, c, d = -2.8276, 1.2813, 1.9655, 0.597
    elif werte == 4:
        a, b, c, d = -1.1554, -2.3419, -1.9799, 2.1828
    elif werte == 5:
        a, b, c, d = -1.9956, -1.4528, -2.6206, 0.8517
elif formel == 5:
    werte = input("1: a, b, c = 7.16878197155893, 8.43659746693447, 2.55983412731439\n"
                  "2: a, b, c = 7.7867514709942, 0.132189802825451, 8.14610984409228\n"
                  "3: a, b, c = 9.74546888144687, 1.56320227775723, 7.86818214459345\n"
                  "4: a, b, c = 9.8724800767377, 8.66862616268918, 8.66950439289212\n"
                  "5: a, b, c = 9.7671244922094, 4.10973468795419, 3.78332691499963\n"
                  "Select: ")
    x, y = 0.0, 0.0
    werte = int(werte)
    if werte == 1:
        a, b, c, d = 7.16878197155893, 8.43659746693447, 2.55983412731439, 0
    elif werte == 2:
        a, b, c, d = 7.7867514709942, 0.132189802825451, 8.14610984409228, 0
    elif werte == 3:
        a, b, c, d = 9.74546888144687, 1.56320227775723, 7.86818214459345, 0
    elif werte == 4:
        a, b, c, d = 9.8724800767377, 8.66862616268918, 8.66950439289212, 0
    elif werte == 5:
        a, b, c, d = 9.7671244922094, 4.10973468795419, 3.78332691499963, 0
elif formel == 6:
    werte = input("1: a, b, c, d = 2.6, -2.5995, -2.9007, 0.3565\n"
                  "2: a, b, c, d = 1.8285, -1.8539, 0.3816, 1.9765\n"
                  "3: a, b, c, d = 2.5425, 2.8358, -0.8721, 2.7044\n"
                  "4: a, b, c, d = -1.8669, 1.2768, -2.9296, -0.4121\n"
                  "5: a, b, c, d = -2.7918, 2.1196, 1.0284, 0.1384\n"
                  "Select: ")
    werte = int(werte)
    x, y = 0.1, 0.1
    if werte == 1:
        a, b, c, d = 2.6, -2.5995, -2.9007, 0.3565
    elif werte == 2:
        a, b, c, d = 1.8285, -1.8539, 0.3816, 1.9765
    elif werte == 3:
        a, b, c, d = 2.5425, 2.8358, -0.8721, 2.7044
    elif werte == 4:
        a, b, c, d = -1.8669, 1.2768, -2.9296, -0.4121
    elif werte == 5:
        a, b, c, d = -2.7918, 2.1196, 1.0284, 0.1384
elif formel == 7:
    werte = input("1: a, b, c, d = 1.546, 1.929, 1.09, 1.41\n"
                  "2: a, b, c, d = 2.907, -1.9472, 1.2833, 1.3206\n"
                  "3: a, b, c, d = 0.8875, 0.7821, -2.3262, 1.5379\n"
                  "4: a, b, c, d = -2.4121, -1.0028, -2.2386, 0.274\n"
                  "5: a, b, c, d = -2.9581, 0.927, 2.7842, 0.6267\n"
                  "Select: ")
    werte = int(werte)
    x, y = 0.1, 0.1
    if werte == 1:
        a, b, c, d = 1.546, 1.929, 1.09, 1.41
    elif werte == 2:
        a, b, c, d = 2.907, -1.9472, 1.2833, 1.3206
    elif werte == 3:
        a, b, c, d = 0.8875, 0.7821, -2.3262, 1.5379
    elif werte == 4:
        a, b, c, d = -2.4121, -1.0028, -2.2386, 0.274
    elif werte == 5:
        a, b, c, d = -2.9581, 0.927, 2.7842, 0.6267
elif formel == 8:
    werte = input("1: a, b, c, d = 2.0246, -1.323, -2.8151, 0.2277\n"
                  "2: a, b, c, d = 1.4662, -2.3632, -0.4167, 2.4162\n"
                  "3: a, b, c, d = -2.7564, -1.8234, 2.8514, -0.8745\n"
                  "4: a, b, c, d = -2.218, 1.4318, -0.3346, 2.4993\n"
                  "5: a, b, c, d = 1.2418, -2.4174, -0.7112, -1.9802\n"
                  "Select: ")
    werte = int(werte)
    x, y = 0.1, 0.1
    if werte == 1:
        a, b, c, d = 2.0246, -1.323, -2.8151, 0.2277
    elif werte == 2:
        a, b, c, d = 1.4662, -2.3632, -0.4167, 2.4162
    elif werte == 3:
        a, b, c, d = -2.7564, -1.8234, 2.8514, -0.8745
    elif werte == 4:
        a, b, c, d = -2.218, 1.4318, -0.3346, 2.4993
    elif werte == 5:
        a, b, c, d = 1.2418, -2.4174, -0.7112, -1.9802
elif formel == 9:
    werte = input("1: a, b, c, d = 1.40, 1.56, 1.40, -6.56\n"
                  "2: a, b, c, d = -2.538, 1.362, 1.315, 0.513\n"
                  "3: a, b, c, d = 1.913, 2.796, 1.468, 1.01\n"
                  "4: a, b, c, d = -2.337, -2.337, 0.533, 1.378\n"
                  "5: a, b, c, d = -2.722, 2.574, 1.284, 1.043\n"
                  "6: a, b, c, d = 1.4, -2.3, 2.4, -2.1\n"
                  "Select: ")
    werte = int(werte)
    x, y = 0.1, 0.1
    if werte == 1:
        a, b, c, d = 1.40, 1.56, 1.40, -6.56
    elif werte == 2:
        a, b, c, d = -2.538, 1.362, 1.315, 0.513
    elif werte == 3:
        a, b, c, d = 1.913, 2.796, 1.468, 1.01
    elif werte == 4:
        a, b, c, d = -2.337, -2.337, 0.533, 1.378
    elif werte == 5:
        a, b, c, d = -2.722, 2.574, 1.284, 1.043
    elif werte == 6:
        a, b, c, d = 1.4, -2.3, 2.4, -2.1
elif formel == 10:
    werte = input("1: a, b, c, d = 0.970, -1.899, 1.381, -1.506\n"
                  "2: a, b, c, d = 1.4, -2.3, 2.4, -2.1\n"
                  "3: a, b, c, d = 2.01, -2.53, 1.61, -0.33\n"
                  "4: a, b, c, d = -2.7, -0.09, -0.86, -2.2\n"
                  "5: a, b, c, d = -0.827, -1.637, 1.659, -0.943\n"
                  "6: a, b, c, d = -2, -2, -1.2, 2\n"
                  "7: a, b, c, d = -0.709, 1.638, 0.452, 1.740\n"
                  "Select: ")
    werte = int(werte)
    x, y = 0.1, 0.1
    if werte == 1:
        a, b, c, d = 0.970, -1.899, 1.381, -1.506
    elif werte == 2:
        a, b, c, d = 1.4, -2.3, 2.4, -2.1
    elif werte == 3:
        a, b, c, d = 2.01, -2.53, 1.61, -0.33
    elif werte == 4:
        a, b, c, d = -2.7, -0.09, -0.86, -2.2
    elif werte == 5:
        a, b, c, d = -0.827, -1.637, 1.659, -0.943
    elif werte == 6:
        a, b, c, d = -2, -2, -1.2, 2
    elif werte == 7:
        a, b, c, d = -0.709, 1.638, 0.452, 1.740

os.system('cls' if os.name == 'nt' else 'clear')

punkte = [(x, y)]

prozent = 0
anzahl = 100000


def eingabe():
    global anzahl
    anzahl = input("Point number: ")
    try:
        anzahl = int(anzahl)
        if anzahl <= 0:
            print("Input has to be positiv and bigger than 0")
            eingabe()
        else:
            pass

    except:
        print("Input has to be a positiv number")
        eingabe()


def berechnen(x, y):
    if formel == 1:
        return -0.8 - 0.1 * x + 1.1 * x * x - 1.2 * x * y + 0.3 * y + 1.1 * y * y, 0.3 * x + 0.4 * x * x + 0.2 * x * y - 1.1 * y + 0.7 * y * y
    elif formel == 2:
        return math.sin(x * y / b) * y + math.cos(a * x - y), x + math.sin(y) / b
    elif formel == 3:
        return math.sin(a * y) + c * math.cos(a * x), math.sin(b * x) + d * math.cos(b * y)
    elif formel == 4:
        return math.sin(y * b) + c * math.sin(x * b), math.sin(x * a) + d * math.sin(y * a)
    elif formel == 5:
        return y - 1 - math.sqrt(abs(b * x - 1 - c)) * sign(x - 1), a - x - 1
    elif formel == 6:
        return math.cos(y * b) + c * math.sin(x * b), math.cos(x * a) + d * math.sin(y * a)
    elif formel == 7:
        return math.cos(y * b) + c * math.cos(x * b), math.cos(x * a) + d * math.cos(y * a)
    elif formel == 8:
        return math.sin(y * b) + c * math.cos(x * b), math.cos(x * a) + d * math.sin(y * a)
    elif formel == 9:
        return d * math.sin(x * a) - math.sin(y * b), c * math.cos(x * a) + math.cos(y * b)
    elif formel == 10:
        return math.sin(y * a) - math.cos(x * b), math.sin(x * c) - math.cos(y * d)


#eingabe()

for i in range(anzahl):
    xalt, yalt = punkte[len(punkte) - 1]
    newpoint = berechnen(xalt, yalt)
    punkte.append(newpoint)
    pos = int((i + 1) / anzahl * 100)
    if pos <= prozent:
        pass
    else:
        prozent = pos
        print(prozent, "% finished")

print("Saving...")

np.save('points.npy', punkte)

print("Finished!")


# https://softologyblog.wordpress.com/2017/03/04/2d-strange-attractors/


# x, y = 0.0, 0.0
# -0.8 - 0.1 * x + 1.1 * x * x - 1.2 * x * y + 0.3 * y + 1.1 * y * y,
#                   0.3 * x + 0.4 * x * x + 0.2 * x * y - 1.1 * y + 0.7 * y * y

# x, y = 1.0, 1.0
# -1 < a, b < 1
# math.sin(x * y / b) * y + math.cos(a * x - y), x + math.sin(y) / b
# a, b, c, d = -0.81, -0.92, 0, 0
# a, b, c, d = 0.65343, 0.7345345, 0, 0
# a, b, c, d = -0.64, 0.76, 0, 0
# a, b, c, d = 0.06, 0.98, 0, 0
# a, b, c, d = -0.67, 0.83, 0, 0

# x, y = 0.1, 0.1
# -3 < a, b, c, d < 3
# math.sin(a * y) + c * math.cos(a * x), math.sin(b * x) + d * math.cos(b * y)
# a, b, c, d = -1.7, 1.3, -0.1, -1.21
# a, b, c, d = -1.7, 1.8, -0.9, -0.4
# a, b, c, d = 1.5, -1.8, 1.6, 2
# a, b, c, d = -2.239, -2.956, 1.272, 1.419
# a, b, c, d = -1.7, 1.8, -1.9, -0.4

# x, y = 0.1, 0.1
# -3 < a, b < 3
# -0.5 < c, d < 1.5
# math.sin(y * b) + c * math.sin(x * b), math.sin(x * a) + d * math.sin(y * a)
# a, b, c, d = -0.966918, 2.879879, 0.765145, 0.744728
# a, b, c, d = -2.9585, -2.2965, -2.8829, -0.1622
# a, b, c, d = -2.8276, 1.2813, 1.9655, 0.597
# a, b, c, d = -1.1554, -2.3419, -1.9799, 2.1828
# a, b, c, d = -1.9956, -1.4528, -2.6206, 0.8517

# x, y = 0.0, 0.0
# 0 < a, b, c < 10
# y - 1 - math.sqrt(abs(b * x - 1 - c)) * sign(x - 1), a - x - 1
# a, b, c, d = 7.16878197155893, 8.43659746693447, 2.55983412731439, 0
# a, b, c, d = 7.7867514709942, 0.132189802825451, 8.14610984409228, 0
# a, b, c, d = 9.74546888144687, 1.56320227775723, 7.86818214459345, 0
# a, b, c, d = 9.8724800767377, 8.66862616268918, 8.66950439289212, 0
# a, b, c, d = 9.7671244922094, 4.10973468795419, 3.78332691499963, 0

# x, y = 0.1, 0.1
# -3 < a, b, c, d < 3
# math.cos(y * b) + c * math.sin(x * b), math.cos(x * a) + d * math.sin(y * a)
# a, b, c, d = 2.6, -2.5995, -2.9007, 0.3565
# a, b, c, d = 1.8285, -1.8539, 0.3816, 1.9765
# a, b, c, d = 2.5425, 2.8358, -0.8721, 2.7044
# a, b, c, d = -1.8669, 1.2768, -2.9296, -0.4121
# a, b, c, d = -2.7918, 2.1196, 1.0284, 0.1384

# x, y = 0.1, 0.1
# -3 < a, b, c, d < 3
# math.cos(y * b) + c * math.cos(x * b), math.cos(x * a) + d * math.cos(y * a)
# a, b, c, d = 1.546, 1.929, 1.09, 1.41
# a, b, c, d = 2.907, -1.9472, 1.2833, 1.3206
# a, b, c, d = 0.8875, 0.7821, -2.3262, 1.5379
# a, b, c, d = -2.4121, -1.0028, -2.2386, 0.274
# a, b, c, d = -2.9581, 0.927, 2.7842, 0.6267

# x, y = 0.1, 0.1
# -3 < a, b, c, d < 3
# math.sin(y * b) + c * math.cos(x * b), math.cos(x * a) + d * math.sin(y * a)
# a, b, c, d = 2.0246, -1.323, -2.8151, 0.2277
# a, b, c, d = 1.4662, -2.3632, -0.4167, 2.4162
# a, b, c, d = -2.7564, -1.8234, 2.8514, -0.8745
# a, b, c, d = -2.218, 1.4318, -0.3346, 2.4993
# a, b, c, d = 1.2418, -2.4174, -0.7112, -1.9802

# x, y = 0.1, 0.1
# -3 < a, b, c, d < 3
# d * math.sin(x * a) - math.sin(y * b), c * math.cos(x * a) + math.cos(y * b)
# a, b, c, d = 1.40, 1.56, 1.40, -6.56
# a, b, c, d = -2.538, 1.362, 1.315, 0.513
# a, b, c, d = 1.913, 2.796, 1.468, 1.01
# a, b, c, d = -2.337, -2.337, 0.533, 1.378
# a, b, c, d = -2.722, 2.574, 1.284, 1.043
# a, b, c, d = 1.4, -2.3, 2.4, -2.1

# x, y = 0.1, 0.1
# -3 < a, b, c, d < 3
# math.sin(y * a) - math.cos(x * b), math.sin(x * c) - math.cos(y * d)
# a, b, c, d = 0.970, -1.899, 1.381, -1.506
# a, b, c, d = 1.4, -2.3, 2.4, -2.1
# a, b, c, d = 2.01, -2.53, 1.61, -0.33
# a, b, c, d = -2.7, -0.09, -0.86, -2.2
# a, b, c, d = -0.827, -1.637, 1.659, -0.943
# a, b, c, d = -2, -2, -1.2, 2
# a, b, c, d = -0.709, 1.638, 0.452, 1.740
