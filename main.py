from beispiel_funktional import multipliziere_liste_funktional
from beispiel_funktional import multipliziere_liste_funktional2
from beispiel_funktional import multipliziere_liste_funktional2_python
from beispiel_funktional import groesser_als
from beispiel_funktional import groesser_als_python
from beispiel_funktional import summe
from beispiel_funktional import anzahl_gerade
from beispiel_funktional import anzahl_gerade2
from beispiel_funktional import curry
from beispiel_funktional import foo
from beispiel_funktional import mein_filter
from beispiel_funktional import mein_filter_inner

print(multipliziere_liste_funktional([3,4,2,5], 3))
print(multipliziere_liste_funktional2([3,4,2,5], 3))
print(multipliziere_liste_funktional2_python([3,4,2,5], 3))
print(groesser_als([3,4,2,5,7], 4))
print(groesser_als_python([3,4,2,5,7], 4))
print(summe([3,4,2,5,7]))
print(anzahl_gerade([3,4,2,5,7, 8, 10]))
print(anzahl_gerade2([3,4,2,5,7, 8, 10]))

bar = curry(foo, 5)
print(bar(3, 2))

print(mein_filter(lambda x: x > 3, [1,3,2,4,5]))
print(mein_filter_inner(lambda x: x > 3, [1,3,2,4,5]))