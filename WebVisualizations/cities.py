import pandas as pd
import datetime

cities = pd.read_csv(r"Resources\Data\cities.csv")

# Tell where to put data into Data webpage ("Data.html")
# ..\..\ tells program to go up two folder out of Data folder and Resources folder
# to find Data.html

cities.to_html("Data.html", index=False,classes="table_data")





