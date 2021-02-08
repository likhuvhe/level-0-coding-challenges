def common_letter(str1, str2):
    common = list(set(str2) & set(str1))
    print("".join(common))