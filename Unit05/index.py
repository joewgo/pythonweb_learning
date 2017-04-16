import os
filename = 'hello_world.txt'

with open(filename,'r') as f:
    result = f.readlines()
    print(result)


'''
if os.path.exists(filename):
    os.remove(filename)
else:
    with open(filename, 'a') as f:
        f.write('HI! 你好喔！')
'''
'''
with open(filename,'w') as f:
  f.write('hello_world中文測試!!!')
'''
