def add_time(start, duration, day='None'):
  a = str(start).split(':')
  b = str(duration).split(':')
  somaDasHorasResto = (int(a[0]) + int(b[0]))%12
  startMinAmPm = a[1].split()
  durationMin = b[1]
  somaDasHorasQuo = (int(a[0]) + int(b[0]))//12  
  SomaMin = int(startMinAmPm[0]) + int(durationMin)
  horasResiduais = SomaMin // 60
  QuoSomaHorasMin = (int(a[0]) + int(b[0]) + horasResiduais)//12
  HorasTotais = int(somaDasHorasResto) + int(horasResiduais)
  MinTotais = int(SomaMin) % 60
  DaysUp = ['S', 'M', 'T', 'W', 'T', 'F', 'S']
  DaysDown = ['s', 'm', 't', 'w', 't', 'f', 's']
  Days = ['Sunday', 'Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday']

  if startMinAmPm[1] == 'AM':
    if QuoSomaHorasMin == 0:
      t = 'AM'

    if QuoSomaHorasMin % 2 == 0:
      t = 'AM'

    if QuoSomaHorasMin % 2 != 0:
      t = 'PM'

  else:
    if QuoSomaHorasMin == 0:
      t = 'PM'      

    if QuoSomaHorasMin % 2 == 0:
      t = 'PM'

    if QuoSomaHorasMin % 2 != 0:
      t = 'AM' 
    
  match = False
  i = 0

  if day != 'None':
    x = 0
    while x <= len(DaysUp) - 1:
      if DaysUp[x] == day[0] or DaysDown[x] == day[0] :
        match = True
      if match == True:
        i = x
      x += 1
      match = False
    if i == 4:
      if day[1] == 'u' or day[1] == 'U':
        i = 2
    if i == 6:
      if day[1] == 'u' or day[1] == 'U':
        i = 0
        
  
  var = 7 - (i + 1)

  if startMinAmPm[1] == 'AM':
    if QuoSomaHorasMin == 0 or QuoSomaHorasMin == 1:
      aviso = ''
      i2 = i
    if QuoSomaHorasMin == 2 or QuoSomaHorasMin == 3:
      aviso = '(next day)'
      i2 = (int(i) + 1)%7
    if QuoSomaHorasMin >= 4:
        aviso = str('(') + str((QuoSomaHorasMin)//2) + str(' ') + str('days later)')
        var2 = int(QuoSomaHorasMin)//2
        i2 = (int(i) + int(var2))%7
        
  else:
    if QuoSomaHorasMin == 0:
      aviso = ''
      i2 = i
    if QuoSomaHorasMin == 1 or QuoSomaHorasMin == 2:
      aviso = '(next day)'
      i2 = (int(i) + 1)%7
    if QuoSomaHorasMin >= 3:
      if QuoSomaHorasMin % 2 == 0:
        aviso = str('(') + str((QuoSomaHorasMin)//2) + str(' ') + str('days later)')
        var2 = int(QuoSomaHorasMin)//2
        i2 = (int(i) + int(var2))%7
      else:
        aviso = str('(') + str((QuoSomaHorasMin + 1)//2) + str(' ') + str('days later)')
        var2 = int(QuoSomaHorasMin + 1)//2
        i2 = (int(i) + int(var2))%7
      
  if day != 'None':
    dayOutput = str(', ') + str(Days[i2])
  else:
    dayOutput = str('')
    


  return new_time(HorasTotais, MinTotais, t, aviso, dayOutput)


def new_time(HorasTotais, MinTotais, t, aviso, dayOutput):
  print(HorasTotais, ':', '{:0{align}{width}}'.format(MinTotais, align='>', width='2'), ' ', t, dayOutput, ' ', aviso, ' ', sep='')
