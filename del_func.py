
from math import exp, log10


def f0(max_kl,epoch):
    return max_kl

def f1(max_kl,epoch):
    return max_kl+(epoch//10)*0.005

def f2(max_kl,epoch):
    return max_kl+0.01*(epoch//10)

def f3(max_kl,epoch):
    return max_kl+log10(epoch)*(0.1)

def f4(max_kl,epoch):
    return 0.5

def f5(max_kl,epoch):
    return 0.5 - (epoch//10)*0.01

def f6(max_kl,epoch):
    return 0.5/exp(epoch//10)

def f7(max_kl,epoch):
    x=epoch//30
    return 0.01+0.8/(x+1)

def f8(max_kl,epoch):
    x=epoch//30
    return 0.01+0.8/(x*x+1)
