import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

# Primary Palette
def cmap1():
 mpl.rcParams['axes.prop_cycle'] = cycler(color=['#003e51', '#00b0b9', '#bad1ba', '#9ab7c1', '#ffcd00', '#fff5de', '#00b18f'])

# Secondary 
def cmap2():
 import matplotlib as mpl
 from cycler import cycler
 mpl.rcParams['axes.prop_cycle'] = cycler(color=['#f88f23', '#007B81', '#ffcd00', '#9EE1E5'
    ,'#00b0b9', '#FFEFA9', '#E0F6F7', '#ddd', '#d5e1e5', '#003e51', '#f3f3f3', '#e9e9e9'])

# Reset Palette
def cmap_reset():
 mpl.rcParams['axes.prop_cycle'] = cycler(color='bgrcmyk')
