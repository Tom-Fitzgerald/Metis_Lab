# ---------- Importing Libraries ---------- #
import os
import scipy.io
import numpy as np
from matplotlib import pyplot as plt

# ---------- Functions ---------- #
def import_data(data_directory):
    """Loads .mat data into a list in alphabetical order of file name

    Args:
        data_directory (string): holds the pathname of the file in which the .mat data is stored

    Returns:
        tuple: returns the list of imported datasets as an imutable list
    """
    #List all the files in the directory
    file_list = os.listdir(data_directory)

    #Filter files to include only .mat files
    mat_files = [file for file in file_list if file.endswith('.mat')]

    #Sort the list of files aphabetically
    mat_files.sort()

    #Loop through each .mat file and load its contents
    mat_data = [] 
    for i in range(len(mat_files)):
        file_path = os.path.join(data_directory, mat_files[i])
        mat_data.append(scipy.io.loadmat(file_path))

    #Return a list containing all the datasets
    return mat_data
 
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

# ---------- Main Code ---------- #
if __name__ == '__main__':

    #Importing Datasets (Note that datasets are loaded in alphabetical order of file name)
    dataset = import_data("/Users/tomfitzgerald/Desktop/Python/Plasma Measurement and Data Analysis/Metis/Datasets")

    average = []
    for i in range(len(dataset)):
        mean,_ = get_average(dataset[i],40,100,"taue")
        average.append(mean)

    #Plotting
    plt.figure(1)
    plt.plot([1e1,1e2,1e3,1e4,1e5,5e5,1e6,3e6,5e6,7e6,1e7],average,"x-")
    plt.xlabel(r"Neutral Beam Injection Power $(W)$") ; plt.ylabel(r"Energy Confinement Time $(s)$")
    plt.title(r"$\tau_{e}$ vs NBI Power")

    plt.show()
