import pandas as pd
import numpy as np
import math

dict={}
def rms(func,env):
    df = pd.read_excel(env+'/'+func+'.xlsx')
    avg_rwd = df['Average reward'][100:]
    mean = np.sum(avg_rwd)/len(avg_rwd)
    avg_rwd = avg_rwd - mean
    sqrd = np.sum(avg_rwd*avg_rwd)
    rms = math.sqrt(sqrd)/len(avg_rwd)

    dict[func] = [rms]
    

for func in ["f0","f1","f2","f3","f4","f5","f6","f7","f8"]:
    rms(func,"Walker-2d")

df = pd.DataFrame(dict)
df.to_excel("Walker-2d/rms.xlsx")