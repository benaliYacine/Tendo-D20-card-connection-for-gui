"""
a=5
b=1.5
print(a+b)
list = [1,"5"]
print(list[0])
print(len(list))
tab=[('yellow',3),('black',8),('blue',7)]
for x,y in tab:
    print(x,y)
i=1
nb=7
while (i <= 10):
    print(nb, "*", i, "=",nb * i)
    i += 1 #ou bien i=i+1


for x in range(0,10): # ou bien range(0,10)
    print(x)

dico={"cours2":18,"cours1":15,"cours3":11}
for i in dico:
    print(i)

dic ={'976':' Mongolia ','52':'Mexico','212':' Morocco ','64':'New Zealand ','33':'france'}
for a in dic:
    print(a)
print(dic.items())


from collections import deque
t=deque( [1,2,3,4])

x=t.appendleft(8)
print(t)

a="Je suis étudiant à l'USTHB"
a.replace('USTHB','ESI')
print(a)

def date (*t):
    print(type(t))
    return str(t[0])+" "+t[1]+" "+str(t[2])

tuple=('a','b','b')
tuple[0]='c'
print(tuple[0])

# print(date( 5 ,"janvier" ,2000 ))#empaqueter

var=open('file.txt','w')
var.write("Et je ne sais pas où me garer.\nEt je ne sais pas où me garer.\nEt je ne sais pas où me garer.\nEt je ne sais pas où me garer.\n")
var.close()



var2=open('file.txt','r')
res=var2.read()
print(type(res))
print(res)

for a in var2:
    print(a)
    print(1)

res=var2.readlines()
# print(res)



import re
ligne="Bonjour tout _ le monde"
x=re.findall("monde$",ligne)
print(x)
for i in x:
    print(i)




print("rttrt\rppp")
print("trg")



import re
M=[[15,20,25],[30,"orange",40],[70,80,90]]
M[1][1]="pomme"
for a in M:
    print(str(a))
    print(re.sub("[',\[\]]","",str(a)))
    print(str(a).replace("'",""))


import sys
sys.stdout.write("test")



import sys
for a in sys.stdin:
    print(a)
    
a=input("donner a:\n")
print(a)




data = {
    "cle1": {
        "sous_cle1": [3, 5, 2]
    },
    "cle2": {
        "sous_cle2": [99, 8, 2]
    },
    "cle3": {
        "sous_cle3": [999, 8, 2]
    },
}

print (data)


dic={{"arbre":[5,3,6]},{"a":[1,6,2]},{"re":[1,2,3]}}



ma_list=['4','4','4','4']
j='5'
for i in range(len(ma_list)):
    ma_list[i]=j


print(ma_list)


a="aA"
a=a.lower()
print(a)

import re
[x = re.findall("\w+$","Bonjour tout _ le monde"),print(x),[print(i) for i in (x)]]


a=[1,2,3]
b=[7,8,9]
print([*zip(a,b)])


a="C:\slash\study\uni\l2\s4"
import os 
print(os.path.isdir(a))


"""



