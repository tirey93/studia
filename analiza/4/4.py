import pandas as pd
import  numpy as np
import ydata_profiling
from ydata_profiling import ProfileReport
import sweetviz as sv
import dtale

df = pd.read_excel('Data/titanic3.xls',sheet_name='dataset')
# #Przypisanie profilu
# report = ProfileReport(df,title='Profiling Report',
#                                  html={'style': {'full_width': True}},
#                                  sort=None, explorative=True, minimal=False, progress_bar=True)
# report.to_file("EDA_Titanic_ydata_profiling.html")
# train = pd.read_csv("Data/titanic/train.csv")
# test = pd.read_csv("Data/titanic/test.csv")
#
# sweetviz_report_compare = sv.compare([train, "Dane treningowe"], [test, "Dane testowe"], target_feat="Survived")
# sweetviz_report_compare.show_html(filepath='EDA_Titanic_sweetviz_compare_report.html')

df['ticket'] = df['ticket'].astype(str)
df['boat'] = df['boat'].astype(str)
df['cabin'] = df['cabin'].astype(str)
df['embarked'] = df['embarked'].astype(str)
df['home.dest'] = df['home.dest'].astype(str)

dtale_report = dtale.show(df)
dtale_report.open_browser()
dtale_report.notebook()