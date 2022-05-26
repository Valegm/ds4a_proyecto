import pandas as pd
import numpy as np
import json
import plotly.express as px
import os
import webbrowser
import warnings
from datetime import datetime as dt
from IPython.core.display import display, HTML
import missingno as msno
print("inicio")
rdl = pd.read_csv('REPORTE_DOCUMENTOS_LAUDOS_20220315.csv',sep = ';')
rdl

