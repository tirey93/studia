import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

df = pd.read_csv("scores.csv") 

print(df.head(10))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_trisurf(df['th_min'], df['th_max'], df['rmse'], 
                       cmap=cm.viridis,  
                       edgecolor='none')

norm = plt.Normalize(vmin=df['blur'].min(), vmax=df['blur'].max()) 
sm = cm.ScalarMappable(cmap=cm.viridis, norm=norm)
sm.set_array([])
fig.colorbar(sm, ax=ax, shrink=0.5, aspect=10, label='Blur (ksize)')

ax.set_xlabel('FRAME_THRESHOLD_MIN')
ax.set_ylabel('FRAME_THRESHOLD_MAX')
ax.set_zlabel('RMSE')
              
plt.title('Wpływ parametrów na błąd RMSE', fontsize=16)

plt.show()