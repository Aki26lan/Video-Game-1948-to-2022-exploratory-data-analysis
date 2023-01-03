import pandas as pd
from pandas_profiling import ProfileReport
df=pd.read_csv(r"C:\Users\UMAPRIYA\Desktop\Data Analyst_Naukri_Dataset\Project Upload\Video_Game_IMDB_list.csv")
print(df.head())

profile = ProfileReport(df,title='Video_Game_IMDB_list')
profile.to_file('Video_Game_IMDB_list.html')




