import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth = 5,marker = "o")
#Set chart title and lable axis
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 24)
plt.ylabel("Square of value",fontsize = 24)
#Set size of tick labels
plt.tick_params(axis="both",labelsize = 12)
plt.show()

