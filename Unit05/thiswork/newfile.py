import os
filename = 'helloworld.txt'

if os.path.exists(filename):
    os.remove(filename)
else:
    with open(filename, 'w') as f:
        f.write('helloworld')
