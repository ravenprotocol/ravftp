'''
This scipt deletes all models collected from previous iteration
'''

import os
 
dir = 'collected_model'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))