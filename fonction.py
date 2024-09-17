import string
import numpy
from numpy import matrix
from numpy import linalg

#fonction tester la numerisation d'un chaine de caractaire
def testN(key):
    N=string.digits
    test=False
    res=0
    if len(key)>0:
         if key[0]=="-":
            key=key[1:]
         for i in key :
             for j in N :
                  if i==j:
                     res=res+1
         if res==len(key):
              test=True
    return test

#fonction tester si la chaine est un entier positif
def testPosInt(key):
    N=string.digits
    test=False
    res=0
    if len(key)>0:
         for i in key :
             for j in N :
                  if i==j:
                     res=res+1
         if res==len(key):
              test=True
    return test 

#tester si le message contion au moins un lettre 
def testalpha(x):
    res=False
    for i in x:
        if possitionMaj(i)>0 or possitionMin(i)>0:
            res=True
            break
    return res  

#fonction pour tester si la lettre est appartien l'alphaber majuscuel est returner leur position
def possitionMaj(x):
    ALPHA=string.ascii_uppercase
    l=len(ALPHA)
    pos=-1
    for i in range(l):
        if ALPHA[i]==x :
            pos=i
            pos=pos+1
    return pos

#fonction pour tester si la lettre est appartien l'alphaber minuscule est returner leur position
def possitionMin(x):
    alpha=string.ascii_lowercase
    l=len(alpha)
    pos=-1
    for i in range(l):
        if alpha[i]==x :
            pos=i
            pos=pos+1
    return pos

#Fonction pour returner la lettre apartire  d'un possition 
def getLetPos(x,y):
    ALPHA=string.ascii_uppercase
    alpha=string.ascii_lowercase
    x=x-1
    if x==-1:
        x=25
    res=''
    if y==1:
        res=ALPHA[x]
    elif y==2 :
        res=alpha[x]
    return res

#Fonction de cryptage :chiffrement de cezare
def crypter1(message,key):
    messagec=''
    for i in message:
        pM=possitionMaj(i)
        pm=possitionMin(i)
        if pM >= 0:
            nwepos=(pM+key)%26
            messagec=messagec+str(getLetPos(nwepos,1))
        elif pm >= 0:
            nwepos=(pm+key)%26
            messagec=messagec+str(getLetPos(nwepos,2))
        else:
            messagec=messagec+i
    return messagec

#Fonction qui rteturner la postion de lettre apres le decryptage
def getposdecyptage(x,key):
     key=key%26
     pos=x
     while key > 0:
         pos=pos-1
         key=key-1
         if pos==0:
             pos=26
     return pos

#Fonction de decryptage :dechiffrement de cezare
def decrypter1(messagec,key):
     messagedc=''
     for i in messagec:
        pM=possitionMaj(i)
        pm=possitionMin(i)
        if pM >= 0:
           newpos=getposdecyptage(possitionMaj(i),key)
           messagedc=messagedc+str(getLetPos(newpos,1))
        elif pm >= 0:
            newpos=getposdecyptage(possitionMin(i),key)
            messagedc=messagedc+str(getLetPos(newpos,2))
        else:
             messagedc=messagedc+i
     return messagedc

#fonction pour tester si la kley est alphabitique
def testAlphaKey(key):
     test=0
     res=False
     if len(key)>0:
         for i in key:
             if possitionMaj(i) >=0 or possitionMin(i) >=0 :
                 test=test+1
             else:
                  break
         if test==len(key):
             res=True
     return res

#fonction pour mettre les possition de lettre dans l'alphaber dans un liste d'entier
def remplasekey(key):
     liste=[]
     for i in key:
         pM= possitionMaj(i)
         pm=possitionMin(i)
         if pM >=0:
             liste.append(pM)
         elif pm >=0 :
            liste.append(pm)
     return liste 

#fonction de cryptage : chiffrement vigenere
def cryptage2(message,key):
    Liste=remplasekey(key)
    messagec=""
    j=0
    for i in message:
        messagec=messagec+crypter1(i,Liste[j])
        j=j+1
        if j==(len(Liste)):
            j=0
    return messagec
 
#fonction de decryptage :dechiffrement vigenere
def decryptage2(messagec,key):
    Liste=remplasekey(key)
    messagedc=""
    j=0
    for i in messagec:
        messagedc=messagedc+decrypter1(i,Liste[j])
        j=j+1
        if j==(len(Liste)):
            j=0
    return messagedc
#fonction permettre de saisire un matrice 
def saisirMatrice(dim,l):
    M=[]
    k=0
    for i in range(dim):
        M.append([0]*dim)
        for j in range(dim):
         M[i][j]=l[k]
         k=k+1
    return M

#cette fonction ajouter des '*' pour la lengeur de message divese sur les numbre de matrice
def corrigemessage1(message,m):
    newmessage=message
    while len(newmessage)%m > 0:
           newmessage=newmessage+'*'
    return newmessage

#cette fonction permettre de diviser le message sur un matrice
def devisemessage(message,m):
    newmessage=message
    dm=[]
    dm1=[]
    for i in newmessage:
        dm1.append(i)
        if len(dm1)%m ==0:
            dm.append(dm1)
            dm1=[]
    return dm

#remplasser les caractére dons le matrice par leur possition
def remplasseMatrice(message,key):
    m=len(message)
    n=key
    new=message
    for i in range(m):
        for j in range(n):
            pM=possitionMaj(message[i][j])
            pm=possitionMin(message[i][j])
            if pM > 0:
                new[i][j]=pM
            elif pm >0:
                new[i][j]=pm
            else :
                new[i][j]=0
    return new
#fonction pour calculer le produit de deux matrice
def produitMatrice(l,key):
    newm=[]
    m=len(key)
    p=len(l)
    for i in range(p):
        md=l[i]
        md2=[]
        for j in range(m):
            md1=0
            for k in range(m):
                md1=md1+key[j][k]*md[k]
            md2.append(md1)
        newm.append(md2)
    for i in range(p):
        for j in range(m):
            if l[i][j]==0:
                newm[i][j]=0

    return newm

#cette fonction suprimer les '*' ajouter par corrigemessage1 apres le cryptage
def corrigemessage2(m,l):
    newm=""
    for i in range(l):
        newm=newm+m[i]
    return(newm)
    
# Finds the inverse of matrix A mod p
def modMatInv(A,p):       
  n=len(A)
  A=matrix(A)
  adj=numpy.zeros(shape=(n,n))
  for i in range(0,n):
    for j in range(0,n):
      adj[i][j]=((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
  return (modInv(int(round(linalg.det(A))),p)*adj)%p

# Finds the inverse of a mod p, if it exists
def modInv(a,p):          
  for i in range(1,p):
    if (i*a)%p==1:
      return i
  raise ValueError(str(a)+" has no inverse mod "+str(p))

# Return matrix A with the ith row and jth column deleted
def minor(A,i,j):    
  A=numpy.array(A)
  minor=numpy.zeros(shape=(len(A)-1,len(A)-1))
  p=0
  for s in range(0,len(minor)):
    if p==i:
      p=p+1
    q=0
    for t in range(0,len(minor)):
      if q==j:
        q=q+1
      minor[s][t]=A[p][q]
      q=q+1
    p=p+1
  return minor
#fonction de cryptage:chiffrement de hill
def cryptage3(message,key):
    l=len(message)
    m=len(key)
    messagecoriger=corrigemessage1(message,m)
    nmessage=devisemessage(messagecoriger,m)
    newm=remplasseMatrice(nmessage,m)
    newm=produitMatrice(newm,key)
    newmc=''
    n=len(nmessage)
    k=0
    for i in range(n):
        for j in range(m):
            pM=possitionMaj(messagecoriger[k])
            pm=possitionMin(messagecoriger[k])
            pos=(newm[i][j])%26
            if pM > 0:
                newmc=newmc+(getLetPos(pos,1))
            elif pm > 0:
                newmc=newmc+(getLetPos(pos,2))
            else:
                newmc=newmc+messagecoriger[k]
            k=k+1
    newmc=corrigemessage2(newmc,l)
    return newmc





