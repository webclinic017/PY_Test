
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.01)

ax1 = plt.subplot(311)
ax1.plot(t, np.sin(2*np.pi*t))

ax2 = plt.subplot(312, sharex=ax1)
ax2.plot(t, np.sin(3*np.pi*t))

ax3 = plt.subplot(313, sharex=ax1)
ax3.plot(t, np.sin(4*np.pi*t))

plt.show()