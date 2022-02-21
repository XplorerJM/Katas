from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(monts=1, weeks=1, hour=10)
print(now)

pause