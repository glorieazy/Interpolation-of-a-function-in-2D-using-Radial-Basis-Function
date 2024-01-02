### Interpolation-of-a-function-in-2D-using-Radial-Basis-Function

'''
    
    - Project Title: Interpolation of a function in 2D using Radial Basis Function

    - Introduction: 
    Interpolation is a fundamental technique in scientific computing, allowing us to estimate values between
    known data points. 

    - Aim & Overview:
    This script demonstrates the use of Radial Basis Function (RBF) interpolation, leveraging the quasi-random 
    Halton sequence for low-discrepancy sampling. The interpolation results are visualized through 
    contour plots and 3D projections.
    The Rbf class from scipy.interpolate is employed for Radial Basis Function interpolation, 
    specifically using the cubic kernel for smoother results.

    - Visualization:
    Results are visualized through two subplots: A Contour Plot and a 3D Projection Plot

    - Configurability:
    Users can adjust parameters such as the number of data points, grid resolution, and the type of RBF kernel. 
    This flexibility facilitates experimentation with different settings for varying interpolation scenarios.
    
    - Referance:
    Lecture Slide/Code by Dr. Sokolov
    https://stackoverflow.com/questions/37872171/how-can-i-perform-two-dimensional-interpolation-using-scipy
    
'''
