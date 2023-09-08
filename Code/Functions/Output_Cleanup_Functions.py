import xarray as xr
import pandas as pd


def depths():
    '''
    *DEPTH - create a list of depths
    '''
    depth_list = [0.0, 25.0, 50.0, 75.0, 100.0, 125.0, 150.0, 175.0, 200.0]
    return(depth_list)


def open_files_12vs12(file_modern_12km, file_historic_12km):
    '''
    *OPEN model output files
    '''
    ds_modern12 = xr.open_dataset(file_modern_12km)
    ds_modern12 = ds_modern12.set_coords(['lon_rho', 'lat_rho'])

    ds_historic12 = xr.open_dataset(file_historic_12km)
    ds_historic12 = ds_historic12.set_coords(['lon_rho', 'lat_rho'])
   
    '''
    *DATE - create a list of months
    '''
    date1_m = "1994-01-01"
    date2_m = "2007-11-01"
    time_length_m = len(ds_modern12['ocean_time'])

    date1_h = "1891-01-01"
    date2_h = "1904-11-01"
    time_length_h = len(ds_historic12['ocean_time'])

    month_list_modern12 = [i.strftime("%B %Y") for i in pd.date_range(start=date1_m, end=date2_m, freq='MS')]
    pd_date_modern12 = pd.to_datetime(month_list_modern12)

    month_list_historic12 = [i.strftime("%B %Y") for i in pd.date_range(start=date1_h, end=date2_h, freq='MS')]
    pd_date_historic12 = pd.to_datetime(month_list_historic12)

    '''
    *ADD DATES TO XARRAY AS A COORDINATE - add to the dimension 'time'
    '''
    ds_modern12 = ds_modern12.assign_coords(time=("time", pd_date_modern12))
    ds_historic12 = ds_historic12.assign_coords(time=("time", pd_date_historic12))
    
    return(ds_modern12, ds_historic12, month_list_modern12, month_list_historic12)


def open_files_fut12(file_future_12km):
    '''
    *OPEN model output files
    '''
    ds_future12 = xr.open_dataset(file_future_12km)
    ds_future12 = ds_future12.set_coords(['lon_rho', 'lat_rho'])

    '''
    *DATE - create a list of months
    '''
    date1_m = "2094-01-01"
    date2_m = "2107-11-01"
    time_length_m = len(ds_future12.ph['time'])

    month_list_future12 = [i.strftime("%B %Y") for i in pd.date_range(start=date1_m, end=date2_m, freq='MS')]
    pd_date_future12 = pd.to_datetime(month_list_future12)

    '''
    *ADD DATES TO XARRAY AS A COORDINATE - add to the dimension 'time'
    '''
    ds_future12 = ds_future12.assign_coords(time=("time", pd_date_future12))
    
    return(ds_future12, month_list_future12)