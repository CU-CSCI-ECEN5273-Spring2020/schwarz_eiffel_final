import numpy as np
import matplotlib.pyplot as plt

#test_eiffel_avgs.csv contains avg cpu idle for the 5 tests
with open('test_eiffel_avgs.csv') as f:
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [float(numeric_string) for numeric_string in x]
    f.close()

#test_eiffel_mod_avgs.csv contains avg cpu idle for the 5 tests for eiffel with modification
with open('test_eiffel_mod_avgs.csv') as f:
    lines = f.readlines()
    x1 = [line.split()[0] for line in lines]
    y1 = [float(numeric_string) for numeric_string in x1]
    f.close()

#dstat logged once every second so this is easier, as long as 0 starts when the test is started
time = np.arange(len(x))

fig, ax = plt.subplots()
ax.plot(time, y, label="Eiffel + Bucket Gran. Search")
ax.plot(time, y1, label="Eiffel")

ax.legend()

ax.set(xlabel='Time (s)', ylabel='CPU Idle',
       title='Eiffel vs Eiffel + Extension')
ax.grid()

fig.savefig("test.png")
plt.show()

#this is the average difference between the TWO AVERAGES of all tests
print np.mean(y) - np.mean(y1)
