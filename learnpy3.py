"""
import re
ligne="eleve3 au poste3"
x=re.search("(\d)(.+)poste\\1",ligne)
if x:
    print("ok",x.group(1))



l1=[1,2,3]
l2=["yacine","ilyes","azzedin"]
d1=dict(zip(l1,l2))
print(d1)

d2={i:j for i,j in zip(l1,l2)}
print(d2)

dict={1:'tt',2:'yy',3:'uu'}
print(list(dict))


if 'a'<'A':
    print('ok')

    """

