#Importing Libraries
import scipy.io
import numpy as np
from matplotlib import pyplot as plt

#Importing Datasets
file_names = ["NBI(1e1)(1e1)","NBI(1e2)(1e2)","NBI(1e3)(1e3)","NBI(1e4)(1e4)","NBI(1e5)(1e5)","NBI(5e5)(5e5)","NBI(1e6)(1e6)","NBI(3e6)(3e6)","NBI(5e6)(5e6)","NBI(7e6)(7e6)","NBI(1e7)(1e7)"]
dataset = []
for i in range(len(file_names)):
    dataset.append(scipy.io.loadmat("/Users/tomfitzgerald/Desktop/Python/Plasma Measurement and Data Analysis/Metis/Datasets/"+file_names[i]+".mat"))

#Functions
def list_subsections(dataset):
    print("subsections (I'm using zerod by default):")
    print(dataset['post'].dtype)

def list_indexes(dataset,subsection='zerod'):
    print("indexes in subsection " + subsection + ":")
    print(dataset['post']['zerod'][0][0].dtype)


def get_variable(dataset,index, subsection='zerod'):
    a = dataset['post'][subsection][0][0][index][0][0]
    a = [float(x[0]) for x in a]
    return a

def get_average(dataset,start, end, index, subsection='zerod'):
    a = get_variable(dataset,index, subsection=subsection)
    return (np.mean(a[start:end]), np.std(a[start:end]))

if __name__ == '__main__':
    average = []
    values = ["ne0","te0","taue"]
    for i in range(len(dataset)):
        mean,_ = get_average(dataset[i],30,100,"taue")
        average.append(mean)

    #Plotting
    plt.figure(1)
    plt.plot([1e1,1e2,1e3,1e4,1e5,5e5,1e6,3e6,5e6,7e6,1e7],average,"x-")
    plt.xlabel(r"Neutral Beam Injection Power $(W)$") ; plt.ylabel(r"Energy Confinement Time $(s)$")
    plt.title(r"$\tau_{e}$ vs NBI Power")

    plt.figure(2)
    plt.plot(get_variable(dataset[4],'taue'))

    plt.show()
