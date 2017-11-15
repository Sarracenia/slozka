
# coding: utf-8

# In[41]:

import random
pozdravy = []
pozdravy.append("Ahoj")
pozdravy.append("Nazdárek")
pozdravy.append("Zdar")
pozdravy.append("Hoj")
pozdravy.append("Čus")
osloveni = []
osloveni.append("Kubo")
osloveni.append("Kubíčku")
osloveni.append("Tubo")
osloveni.append("Tubíčku")
print(random.sample(pozdravy, 1)+random.sample(osloveni, 1)) 
if input("Chtěl bys přidat oslovení? ") == "ano":
    b=input("A jaké by jsi chtěl přidat?")
    osloveni.append(b)
else:
    print("Tak né no") 
if input("A pozdrav by jsi přidat chtěl?") == "ano":
    d=input("A jaký by jsi chtěl přidat?")
    pozdravy.append(d)
else:
    print("Tak si trhni no")

