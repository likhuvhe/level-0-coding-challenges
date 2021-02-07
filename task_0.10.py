def common_letter(str1, str2):
    common = list(set(str2) & set(str1))
    
    commons = ""
    for comn in common:
        commons += f"{comn}, "
    if commons != "":
        print(f"Common letters: {commons[:-2]}")