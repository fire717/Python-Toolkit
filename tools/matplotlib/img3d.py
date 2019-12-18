import mpl_toolkits.mplot3d

x = np.random.randint(0,40,10)
y = np.random.randint(0,40,10)
z = 80*abs(np.sin(x+y))

ax = plt.subplot(projection='3d')

for xx,yy,zz in zip(x,y,z):
    color = np.random.random(3)
    ax.bar3d(xx,
            yy,
            0,
            dx = 1,
            dy = 1,
            dz = zz,
            color=color)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
