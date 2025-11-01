# WE ARE CLEANING EXCEL FILE FOR CUSTOMERS
import pandas as pd

# EXCEL DOSYASINI OKU
try:
    df = pd.read_excel("room.xlsx")
except:
    print("ERROR: THERE IS NO EXCEL FILE")
    quit()

# TÜM SÜTUN İSİMLERİNDEKİ BOŞLUKLARI TEMİZLE
df.columns = df.columns.str.strip()

# SAYI TEMİZLEME (eksiler, nokta, €, boşluk, kelime vs. hepsi gider → sadece rakam kalır)
df['review'] = df['review'].astype(str).str.replace(r"\D", "", regex=True).astype(int)
df['total'] = df['total'].astype(str).str.replace(r"\D", "", regex=True).astype(int)
df['per night'] = df['per night'].astype(str).str.replace(r"\D", "", regex=True).astype(int)
df['rating']= df['rating'].astype(str).str.replace(r"\D", "", regex=True).astype(int)

# INDEX 1'DEN BAŞLASIN
df.index = range(1, len(df) + 1)

# SONUCU GÖSTER
#print(df)
#print(df.dtypes)
df['score']=(df["rating"]*df["review"])/df["per night"]
df=df.sort_values('score',ascending=False)
df['title']=df["title"].str.split(',').str[0]
df_display = df[['title', 'location', 'per night', 'rating', 'review', 'score']]
df_display.index=range(1,len(df_display)+1)
print(df_display)

# İSTERSEN TEMİZ EXCEL KAYDET
df.to_excel("room_clean.xlsx", index=False)