# -*- coding: cp1251 -*-
try:
    def string(list):
        if len(list)<6:
            return "����������� �������"
        else:
            return list[:3] + list[-3:]
    print(string('������ �����!'))
except Exception as e:
    print(f'error: {e}')


