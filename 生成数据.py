import matplotlib.pyplot as plt

input_values=[i for i in range(1,6)]
squares = [1, 4, 9, 16, 25]

# plot()绘制出有意义的图形
# show()打开matplotlib查看器
# plot(列表名，列表名，linewidth=线条粗细)
# title()给图表指定标题
# xlabel()，ylabel()为每条轴设置标题
# tick_prarms()设置刻度样式，axes='both'对x和y轴上都标上刻度

plt.plot(input_values, squares, linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()
