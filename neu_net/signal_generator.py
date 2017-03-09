import math
import matplotlib.pyplot as plt

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def generate_cos(number_of_samples):
    signal = list()
    for i in frange(0.0, math.pi/2, 0.1):
        print i
        #signal.append(float(math.cos(float(i))))
        signal.append(float(2)*float(i) + float(2))
        #signal.append(2 * (float(i) + float(i)*float(i)))
    return signal

# def generate(number_of_samples):
#     signal = list()
#     for i in range(10):
#         signal.append(math.cos(float(float(i)*0.314)))
#     return signal

# def generate_samples(number_of_samples):
#     samples = list()
#     for i in range(10):
#         samples.append(float(float(i)*0.314))
#     return samples



def generate_samples(number_of_samples):
    samples = list()
    for i in frange(0.0, math.pi/2, 0.1):
        samples.append(i)
    return samples

def plot_sth(x, y, x_title, y_title, title):
    plt.plot(x, y, 'r')
    plt.ylabel(y_title)
    plt.xlabel(x_title)
    plt.title(title)
    plt.grid()
    plt.show()



