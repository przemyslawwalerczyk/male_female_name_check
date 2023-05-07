name = input('Provide a Polish name: ')

if name.endswith('a') == True and name != "Kuba":
  print('This is a female name')
elif (name.endswith('a') == False) or name == "Kuba":
  print('This is a male name')
