
try:
   import statistics
   list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   list_avarange = statistics.mean(list)
   print(f'avarange: {list_avarange}')
except Exception as e:
    print(f'error: {e}')




    #інпут не осилив
try:
    def list_av(list):
        list = list(map(int(input('enter number: ').split())))
        return list
    print(list_av(list)/len(list))

except Exception as e:
    print(f'error: {e}')
