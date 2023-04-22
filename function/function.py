try:
    def function():
        a = int(input('Enter a number: '))
        for i in range(1, a ):
            if a % i == 0:
                print(i)
        return a
    print(function())
except Exception as e:
    print(f'error: {e}')
