import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def fetch_null_cases(dataframe, var, print_list=False):
    nulos = dataframe[var].isna()
    cantidad = nulos.sum()
    porcentaje = cantidad / dataframe.shape[0] * 100
    casos = []

    if print_list:
        casos = dataframe[nulos]["cname"]
        
    return cantidad, porcentaje, casos
	


def fetch_descriptives(data: pd.DataFrame, columnas: list):
    categoricas = None
    numericas = None
    
    try:
        categoricas = data[columnas].describe(include = [object])
    except Exception as e:
        print(e)
    
    try:
        numericas = data[columnas].describe(include = [np.number])
    except Exception as e:
        print(e)
        
        
    return categoricas, numericas