while True:
    try:
        user_input = input()
        a, b = map(int, user_input.split())
        print(a + b)
        
    except:
        break