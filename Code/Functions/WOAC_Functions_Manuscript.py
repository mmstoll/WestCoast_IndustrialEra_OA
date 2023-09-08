import numpy as np
import pandas as pd
import sys
import os
import importlib


'''
CALCULATES PH VALUES ASSUMING CALCIFICATION/DISSOLUTION
 - Returns a range of calculated pH values (pH_calc_tot, total scale) given a range of DIC and TA. Assumes constant temp and salinity
'''
def CO2_calcification_calc(seasonal_avgs, season):
    sys.path.insert(1, '../Functions')
    import pH_Functions as ph_fxns
    importlib.reload(ph_fxns)
    
    avg_temp = seasonal_avgs['temp_avg']['summer_avg']
    avg_sal = seasonal_avgs['sal_avg']['summer_avg']
    avg_alk = seasonal_avgs['alk_avg']['summer_avg']
    avg_DIC = seasonal_avgs['DIC_avg']['summer_avg']
        
    DIC_start = avg_DIC - 161
    DIC_end = avg_DIC + 139
    TA_start = avg_alk - 322
    TA_end = avg_alk + 278
    
    DIC_range = np.linspace(DIC_start, DIC_end, 301) #units umol/kg
    Alk_range = np.linspace(TA_start, TA_end, 301) #units umol/kg
    
    pH_calc_tot = pd.DataFrame(columns = ['pH_calc_tot'], index = DIC_range)

    for j in range(0,len(DIC_range)):
        temp = avg_temp #in units Celsius
        sal = avg_sal #in units PSU
        DIC = (DIC_range[j])/(1*10**6) #DIC must be in units mol/kg; converting from umol/kg
        Alk = (Alk_range[j])/(1*10**6) #Alk must be in units mol/kg; converting from umol/kg
        ph_value = ph_fxns.f_tot(temp,sal,DIC,Alk) 
        pH_calc_tot.iloc[j] = ph_value #this pH is reported on the total scale
    
    return(pH_calc_tot)

'''
CALCULATES PH VALUES ASSUMING CO2 INVASION
 - Returns a range of calculated pH values (pH_calc_tot, total scale) given a range of DIC and a specific station. Assumes constant Alkalinity, temp, and salinity
'''
def CO2_invasion_calc(seasonal_avgs, DIC_range, season):
    sys.path.insert(1, '../Functions')
    import pH_Functions as ph_fxns
    importlib.reload(ph_fxns)

    avg_temp = seasonal_avgs['temp_avg']['summer_avg']
    avg_sal = seasonal_avgs['sal_avg']['summer_avg']
    avg_alk = seasonal_avgs['alk_avg']['summer_avg']
    avg_DIC = seasonal_avgs['DIC_avg']['summer_avg']

    DIC_range = np.linspace(1950, 2250, 301) #units umol/kg

    pH_calc_tot = pd.DataFrame(columns = ['pH_calc_tot'], index = DIC_range)

    for j in range(0,len(DIC_range)):
        temp = avg_temp #in units Celsius
        sal = avg_sal #in units PSU
        DIC = (DIC_range[j])/(1*10**6) #DIC must be in units mol/kg; converting from umol/kg
        Alk = avg_alk/(1*10**6) #Alk must be in units mol/kg; converting from umol/kg
        ph_value = ph_fxns.f_tot(temp,sal,DIC,Alk) 
        pH_calc_tot.iloc[j] = ph_value #this pH is reported on the total scale
    
    return(pH_calc_tot)


'''
CALCULATES PH VALUES ASSUMING PHOTOSYNTHESIS/RESPIRATION
 - Returns a range of calculated pH values (pH_calc_tot, total scale) given a range of DIC and a specific station. Assumes constant temp and salinity
'''
def CO2_respiration_calc(seasonal_avgs, season):
    sys.path.insert(1, '../Functions')
    import pH_Functions as ph_fxns
    importlib.reload(ph_fxns)
    

    avg_temp = seasonal_avgs['temp_avg']['summer_avg']
    avg_sal = seasonal_avgs['sal_avg']['summer_avg']
    avg_alk = seasonal_avgs['alk_avg']['summer_avg']
    avg_DIC = seasonal_avgs['DIC_avg']['summer_avg']

    DIC_start = avg_DIC - 161
    DIC_end = avg_DIC + 139
    TA_start = avg_alk + 25.82
    TA_end = avg_alk -22.29

    
    DIC_range = np.linspace(DIC_start, DIC_end, 301) #units umol/kg
    Alk_range = np.linspace(TA_start, TA_end, 301) #units umol/kg
    
    pH_calc_tot = pd.DataFrame(columns = ['pH_calc_tot'], index = DIC_range)

    for j in range(0,len(DIC_range)):
        temp = avg_temp #in units Celsius
        sal = avg_sal #in units PSU
        DIC = (DIC_range[j])/(1*10**6) #DIC must be in units mol/kg; converting from umol/kg
        Alk = (Alk_range[j])/(1*10**6) #Alk must be in units mol/kg; converting from umol/kg
        ph_value = ph_fxns.f_tot(temp,sal,DIC,Alk) 
        pH_calc_tot.iloc[j] = ph_value #this pH is reported on the total scale
    
    return(pH_calc_tot)

'''
CALCULATES PH VALUES ASSUMING UPWELLING/MIXING
 - Returns a range of calculated pH values (pH_calc_tot, total scale) given a range of DIC and a specific station. Assumes constant Alkalinity, temp, and salinity
'''
def CO2_upwelling_calc(seasonal_avgs, upwelling_properties, season):
    sys.path.insert(1, '../Functions')
    import pH_Functions as ph_fxns
    importlib.reload(ph_fxns)
    
    
    avg_temp = seasonal_avgs['temp_avg']['summer_avg']
    avg_sal = seasonal_avgs['sal_avg']['summer_avg']
    avg_alk = seasonal_avgs['alk_avg']['summer_avg']
    avg_DIC = seasonal_avgs['DIC_avg']['summer_avg']
        
    DIC_range_mix = np.linspace(upwelling_properties.loc['Annual Average']['DIC']/1.024, avg_DIC, 100) #units umol/kg
    Alk_range_mix = np.linspace(upwelling_properties.loc['Annual Average']['TA']/1.024, avg_alk, 100) #units umol/kg

    pH_calc_tot = pd.DataFrame(columns = ['pH_calc_tot'], index = DIC_range_mix)

    for j in range(0,len(DIC_range_mix)):
        temp = avg_temp #in units Celsius
        sal = avg_sal #in units PSU
        DIC = (DIC_range_mix[j])/(1*10**6) #DIC must be in units mol/kg; converting from umol/kg
        Alk = (Alk_range_mix[j])/(1*10**6) #Alk must be in units mol/kg; converting from umol/kg
        ph_value = ph_fxns.f_tot(temp,sal,DIC,Alk) 
        pH_calc_tot.iloc[j] = ph_value #this pH is reported on the total scale
    
    m_mix, b_mix = np.polyfit(pH_calc_tot.index, pH_calc_tot['pH_calc_tot'].astype(np.float64), 1)
    
    return(pH_calc_tot, m_mix, b_mix)