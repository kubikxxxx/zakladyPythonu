from time import sleep

number_input = 0
while number_input != 73:
    print("co je perfektní číslo?")
    number_input = input("zadejte výsledek:")
    if int(number_input) == 73:
        print(f"přesně tak, číslo {number_input} je nejlepší číslo, zkuste si zjistit proč")
        secured_input = input("krásně, teď zadejte číslo a tento program ho uhodne:")
        for i in range (0,8):
            print("probýhají složité výpočty...")
            sleep(1)
        print("dle výpočtů je vámi zadané číslo: {}".format(secured_input))

    else:
        print("špatně, číslo {} není perfektní (ovšem každý to může vidět jinak :) )".format(number_input))
        if int(number_input) < 73:
            print(f"zkuste větší číslo než {number_input}")
        elif int(number_input) > 73:
            print("zkuste menší číslo než {}".format(number_input))
