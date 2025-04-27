import pandas as pd 

data={
    'base word':['play','run','write','happy'],
    'added morph':['-ed','-ing','-er','-ness'],
    'new word':['played','running','writer','happiness'],
    'deleted morph':['-','-','-','-'],
    'new_word(after deletion)':['play','run','write','happy']
}
  
df=pd.DataFrame(data)
print(df)

def add_morph(row):
    return row['base word']+row['added morph']

def delete_morph(row):
    if row['deleted morph'] != '-':
        return row['base word'].replace(row['deleted morph'], '')
    return row['base word']

df["New Word (After Addition)"] = df.apply(add_morph, axis=1)
df["New Word (After Deletion)"] = df.apply(delete_morph, axis=1)

print (df)