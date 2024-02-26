import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib as mpl
from matplotlib.dates import DateFormatter
import random

# crea la figura e gli assi
fig, ax = plt.subplots(figsize=(12, 12))

number_of_colors = 8

def init():
    # imposto i nomi degli assi
    ax.set_xlabel('data e ora')
    ax.set_ylabel('prezzi stock')
    # imposto il titolo
    ax.set_title('prezzi stock META/minuto', pad=20, fontsize=20, font='times new roman', weight='bold')
    ax.xaxis.set_major_formatter(DateFormatter('%m-%d %H:%M'))
     # chiamo l'api per i dati che servono
    data = callApi()
    # imposto ascisse e ordinate
    x = data.index
    y1 = data.iloc[:,0]
    y2 = data.iloc[:,1]
    y3 = data.iloc[:,2]
    y4 = data.iloc[:,3]

    # disegno il grafico
    open = ax.plot(x, y1, color= random_color(), label="Open")
    high = ax.plot(x, y2, color= random_color(), label="High")
    low = ax.plot(x, y3, color= random_color(), label="Low")
    close = ax.plot(x, y4, color= random_color(), label="Close")
    fig.legend(loc='outside upper right')

def callApi():
    d = yf.download("META", interval="1m", period="1d")
    df = pd.DataFrame(data=d)
    return df

def random_color():
    color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    return color

def update(i):
    # cancello il disegno
    ax.clear()
    # la funzione init reimposta il grafico con le labels principali
    init()

init() 
# ogni minuto il grafico viene aggiornato
ani = anim.FuncAnimation(plt.gcf(), update, interval=60000, cache_frame_data=False)
plt.show()

