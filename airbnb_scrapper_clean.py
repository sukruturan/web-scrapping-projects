# WE ARE CLEANING EXCEL FILE FOR CUSTOMERS
import pandas as pd

# READ EXEL FİLE 
try:
    df = pd.read_excel("room.xlsx")
except:
    print("ERROR: THERE IS NO EXCEL FILE")
    quit()

# CLEAN FOLDERS
df.columns = df.columns.str.strip()

# EDİT COLUMNS
df['review'] = df['review'].astype(str).str.replace(r"\D", "", regex=True).astype(int)
df['total'] = df['total'].astype(str).str.replace(r"\D", "", regex=True).astype(int)
df['per night'] = df['per night'].astype(str).str.replace(r"\D", "", regex=True).astype(int)
df['rating']= df['rating'].astype(str).str.replace(r"\D", "", regex=True).astype(int)

# INDEX 1'DEN BAŞLASIN
df.index = range(1, len(df) + 1)

#SHOW RESULT
#print(df)
#print(df.dtypes)
df['score']=(df["rating"]*df["review"])/df["per night"]
df=df.sort_values('score',ascending=False)
df['title']=df["title"].str.split(',').str[0]
df_display = df[['title', 'location', 'per night', 'rating', 'review', 'score']]
df_display.index=range(1,len(df_display)+1)
print(df_display)

# SAVE EXEL
df.to_excel("room_clean.xlsx", index=False)
