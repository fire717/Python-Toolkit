import matplotlib.pyplot as plt
def draw_hist(nums):
    plt.hist(nums,200)
    plt.xlim(0,5020)
    
    plt.xlabel('number')
    plt.ylabel('counts')

    plt.show()

draw_hist(wifi_num)