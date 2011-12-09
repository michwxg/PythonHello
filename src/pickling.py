import pickle as p
'''
数据持久化
'''

shoplistfile = 'shoplist.data'
shoplist = ['apple','mango','carrot']

aFile = open(shoplistfile, 'wb')
p.dump(shoplist, aFile)
aFile.close()

'''
增加注释
'''