import numpy as np                       # import library as alias
from astropy.table import Table

def main():
    # np.linspace:
    x = np.linspace(0, 2*np.pi, 1000)    # define x
    y = np.sin(x)                        # define y

    data_table = Table()
    data_table["x"] = x
    data_table["y"] = y

    #data_table["x"].format = "{:.3f}"
    #data_table["y"].format = "{:.3f}"

    print(data_table)                    # print table!!


# if the main function exists, run it
if __name__ == '__main__':
	main()