def main(): 
  print("Please select one of the following destinations.", '\n', "1. Hawaii ", '\n', '2. Bahamas', '\n', '3. Cancun')
  destinations = input()
  if destinations == "1"or "Hawaii":
    carrier(destinations)
  elif destinations == '2' or 'Bahamas':
    carrier(destinations)
  elif destinations == '3' or "Cancun":
    carrier(destinations)
  else:
    print('Blah')
def carrier(destinations):
  print("Please select one of the following carriers.", '\n', "1. US Air ", '\n', '2. Delta', '\n', '3. United')
  carrier =input()
  if carrier == '1' or 'US Air':
    passengers(carrier,destinations)
  elif carrier == '2' or 'Delta':
    passengers(carrier,destinations)
  elif carrier == '3' or "United":
    passengers(carrier,destinations)
  else:
    print('Blah')
def passengers(carrier,destinations):
  print("Passenger Menu", '\n', "1. One passenger", '\n', "2. Two passengers", '\n', '3. Three passengers')
  passengers = input()
  if passengers == '1' or 'One':
   calculations(passengers,carrier,destinations)
  elif passengers == '2' or 'Two':
    calculations(passengers,carrier,destinations)
  elif passengers == '3' or "Three":
     calculations(passengers,carrier,destinations)
  elif passengers == '4' or "Four":
     calculations(passengers,carrier,destinations)
  else:
    print('Blah')
def calculations(passengers,carrier,destinations):
  if destinations == 'Hawaii' or '1':
    if carrier == 'US Air' or'1':
      if passsengers == '1':
  elif destinations =='Bahamas' or '2':
    if carrier == 'US Air'or '1':
      if passengers == '1':
  elif destinations == 'Cancun' or '3':
    
  print(passengers,carrier,destinations)
main()