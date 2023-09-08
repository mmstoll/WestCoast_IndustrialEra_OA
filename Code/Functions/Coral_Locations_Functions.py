import numpy as np

'''
FIND LOCATION INDICES NEAREST TO CORAL SITE
--> Finds and returns the index array of the point in the grid represented by lon1,lat1 that is closest to the target with lon2, lat2, and the minimum distance in km.
--> lon2 and lat2 can be scalars or arrays of the same size as lon1 and lat1.
'''
def find_indices(case, ds, lon, lat):
    if case == 'modern':
        ds_modern = ds
        lon1 = ds_modern['lon_rho']
        lat1 = ds_modern['lat_rho']
    if case == 'historic':
        ds_historic = ds
        lon1 = ds_historic['lon_rho']
        lat1 = ds_historic['lat_rho']
    
    if np.isscalar(lon):
        lon2 = np.ones_like(lat1) * lon #creates array of the same shape as ds['lat_rho'] of the value lon2
    if np.isscalar(lat):
        lat2 = np.ones_like(lat1) * lat #creates array of the same shape as ds['lat_rho'] of the value lat2
    
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    
    # take the difference between the value of lon2 (input by user) and every point in lon1 and lat 1. 
    # returns values in radians 
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    # haversine formula
    haversine = (np.sin(dlat/2.)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2)
    
    # calculates the distance
    dist = 2. * np.arcsin(np.sqrt(haversine))
    r = 6371. # Radius of Earth in kilometers
    haversine_fun = dist*r #this converts the haversine distance into km 
    
    # This just finds the minimum value in haversine_fun because this is the closest lat, lon to point specified by user and returns the indices of eta_rho and xi_rho
    indice_values = dist.argmin(dim=['eta_rho','xi_rho']) #values is in a dictionary
    iy = int(indice_values['eta_rho']) #float
    ix = int(indice_values['xi_rho']) #float   
    
    return(iy,ix)

'''
ROUND DEPTHS 
--> Round to nearest increment of 25 meters
'''
def round_depth(site_depth, base = 25):
    rounded_depth = base * round(float(site_depth)/base)
    return int(rounded_depth)
