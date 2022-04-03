import matplotlib.pyplot as plt

minmum = -10
maxmum = 10
xpoints1 = list(range(minmum, 1))
xpoints2 = list(range(1, maxmum))
ypoints1 = []
ypoints2 = []
for i in xpoints1:
    ypoints1.append(10/(i-1))
for i in xpoints2:
    ypoints2.append(3*i+3)

plt.plot(xpoints1, ypoints1)
plt.plot(xpoints2, ypoints2)

plt.show()

