if __name__ == "__main__":

    dict_a = {1:10, 2:20}
    dict_b = {3:30, 4:40}
    dict_c = {5:50, 6:60} 

    print(f'res = { {**dict_a, **dict_b, **dict_c} }')