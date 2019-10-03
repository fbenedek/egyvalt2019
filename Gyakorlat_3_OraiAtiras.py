kartyak = ['2383 8823 9423 1164']

for kartya in kartyak:
  kartyaCheck = []
  for karakter in kartya:
    if karakter != ' ':
      kartyaCheck.append(karakter)
  print(kartyaCheck)
  for index, karakter in enumerate(kartyaCheck):
    if index%2 == 0:
      double = 2*int(karakter)
      if double >= 10:
        double = int(str(double)[1])+int(str(double)[0])
      kartyaCheck[index] = str(double)
  print(kartyaCheck)
  kartyaCheckSum = 0
  for karakter in kartyaCheck:
    kartyaCheckSum += int(karakter)
  print(kartyaCheckSum)