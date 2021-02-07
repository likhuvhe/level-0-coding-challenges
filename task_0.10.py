def common_char(str1, str2):
    common = list(set(str2) & set(str1))
    
    commons = ""
    for comn in common:
        commons += f"{comn}, "
    print(commons[:-2])