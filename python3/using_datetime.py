from datetime import datetime
from datetime import timedelta

date_str = 'December 14, 2017'
now = datetime.now()
delay14 = now + timedelta(days=-40)   # 计算14天之后的时间
dt = datetime.strptime(date_str, '%B %d, %Y')
print(dt.strftime('%Y-%m-%d'), now, delay14)
print(dt < delay14)

