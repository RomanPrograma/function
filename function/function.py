try:
    def avarage(list):
        list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        return sum(list)/len(list)
    print(avarage(list))

except Exception as e:
    print(f'error: {e}')
