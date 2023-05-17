import csv
import pandas as pd

#df1 = Dataframe from List
df1=pd.DataFrame()

## List of string
lst=['Sarjana','Sarjana','Sarjana','Sarjana','Sarjana','Sarjana','Sarjana','Sarjana','Sarjana','Sarjana']
fak=['Keguruan dan Ilmu Pendidikan','Keguruan dan Ilmu Pendidikan','Keguruan dan Ilmu Pendidikan','Keguruan dan Ilmu Pendidikan',
     'Keguruan dan Ilmu Pendidikan','Keguruan dan Ilmu Pendidikan','Keguruan dan Ilmu Pendidikan','Keguruan dan Ilmu Pendidikan',
     'Keguruan dan Ilmu Pendidikan','Keguruan dan Ilmu Pendidikan']
prodi=['Bimbingan Konseling','Pendidikan Keagamaan Katholik','Pendidikan Guru Sekolah Dasar','Pendidikan Bahasa Inggris',
      'Pendidikan Bahasa dan Satra Indonesia', 'Pendidikan Sejarah','Pendidikan Ekonomi Bidang Keahlian Khusus Pendidikan Ekonomi',
       'Pendidikan Ekonomi Bidang Keahlian Khusus Pendidikan Akuntansi',
      'Pendidikan Matematika','Pendidikan Fisika']
jmlMhs=['474','378','905','609','328','142','155','185','292','78']

## Calling dataframe constructor ke list
df1['Program']=lst
df1['Fakultas']=fak
df1['Prodi']=prodi
df1['Jumlah']=jmlMhs

# Mengubah index mulai dari 1
df1.index = df1.index + 1

#df2 = Dataframe from a dictionary

#dengan dictionary 
data = {'Program':['Sarjana','Sarjana','Sarjana','Sarjana','Sarjana','Sarjana' ,'Sarjana','Sarjana','Sarjana',
                    'Sarjana'],
        'Fakultas':['Keguruan dan Ilmu Pendidikan','Keguruan dan Ilmu Pendidikan',
                       'Ekonomi','Ekonomi','Ekonomi','Sains dan Teknologi','Sastra','Sastra','Sastra','Sains dan Teknologi'], 
        'Prodi':['Pendidikan Biologi','Pendidikan Kimia','Akuntansi','Manajemen','Ekonomi','Matematika',
                   'Sastra Indonesia','Sastra Inggris','Sejarah','Teknik Elektro'],
        'Jumlah':[200,99,775,952,221,93,182,785,149,257]}
#memanggil data frame 
df2 = pd.DataFrame(data,index = [11,12,13,14,15,16,17,18,19,20])


#df3 = Dataframe from a List of List
indexList = list()
for i in range(20, 30):
    indexList.append(i+1)

tempList  = [['Sarjana', 'Sains dan Teknologi', 'Teknik Mesin', '459'], ['Sarjana', 'Sains dan Teknologi', 'Informatika', '738'], ['Sarjana', 'Farmasi', 'Farmasi', '720'], ['Sarjana', 'Psikologi', 'Psikologi', '969'], ['Sarjana', 'Teologi', 'Filsafat Keilahian ', '312'], ['Magister', 'Keguruan dan Ilmu Pendidikan', 'Magister Pendidikan Bahasa Inggris', '27'], ['Magister', 'Keguruan dan Ilmu Pendidikan', 'Magister Pendidikan Bahasa Indonesia', '22'], ['Magister', 'Keguruan dan Ilmu Pendidikan', 'Magister Pendidikan Matematika', '20'], ['Magister', 'Farmasi', 'Magister Farmasi', '68'], ['Magister', 'Ekonomi', 'Magister Manajemen', '71']]

col=["Program", "Fakultas", "Prodi", "Jumlah"]
df3=pd.DataFrame(tempList,index= indexList,columns = col)

#df4 = Dataframe from Series
data = {'Program': pd.Series(['Magister', 'Magister', 'Magister', 'Magister', 'Magister', 'Doktor', 'Vokasi', 'Vokasi', 'Profesi', 'Profesi', 'Profesi'], 
                             index=range(31, 42)),
        'Fakultas': pd.Series(['Psikologi', 'Sastra', 'Teologi', 'Pascasarjana', 'Pascasarjana', 'Pascasarjana', 'Vokasi', 'Vokasi', 'Farmasi', 'Keguruan dan Ilmu Pendidikan', 'Sains dan Teknologi'], 
                             index=range(31, 42)),
        'Prodi': pd.Series(['Psikologi Program Magister', 'Magister Sastra', 'Magister Filsafat Keilahian', 'Magister Kajian Budaya', 'Magister Kajian Bahasa Inggris', 'Doktor Kajian Budaya', 'Mekatronika', 'Teknologi Elektromedis', 'Pendidikan Profesi Apoteker', 'Pendidkan Profesi Guru', 'Program Profesi Insinyur'], 
                             index=range(31, 42)),
        'Jumlah': pd.Series([0, 5, 43, 48, 34, 13, 114, 135, 189, 138, 2], 
                             index=range(31, 42))
    }
df4 = pd.DataFrame(data)


# Create a list of prev dataframes
frames=[df1 ,df2, df3, df4]

## Concatenating dataFrames to a single df
# Menggunakan concat dengan list karena :
# 1. lebih cepat dibanding menambahkan satu per satu
# 2. append sudah deprecated pada versi python pada ide saya
df = pd.concat(frames)
print(df)

# Export to csv with path
df.to_csv(r'C:\Users\anton\OneDrive\Documents\College\PAD #1\Pandas\export_dataframe.csv', index=False, header=True)

# Export to json with path with a split orientation with index
df.to_json(r'C:\Users\anton\OneDrive\Documents\College\PAD #1\Pandas\export_dataframe.json', orient = 'split', compression = 'infer', index = 'true')