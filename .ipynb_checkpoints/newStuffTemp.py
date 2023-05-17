

def main():
    #Display the names of the first three presi
    file = "presidenIndonesia.txt"
    print("Display dengan Loop:")
    displaydenganLoop(file)
    print()
    print("InDisplay dengan list :")
    displaymenjadiList(file)
    print("InDisplay dengan read: ")
    displaydenganread(file)
    print()
    tambahDataWithAppend(file)
    displaydenganread(file)
    print()
    tambahDataWithWrite(file)
    displaydenganread(file)


def displaydenganread(file):
    infile=open(file,'r')
    line=infile.readline()
    while line !='':
        print(line,end="")
        line=infile.readline()
    infile.close()

def displaydenganLoop(file):
    infile = open(file, 'r')
    for line in infile:
        print(line, end="")
    infile.close()


def displaymenjadiList(file):
    infile = open(file,'r')
    listPres = [line.rstrip() for line in infile]
    infile.close()
    print(listPres)

def tambahDataWithAppend(file):
    outfile = open(file, 'a')
    list1=["Abdurahman Wahid\n", "Megawati Soekarno Putri\n"]
    outfile.writelines(list1)
    outfile.close()
    
def tambahDataWithWrite(file):
    outfile = open(file, 'a' )
    list1=["Susilo Bambang Yudhoyono\n"]
    outfile.writelines(list1)
    outfile.close()

def csv() :
    fakultas = input("Masukan nama Fakultas : ")
    #fakultas=fakultas.title()
    if fakultas !="":
        infile=open("JumlahMahasiswaUSD2.csv",'r')
        for line in infile:
            data=line.split(';')
            #print(data[1])
            if data[1]==fakultas:
                print(data[2])
    else :
        print("Fakultas tidak di temukan")

main()