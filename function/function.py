

try:
    def cap_words():
        text = input('Enter a string: ').split()
        for word in text:
            if word.isalpha():
                print(word.capitalize(), end=' ' )
                
    print(cap_words())
except Exception as e:
    print(f'error: {e}')
