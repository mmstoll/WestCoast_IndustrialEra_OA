#Functions to convert carbonate parameters to pH

import math
from scipy import optimize


def averaged_parameters_summer(ds, iy, ix, box_length, date_index_start, date_index_end, month_start, month_end, osborne = 'off'):
    parameter_list = ['DIC','Alk','temp','salt','pco2','ph']
    variable_list = []
    dataset_dict = {}
    prof_dict = {}
    
    def is_jja(month):
        return (month >= month_start) & (month <= month_end)
        
    for i in range(0,len(parameter_list)):
        variable_list.append(ds[parameter_list[i]])
        selected_data_parameter = variable_list[i].isel(time = range(date_index_start, date_index_end+1),
                                                        eta_rho =range(iy-1,iy+box_length+2),
                                                        xi_rho = range(ix-1,ix+box_length+2))
        selected_data_parameter_jja = selected_data_parameter.sel(time=is_jja(selected_data_parameter['time.month']))
 
        dataset_dict[parameter_list[i]] = selected_data_parameter_jja
    
        prof_parameter = dataset_dict[parameter_list[i]].mean(dim=('eta_rho','xi_rho','time'), skipna = True)
        prof_dict[parameter_list[i]] = prof_parameter
    
    return(prof_dict)

'''
*FUNCTION that returns equation for zero-finding, constants for the Total Scale
Temp in units celcius, salinity in units PSU, DIC in units mol/kg, TA in units mol/kg
'''
def f_tot(temp,sal,DIC,Alk):
    TK = temp + 273.15 #temperature in Celsius into Kelvin	
    I = 19.924*sal/(1000 - 1.0049 * sal) #molal ionic strength
    R = 83.131 #Gas constant
    
    #Conservative seawater components as a function of salinity
    B_T = 0.000416 * sal / 35 #total boron
    F_T = 7e-5 * sal / 35 #total HF and F-
    # SO4_T = .0293*Sal/35 #total sulfate species from Millero 1995
    SO4_T = .02824 * sal / 35 #total sulfate species from DOE 1994, and Dickson/Millero's refitting of Mehrbach
    Ca_T = .01028 * sal / 35

    #1st dissociation constant for seawater as a function of T and S
    #Total Scale
    #Merhrbach et al 1973's values (refit by Dickon and Millero 1987) 
    #but given on the total scale by Lueker et al. (2000)
    tempA = -0.011555 * sal + 0.0001152 * sal**2
    pK1_star = -61.2172 + tempA + 3633.86/TK + 9.6777*math.log(TK)
    K_1_star = 10**(-1*pK1_star)
    K_1 = K_1_star

    #2nd dissociation constant for seawater as a function of T and S
    #Total Scale
    #Merhrbach et al 1973's values (refit by Dickon and Millero 1987) 
    #but given on the total scale by Lueker et al. (2000)    
    tempA = -.01781*sal + 0.0001122*sal**2
    pK2_star = 471.78/TK + 25.9290 + tempA - 3.16967*math.log(TK)
    K_2_star = 10**(-1*pK2_star)
    K_2 = K_2_star

    #dissociation contant for H2O as recommended by DOE (1994)
    #Total Scale
    temp1 = 148.96502-13847.26/TK-23.6521*math.log(TK)
    temp2 = (118.67/TK-5.977+1.0495*math.log(TK))*math.sqrt(sal)-0.01615*sal
    K_W_star = math.exp(temp1 + temp2)
    pKW_star =-1*math.log(K_W_star,10)
    K_W = K_W_star

    #Boric Acid
    #as reported in Millero 1995 
    #from Dickson Deep-Sea Res 1990 (Roy 1993 agrees)
    #both are in synthetic seawater without F-
    temp1 = (-8966.90-2890.53*math.sqrt(sal)-77.942*sal+1.728*(sal**(3/2))-0.0996*(sal**2))/TK
    temp2 = 148.0248+137.1942*math.sqrt(sal)+1.62142*sal
    temp3 = -math.log(TK)*(24.4344+25.085*math.sqrt(sal)+0.2474*sal)+0.053105*math.sqrt(sal)*TK
    K_B_star = math.exp(temp1+temp2+temp3)
    pKB_star =-1*math.log(K_B_star,10)
    K_B = K_B_star

    
    def f_zero(x):
        denom = (x**2+K_1*x+K_1*K_2)
        Alpha0 = (x**2)/denom
        Alpha1 = (K_1*x)/denom
        Alpha2 = (K_1*K_2)/denom
    
        return((Alpha1*DIC) + (2*Alpha2*DIC) + (K_W/x) + (B_T/(1+x/K_B)) - Alk - x) #equation that equals 0
    
    root = optimize.bisect(f_zero,1*10**-16,1) #calculates root of the equation returned by f_zero
    ph_value = (-math.log(root,10)) #calculates and returns the pH values
    return(ph_value)