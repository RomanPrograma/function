# -*- coding: cp1251 -*-
try:
    def string(list):
        if len(list)<6:
            return "Недостатньо символів"
        else:
            return list[:3] + list[-3:]
    print(string('Добрий вечір!'))
except Exception as e:
    print(f'error: {e}')


