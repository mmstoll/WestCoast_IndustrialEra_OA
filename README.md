# A Century of Change in the California Current: Upwelling Systems Accelerate Acidification 

## Content
 - Overview
 - Installation Guide/System Requirements
 - Instructions for Use
 - License

### Overview
Jupyter notebooks and python scripts to reproduce the figures and analyses presented in 'A Century of Change in the California Current: Upwelling Systems Accelerate Acdification'. 

### Installation Guide and System Requirements
To run the notebooks on your local desktop, you will need to install Python through anaconda. The following notebooks use Python version 3.9.12.

1) Install conda from official anaconda website: https://www.anaconda.com/products/distribution
2) Next, clone this repository from the command line by running:
```ruby
git clone https://github.com/mmstoll/WestCoast_IndustrialEra_OA.git
```
3) Then change into the WestCoast_IndustrialEra_OA directory:
```ruby
cd WestCoast_IndustrialEra_OA
```
4) To set up your software environment, it is recommended you use the provided conda environment. This environment lists the necessary packages and versions to run the Jupyter notebooks:
```ruby
conda activate oa-environment
```
5) To run the Jupyter notebooks, you will need to launch Jupyter in your web browser:
```ruby
jupyter notebook
```
Typical install time on desktop: < 30 mins

### Instructions for Use
Each cell of code can be run with ```shift + enter``` or you can run the entire notebook by selecting ```Run``` --> ```Run All Cells``` in the dropdown menu.

For more information on running Jupyter notebooks, see the [Jupyter Documentation](https://docs.jupyter.org/en/latest/).

### Notebook Descriptions
#### **Code:**
 - d11B_Raw_Data_Analysis.ipynb
    - **Extended Data Figure 2:** Skeletal δ11B data from the Salish Sea West Coast
 
 - Salish_Sea_Analysis.ipynb
    - **Extended Data Figure 3:** Centennial changes in _p_ CO<sub> 2 </sub> and pH in the Salish Sea
    - Calculates coral-based estimates of pH and _p_ CO<sub> 2 </sub> centennial change in the Salish Sea 
 
 - Salish_Sea_Box_Model.ipynb
    - Estimates of centennial change in pH and _p_ CO<sub> 2 </sub> in the Salish Sea using box model
 
 - ROMS_Model_Analysis.ipynb
    - **Main Text Figure 1a:** Climatological mean map of _p_ CO<sub> 2 </sub> anomaly at 75 meters depth over the ROMS domain
    - **Main Text Figure 3a - 3d:** Maps of future acidification in the California Current following RCP 8.5 emissions scenario
    - **Main Text Figure 3e:** Time series of atmospheric and oceanic _p_ CO<sub> 2 </sub> over the 21st century
 
 - ROMS_Model_Decomposition_Analyses.ipynb
    - Preformed DIC Test: Can estimates of ΔDIC derived from equilibration of atmospheric CO<sub> 2 </sub> at outcropping regions and accompanying thermodynamic effects explain modeled ΔDIC?
    - Preformed O<sub> 2 </sub> Test: Can centennial shifts in remineralization explain modeled ΔDIC?
    - **Extended Data Figure 7**: The ratio of ∆DIC attributed to changes in remineralization to modeled ∆DIC at 0–200 meters depth 
    - **Extended Data Figure 8**: The ratio of preformed ∆DIC attributed to equilibration of atmospheric CO<sub> 2 </sub> and thermodynamic effects (Methods, Equation 3) to modeled ∆DIC at 0–50 meters, 75–125 meters, and 150–200 meters depth
 
 - Coral_vs_Model_Comparison.ipynb
    - **Main Text Figure 2:** Geochemical and model records of 20th century acidification in the California Current
    - **Extended Data Table 4:** West Coast coral _p_ CO<sub> 2 </sub> and pH values (total scale) informed by skeletal δ11B
    - **Supplementary Info Figure 3.2:** Comparison between historic model-based and coral-based _p_ CO<sub> 2 </sub> estimates in the California Current 
 
#### **Data:**
- Atmospheric_Global_Annual_CO2_IAC_Switzerland.csv
   - Atmospheric CO<sub> 2 </sub> data from Institute for Atmospheric and Climate Science, Switzerland  
- BGC_Model_Coral_d11B_Data.csv
   - Historic and modern coral δ11B data, as previewed in Extended Data Table 3
- Manuscript_West_Coast_Coral_Data.xlsx
   - Sheet 1: Historic West Coast coral δ11B data
   - Sheet 2: Historic West Coast coral δ11B data, averaged by location
- Manuscript_West_Coast_Coral_Data_BGC_Model.xlsx
   - Historic West Coast coral δ11B data, averaged by location
- Upwelling_Properties.csv
   - Saved output from modern ROMS simulation from upwelled waters that enter the Salish Sea from the California Current    
- Simulation model output data can be made available by email requests to the corresponding authors. The physical and biogeochemical codes used for the 4km resolution simulations of this model can be found at https://github.com/UCLA-ROMS/Code. 

### License
These notebooks are licensed under the [MIT License](/LICENSE), which allows academic and commercial re-use and adaptation of this work.
