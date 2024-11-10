import numpy as np
import ipywidgets as widgets
from bqplot import pyplot as plt
import bqplot

n = 200

x = np.linspace(0.0, 10.0, n)
y = np.cumsum(np.random.randn(n)*10).astype(int)

label_selected = widgets.Label(value="Selected: 0")
label_selected


fig = plt.figure( title='Histogram')
np.random.seed(0)
hist = plt.hist(y, bins=25)
hist.scales['sample'].min = float(y.min())
hist.scales['sample'].max = float(y.max())
display(fig)
fig.layout.width = 'auto'
fig.layout.height = 'auto'
fig.layout.min_height = '300px' # so it shows nicely in the notebook
fig.layout.flex = '1'


fig = plt.figure( title='Line Chart')
np.random.seed(0)
n = 200
p = plt.plot(x, y)
fig

fig.layout.width = 'auto'
fig.layout.height = 'auto'
fig.layout.min_height = '300px' # so it shows nicely in the notebook
fig.layout.flex = '1'

brushintsel = bqplot.interacts.BrushIntervalSelector(scale=p.scales['x'])

def update_range(*args):
    label_selected.value = "Selected range {}".format(brushintsel.selected)
    mask = (x > brushintsel.selected[0]) & (x < brushintsel.selected[1])
    hist.sample = y[mask]
    
brushintsel.observe(update_range, 'selected')
fig.interaction = brushintsel