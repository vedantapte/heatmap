import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

# Function to generate a list of random coordinate points
# and store them in a file titled "coordinates.txt"
def generateCoordinatePointsFile():
    # Define the dimensions of our field
    xMin = -47
    xMax = 47
    yMin = -68
    yMax = 68
    
    # Create a file titled coordinates.txt
    with open("./coordinates.txt", "w") as c:

        # Add corners of our field as coordinate points
        # (-47, 68), (47, 68), (-47, -68), (47, 68)
        c.write("{x},{y}\n".format(x = str(xMin), y = str(yMin)))
        c.write("{x},{y}\n".format(x = str(xMin), y = str(yMax)))
        c.write("{x},{y}\n".format(x = str(xMax), y = str(yMin)))
        c.write("{x},{y}\n".format(x = str(xMax), y = str(yMax)))

        i = 0
        numPoints = 100
        
        # Randomly generate numPoints coordinate points,
        # and add them to the "coordinates.txt" file
        while i < numPoints:
            x = random.randint(xMin, xMax) # x coordinate
            y = random.randint(yMin, yMax) # y coordinate

            if (x,y) in [(xMin, yMin), (xMin, yMax), (xMax, yMin), (xMax, yMax)]:
                continue
            else:
                c.write("{x},{y}\n".format(x = str(x), y = str(y)))
                i += 1


# Function to generate a heat map given a
# file with x,y coordinate points
def generateHeatMap(file, showPoints, colorScheme):
    # Load the coordinates file
    x, y = np.loadtxt(file, delimiter=',', unpack=True)

    # Plot all the coordinate points
    if showPoints:
        plt.plot(x, y, 'o', markersize=1, markeredgecolor="black")

    # Generate our kernel density estimation
    kde = sns.kdeplot(
        x=x,
        y=y,
        shade=True,
        #shade_lowest=True,
        thresh=0.0,
        alpha=.8,
        n_levels = 20,
        cmap=colorScheme
    )

    # Plot the kernel density estimation
    plt.xlim(-47, 47)
    plt.ylim(-68, 68)
    # plt.grid()
    plt.show()


# generateCoordinatePointsFile()
generateHeatMap(
    file = './attackingMid.txt',
    showPoints = False,
    colorScheme = "viridis"
)


# SOURCES
# https://stackoverflow.com/questions/64055621/write-coordinates-to-txt-file-to-future-use-it-in-program
# https://cmdlinetips.com/2012/09/three-ways-to-write-text-to-a-file-in-python/#:~:text=To%20create%20and%20write%20to,a%20new%20file%20to%20write.&text=If%20you%20want%20to%20append,if%20it%20does%20not%20exist.
# https://seaborn.pydata.org/tutorial/color_palettes.html
# https://www.youtube.com/watch?v=N46zGdX_xsY
