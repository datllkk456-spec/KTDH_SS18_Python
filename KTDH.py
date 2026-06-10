product_list = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]

def add_product(product_list):
    ID = input("Nhập vào ID sản phẩm: ")
    product_name = input("Nhập tên sản phẩm: ")

    while True:
        try:
            price = int(input("Nhập vào giá bán: "))
            if price > 0:
                break
            print("Giá bán phải lớn hơn 0!")
        except ValueError:
            print("Giá bán phải là số!")

    new_product = {
        "id": ID,
        "name": product_name,
        "price": price
    }

    product_list.append(new_product)

    print("Thêm sản phẩm thành công!")


def show_product(product_list):
    if not product_list:
        print("Cửa hàng hiện chưa có sản phẩm nào!")
    else:
        title = f"__________ DANH SÁCH SẢN PHẨM __________"
        print(title)
        header = f"{'ID':<5} | {'Tên sản phẩm':<15} | {'Giá bán':<12}"
        print(header)
        print("="*len(header))
        for item in product_list:
            print(f"{item['id']:<5} | {item['name']:<15} | {item['price': ,]:<12}")


while True:
    menu_title = f" QUẢN LÍ CỦA HÀNG - MINI STORE ".center(50, "=")
    users_choice = input(f"""
    {menu_title}
    1. Xem danh sách sản phẩm hiện có
    2. Thêm mới một sản phẩm
    3. Cập nhật giá sản phẩm theo ID
    4. Thoát chương trình
    {'='*len(menu_title)}
    Lựa chọn của bạn(1-4): """)
    
    match users_choice:
        case "1":
            show_product(product_list)
        case "2":
            add_product(product_list)
        case "3":
            pass
        case "4":
            print("Thoát chương trình......")
            break
        case _:
            print("Lựa chọn không hợp lệ")
        