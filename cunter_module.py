from collections import Counter
import random
list1 = random.sample(range(10), k=4)
list2 = random.sample(range(10), k=4)
list3 = random.sample(range(10), k=4)
list4 = random.sample(range(10), k=4)


print(list1)


liste_listesi = [list1, list2, list3, list4]
list_toplam = list1 + list2 + list3 + list4

print (liste_listesi)
print(list_toplam)
for index, liste in enumerate(liste_listesi):
    print('{}, liste \t {}'.format(index, liste))
print(Counter(list_toplam))
print(Counter("adsfdgddghfje"))


sarki = """Ağla kalbim ağla sen ağla kalbim ağla
Sus sesin duyulmasın içinden ağla
Ağla kalbim ağla sen ağla kalbim ağla
Sus sesin duyulmasın içinden ağla
İçinden ağla"""

print (sarki)
print(Counter(sarki))
print (Counter(sarki.split()))
print(sarki.lower())
print(sarki.lower().split())
print(Counter(sarki.lower().split()))



