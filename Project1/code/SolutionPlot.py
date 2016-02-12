# Plotting program for PHY 480 project 1
# Plots calculated and actual solutions of poisson equation
# Written by: Noah Green
# Date: 1/29/2016
# Last Modified: 2/11/2016

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.lines as line
import GetCoords

def main():
    # Open file with filenames
    try:
        file_file = open( "CoordFiles.txt", "r" )
    except FileNotFoundError:
        print("Error: file not found\n")
    filename_list = []
    for line in file_file:
        filename_list.append(line.strip())
    
    count = 0
    for filename in filename_list:
        count += 1
        fig_name = "solution"+str(count)+".png"
        # Get coordinates from file
        print(filename)
        coords_tuple = GetCoords.get_coords( filename )

        # Get plot boundaries ( 10% beyond max/min of graphs )
        x_min = 1.1*min( coords_tuple[0] )
        y_min = 1.1*min( ( min(coords_tuple[1]), min(coords_tuple[2]) ) )
        x_max = 1.1*max( coords_tuple[0] )
        y_max = 1.1*max( ( max(coords_tuple[1]), max(coords_tuple[2]) ) )

        # Make plot
        plt.plot( coords_tuple[0], coords_tuple[1], label = "Actual" )
        plt.plot( coords_tuple[0], coords_tuple[2], label = "Calculated" )
        plt.axis( [x_min, x_max, y_min, y_max] )
        plt.legend( loc = 7 )
        plt.xlabel( 'Independent Variable' )
        plt.ylabel( 'Dependent Variable' )
        plt.title( 'Exact and Calculated Solutions to Poisson Equation' )
        plt.savefig(fig_name)
        plt.clf()
        
    

main()
