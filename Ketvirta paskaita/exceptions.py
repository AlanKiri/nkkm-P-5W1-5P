while True:
    # try:
    #     number = int(input("Input a integer: "))
    # except ValueError:
    #     print('You entered wrong data.')
    #     print('Int please...')

    try:
        by = int(input('Input 0: '))
        print(100 / by)
    except ZeroDivisionError as inst:
        print(inst)
        print('test')
    # except ValueError:
    #     print('Please enter a int')
    except Exception as inst:
        print(inst)
        print('error')
