numbers_tuple = (10, 20, 30, 40, 50)

while True:
    print("tuple:", numbers_tuple)

    index_to_remove = int(input("tuple item: "))

    if index_to_remove == -1:
        print("program end.")
        break
    elif 0 <= index_to_remove < len(numbers_tuple):
        numbers_list = list(numbers_tuple)
        numbers_list.pop(index_to_remove)
        numbers_tuple = tuple(numbers_list)
        print("deleted", index_to_remove)
    else:
        print("The index is not entered correctly")
