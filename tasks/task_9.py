byte_size = 1234567890

kilo_size = byte_size / 1024
mega_size = kilo_size / 1024
giga_size = mega_size / 1024

print('Объём информации ' + str(byte_size) + ' байт' + '\n'
      + 'В килобайтах: ' + str(kilo_size) + '\n'
      + 'В мегабайтах: ' + str(mega_size) + '\n'
      + 'В гигабайтах: ' + str(giga_size) + '\n')
