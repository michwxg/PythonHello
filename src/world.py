ab = {
      'miko': '33@qq.com',
      'shuang': 'kdk@gmail.com'
      }

ab['kang'] = 'kk@msn.com'

for name, address in ab.items():
    #print("name is %s, address is %s" % (name, address))
    pass

shoplist = ['mango', 'banana', 'apple']

print(shoplist[0])
print(shoplist[0:-1])

delimeter = '**'
print(delimeter.join(shoplist))
