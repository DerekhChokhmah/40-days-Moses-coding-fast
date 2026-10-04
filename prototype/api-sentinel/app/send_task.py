from database import check_monitor
print(check_monitor.delay(1))
print(check_monitor.delay(2))
print(check_monitor.delay(3))
print(check_monitor.delay(4))
print(check_monitor.delay(5))
