import csv
f = open("NO2.txt", 'r', encoding='ANSI') #list with names and grades from exam 1, just copied from official grades pdf
y = f.read()
y = y.splitlines() #each text line contains 1 information, thats the way i found to copy the pdf
names = [] #names of the applicants
NO = {} #names : grades in exam 1
ND = {} #names : grades in exam 2
NF = {} #names : final grades
list1 = [y[x:x+4] for x in range(0, len(y),4)]  #Copy just the names and grade lines, ignores the other lines

for applicant in list1:
    NO.update({applicant[1]: float(applicant[2])}) #commented 1 day after its done, have no clue why name is in position 1
    names.append(applicant[1])



f2 = open("nd.txt", 'r', encoding='ANSI') #list with names and grades from exam 2, just copied from official grades pdf
y2 = f2.read()
y2 = y2.splitlines()


list2 = [y2[x:x+6] for x in range(0, len(y),6)] #Copy just the names and grade lines, ignores the other lines

list2 = [x for x in list2 if x != []] #for some reason it kept adding empty lists, added this hack

for applicant in list2:
    ND.update({applicant[1]: float(applicant[2])}) #commented 1 day after its done, have no clue why name is in position 1


for name in names:
    if name in ND:
        NFC = ((2*NO[name]+5*ND[name])/26)   #final grade formula
        NF.update({name : NFC})


with open('ufg.csv', 'w') as f:  # write dict to a csv
    w = csv.DictWriter(f, NF.keys())
    w.writeheader()
    w.writerow(NF)
