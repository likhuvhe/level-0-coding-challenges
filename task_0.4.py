def even_or_odd(num):
    if isinstance(num, int):
        if num % 2 == 0:
            print("even")
        else:
            print("odd")