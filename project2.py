
# scientific
import math
import numpy as np

# interpolate
from scipy.interpolate import Rbf
from scipy.stats.qmc import Halton

# plotting
import matplotlib.pyplot as plt



########### Algorithm encapsulation #############

class InterpolationVisualizer:
     
    """
    Class for visualizing interpolation using Radial Basis Functions (RBFs).

    Attributes:
        num_points (int): Number of data points for interpolation.
        grid_resolution (int): Resolution of the grid for visualization.

    Methods:
        interpolate_and_plot(): Perform RBF interpolation and visualize the results.
    """     
    
    def __init__(self, num_points=100, grid_resolution=100):
        
        """
        Initialize the InterpolationVisualizer instance.

        Parameters:
            num_points (int): Number of data points for interpolation.
            grid_resolution (int): Resolution of the grid for visualization.
        """        
        self.num_points = num_points
        self.grid_resolution = grid_resolution
        
        # Generate low-discrepancy Halton sequences for x and y

        self.halton_sequence = Halton(2).random(n=self.num_points) # returns 2 columns of random Halton sequence
        self.x = self.halton_sequence[:, 0] # set first column to x
        self.y = self.halton_sequence[:, 1] # set second column to y
        self.z = np.cos(math.pi * self.x) * np.sin(math.pi * self.y) # target function cos(pi.x)sin(pi.y)

        # Define the grid for interpolation on a unit square domain
        
        self.xi = np.linspace(0, 1, self.grid_resolution) # 100 linearly spaced numbers
        self.yi = np.linspace(0, 1, self.grid_resolution) # 100 linearly spaced numbers
        self.xi, self.yi = np.meshgrid(self.xi, self.yi)


    def interpolate_and_plot(self):
        """ 
            Perform RBF interpolation and visualize the results using contour plot and 3D projection. 
        """        
        
        # Construct the RBF interpolant
        
        rbf = Rbf(self.x, self.y, self.z, function='cubic') # set the RBF kernel to 'cubic' for smoothness

        # Interpolate the values on the grid
        
        zi = rbf(self.xi, self.yi)


        # Plot the original data and the interpolated surface using contour plot and 3D projection
        
        fig, axs = plt.subplots(1, 2, figsize=(12, 5))
        
        # set main title
        
        #fig.suptitle('2D Interpolation of a Function', fontsize=14)
        fig.suptitle('2D Interpolation of a Function  $\cos(\pi x)\sin(\pi y)$', fontsize=14)



        #########   Contour Plot  #############
        
        # contour plot for the interpolation
        c = axs[0].contourf(self.xi, self.yi, zi, cmap='viridis', levels=20, alpha=0.5) 
        # scatter plot for the original data
        sc = axs[0].scatter(self.x, self.y, c=self.z, cmap='viridis', label='Original Data') 
        
        axs[0].set_xlabel('X')  # contour plot x label
        axs[0].set_ylabel('Y')  # contour plot y label
        axs[0].set_title('Contour Plot')    # contour plot title
        # Place legend outside the plot
        axs[0].legend(loc='upper right', bbox_to_anchor=(1.6, 1), ncol=2, fontsize=9)
        
        # Add a colorbar associated with the contour plot
        cbar = plt.colorbar(c, ax=axs[0], label='Function values')  

        ########    3D Projection   ##########
        
        axs[1] = plt.subplot(122, projection='3d')
        sc = axs[1].scatter3D(self.x, self.y, self.z, c=self.z, cmap='viridis', label='Original Data')
        axs[1].plot_surface(self.xi, self.yi, zi, cmap='viridis', alpha=0.5)
        axs[1].set_xlabel('X')
        axs[1].set_ylabel('Y')
        axs[1].set_zlabel('Function values')
        axs[1].set_title('3D Projection Plot')

        plt.tight_layout()
        plt.show()

# Instantiate the class and visualize the interpolation
visualizer = InterpolationVisualizer()
visualizer.interpolate_and_plot()