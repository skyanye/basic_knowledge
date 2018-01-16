from datetime import datetime

# striptime()日期字符串作为第一个实参，第二个实参告诉python怎么设置日期的格式
first_date = datetime.striptime('2014-7-1', '%Y-%m-%d')
print(first_time)

# %A 星期的名称，如Monday
# %B 月份名，如January
# %m 用数字表示的月份（01-12）
# %d 用数字表示月份中的一天（01-31）
# %Y 四位的年份，如2015
# %y 两位的年份，如15
# %H 24小时制的小时数（00-24）
# %I 12小时制的小时数（01-12）
# %p am或pm
# %M 分钟数（00-59）
# %S 秒数（00-61）
