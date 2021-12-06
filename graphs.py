from typing import List
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

df=pd.read_excel('Reacher-v2/f0.xlsx')

epochs=df['Episode'][1:]
last_reward=df['Last reward'][1:]
average_reward=df['Average reward'][1:]
plt.plot(epochs,average_reward,label="f0 : 0.01  avg rwd")

# plt.plot(epochs,last_reward,label="f0 : 0.01  current rwd")


df=pd.read_excel('Reacher-v2/f1.xlsx')

epochs=df['Episode'][1:]
last_reward=df['Last reward'][1:]
average_reward=df['Average reward'][1:]
plt.plot(epochs,average_reward,label="f1 : 0.01+([n/10])*0.005  avg rwd")

# plt.plot(epochs,last_reward,label="f1 : 0.01+([n/10])*0.005  current rwd")


df=pd.read_excel('Reacher-v2/f2.xlsx')

epochs=df['Episode'][1:]
last_reward=df['Last reward'][1:]
average_reward=df['Average reward'][1:]
plt.plot(epochs,average_reward,label="f2 : 0.01+([n/10])*0.01  avg rwd")

# plt.plot(epochs,last_reward,label="f2 : 0.01+([n/10])*0.01  current rwd")


df=pd.read_excel('Reacher-v2/f3.xlsx')

epochs=df['Episode'][1:]
last_reward=df['Last reward'][1:]
average_reward=df['Average reward'][1:]
plt.plot(epochs,average_reward,label="f3 : 0.01+log10(n)*0.1  avg rwd")

# plt.plot(epochs,last_reward,label="f3 : 0.01+log10(n)*0.1  current rwd")

df=pd.read_excel('Reacher-v2/f4.xlsx')

epochs=df['Episode'][1:]
last_reward=df['Last reward'][1:]
average_reward=df['Average reward'][1:]
plt.plot(epochs,average_reward,label="f4 : 0.5  avg rwd")

# plt.plot(epochs,last_reward,label="f4 : 0.5  current rwd")

df=pd.read_excel('Reacher-v2/f5.xlsx')

epochs=df['Episode'][1:]
last_reward=df['Last reward'][1:]
average_reward=df['Average reward'][1:]
plt.plot(epochs,average_reward,label="f5 : 0.5 - ([n/10])*0.01  avg rwd")

# plt.plot(epochs,last_reward,label="f5 : 0.5 - ([n/10])*0.01  current rwd")

df=pd.read_excel('Reacher-v2/f6.xlsx')

epochs=df['Episode'][1:]
last_reward=df['Last reward'][1:]
average_reward=df['Average reward'][1:]
plt.plot(epochs,average_reward,label="f6 : 0.5/exp([n/10])  avg rwd")

# plt.plot(epochs,last_reward,label="f6 : 0.5/exp([n/10]) current rwd")

df=pd.read_excel('Reacher-v2/f7.xlsx')

epochs=df['Episode'][1:]
last_reward=df['Last reward'][1:]
average_reward=df['Average reward'][1:]
plt.plot(epochs,average_reward,label="f7 : 0.01+0.8/(x+1)  avg rwd")

# plt.plot(epochs,last_reward,label="f7 : 0.01+0.8/(x+1) current rwd")

df=pd.read_excel('Reacher-v2/f8.xlsx')

epochs=df['Episode'][1:]
last_reward=df['Last reward'][1:]
average_reward=df['Average reward'][1:]
plt.plot(epochs,average_reward,label="f8 : 0.01+0.8/(x*x+1)  avg rwd")

# plt.plot(epochs,last_reward,label="f8 : 0.01+0.8/(x*x+1) current rwd")

plt.xlabel("No. of episodes")
plt.ylabel("Average reward")
plt.legend()
plt.show()