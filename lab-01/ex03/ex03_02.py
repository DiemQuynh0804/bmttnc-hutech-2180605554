def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("Nhập danh sách cá số, các nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi đảo ngược là: ", dao_nguoc_list)

def tao_tuple_tu_list(lst):
    return tuple(lst)
