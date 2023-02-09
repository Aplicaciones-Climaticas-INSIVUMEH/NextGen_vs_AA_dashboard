import pandas as pd

datapath = 'jan23data/'
aadata = 'scores_aa_2021-2022.csv'
ngdata = 'scores_nextgen_2021-2022.csv'

# prefixes = ['','climaest_','obschirps_','raster_']
datafont = {'Climatología de CHIRPS y observados de estaciones.':'',
            'Climatología y observados de estaciones.':'climaest_',
            'Climatología y observados de CHIRPS sampleados a estaciones.':'obschirps_',
            'Climatología y observados de CHIRPS raster completo.':'raster_'}

metrics = ['HR','HSS','2AFC','LEPS']

years = [2021,2022,2023]
months = ['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic']
months_to_number = {'ene':1,'feb':2,'mar':3,'abr':4,'may':5,'jun':6,'jul':7,'ago':8,'sep':9,'oct':10,'nov':11,'dic':12}

prefix = datafont['Climatología de CHIRPS y observados de estaciones.']

monAA_original = pd.read_csv(datapath+prefix+aadata,header=[0,1])[['date','score']].droplevel(0,axis=1)
monNG_original = pd.read_csv(datapath+prefix+ngdata,header=[0,1])[['date','score']].droplevel(0,axis=1)

print(monAA_original.mean())
print(monNG_original.mean())

