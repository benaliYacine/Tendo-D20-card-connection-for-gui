
print('hello')
print('hello\thello\thello\t')
c=3.2
print("c=",c)
f=float(c)#fonctionfloat()#avecint()(entiers)onperdlaprécision
print(f)
a="il "
b="écrit"
a=a+b #a+=b
print(a)
maliste1= ["dog", "cat", "mouse" ] #une liste avec 3 objets
print(maliste1)
a=()
print(a)
b=1,2,3
print(type(b))
(a,b)=(3,5)
print()
ma_chaine="J’aimel’USTHB"
ma_liste=ma_chaine.split("’")
print(ma_liste[2])                         
for x in range(2,11): # ou bien range(0,10)
    print(x)

tab=[('yellow',3),('black',8),('blue',7)] # unelistede 3 tuples
for x in tab:
    print(x)#sinonprint(x,y) pour afficherles entiers

dico={"cours2":18,"cours1":15,"cours3":11}
print(type(dico.keys()))
for i in dico.keys(): # ou for i in dico:
    print(i," est une clé") # ou +au lieu de
animal="cat"
num=['i','ii','iii','iv','v']
if animal == "cat":
    for x in num:
        print("We hate cat","",x,"")

a={'plâtre':'blanc','pneu':5,4:'vert'}
for i in a.keys():
    print(type(i))

a =[7,9,8]
print(list(reversed(a)))#construire un objet list à partir d’un objet reverse list

dic={"cours1":15,"cours2":18,"cours3":11}
for i in sorted( dic.keys()):
    print(i) #afficher individuellement les valeurs

for i in sorted(dic.keys()):
    print(dic[i])

texte=["pomme","pain","pomme","orange","pomme","pain"]
lettres ={}
for c in texte:
    if c in lettres:
        lettres[c] = lettres[c] + 1#ou lettres[c]+=1
    else:
        lettres[c] = 1
for i in sorted (lettres):
    print (i,lettres. get (i))
import datetime

# get the POSIX timestamp for the current date and time
timestamp = datetime.datetime.now().timestamp()

print(timestamp)  # e.g. 1650000000.123456


for i, boucle in enumerate(range(15, 22, 2)):
    print(f"Step {i}: {boucle}")

var= open('fic.txt','w')#on obtient un objet de type « file »
var.write('Je suis devant l\'école!\n')
var.close()
var= open('fic.txt','r')
