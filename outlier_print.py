import numpy as np

def print_ouliers(dist):
    dist = sorted(dist)
    n = len(dist)
    
    q1 = (n+2)/4
    q3 = (3*n + 2)/4
    
    if type(q1) and type(q3) == float:
        upper1 = int(np.ceil(q1))
        lower1 = int(np.floor(q1))
        upper2 = int(np.ceil(q3))
        lower2 = int(np.floor(q3))
        
        ansa1 = int((dist[upper1 - 1] + dist[lower1 -1]) / 2)
        ansa2 = int((dist[upper2-1] + dist[lower2-1]) / 2)
        
        iqr = ansa2 - ansa1
        
        upper_bound = ansa2 + 1.5*iqr
        lower_bound = ansa1 - 1.5*iqr
        
        outliers = [num for num in dist if num < lower_bound or num > upper_bound]
        return outliers                
    else:
        upper_bound = q3 + 1.5*iqr 
        lower_bound = q1 - 1.5*iqr
        
        outliers = [num for num in dist if num < lower_bound or num > upper_bound]
        return outliers