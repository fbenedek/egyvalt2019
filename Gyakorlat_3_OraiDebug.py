kartyak = ['2383 8823 9423 1164']

def kartyaStrListavaKonvertalas(kartya):
  '''
  Listává konvertálja a str-ként beolvasott adatot, és törli a szóközöket.
  '''
  kartyaAdatLista=[]
  for karakter in kartya:
    if karakter != ' ':
      kartyaAdatLista.append(karakter)

  return kartyaAdatLista

def szamjegyOsszeg(szam):
  '''
  Egy tízes számrendszerbeli, strként vagy listaként addot szám jegyeinek összegét számolja ki.
  '''
  osszeg=0
  for jegy in szam:
    osszeg+=int(jegy)

  return osszeg

def LuhnAtalakitas(kartyalista):
  '''
  A listaként megkapott kártyaszámot várja, és egy olyan listát ad vissza, aminek az elemeit összegezve ellenőrizhető az érvényesség.
  '''
  for index, karakter in enumerate(kartyalista):
    if index%2 == 0:
      ujErtek = 2*int(karakter)
      if ujErtek >= 10:
        ujErtek = szamjegyOsszeg(karakter)
      kartyalista[index] = str(ujErtek)
  return kartyalista
