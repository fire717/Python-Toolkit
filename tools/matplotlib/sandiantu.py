def plotData(x,y):
    fig = plt.figure(figsize=(30,20))  
    #ax= fig.add_subplot(111) #使画在一个图上
    ax1 = plt.scatter(x, y, marker = 'x', color = 'b')  
    plt.xlabel('time') 
    plt.ylabel('price')
    plt.show()

plotData(plot_x_list,plot_y)