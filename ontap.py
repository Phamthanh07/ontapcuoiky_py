class Product:
    def __init__(self, id, name, import_price, quantity, storage_fee):
        self.id = id
        self.name = name
        self.import_price=  import_price
        self.quantity = quantity
        self.storage_fee = storage_fee
        self.total_value = 0
        self.stock_status = ""


        self.calculate_total_value()
        self.classify_stock_status()

    def calculate_total_value(self):
        self.total_value = (self.import_price * self.quantity) + self.storage_fee

    def classify_stock_status(self):
        if self.total_value >= 30000000:
            self.stock_status = "Rat cao(rui ro u dong von)"

        elif self.total_value >= 15000000:
            self.stock_status = "Cao (can chu y)"

        elif self.total_value >= 9000000:
            self.stock_status = "Trung binh"

        else:
            self.stock_status = "Thap"

class ProductManager:
    def __init__(self):
        self.products = []

    def find_by_id(self,product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def add_product(self):
        try:
            product_id = input("Nhap vao id ban muon them: ").strip()

            if product_id == "":
                print("Ma san pham khong duoc de trong")
                return

            if self.find_by_id(product_id):
                print("Ma nay da ton tai!")
                return

            name_input = input("Nhap vao ten san pham: ").strip()

            if name_input == "":
                print("Ten san pham khong duoc de trong")
                return

            import_price_input = float(input("Nhap vao gia san pham: "))
            storage_fee_input = int(input("Nhap vao chi phi kho: "))
            quantity_input = int(input("Nhap vao so luong ton kho: "))

            if import_price_input < 0:
                print("Gia san pham khong dc nho hon 0")
                return

            if storage_fee_input < 0:
                print("Chi phi kho khong dc nho hon 0")
                return

            if quantity_input < 0 or quantity_input > 1000:
                print("Da vuot qua gioi han suc chua cua ke")
                return

            product = Product(
                product_id, name_input, import_price_input, quantity_input, storage_fee_input
            )

            self.products.append(product)

            print("Da them thanh cong san pham")

        except ValueError:
            print("Du lieu khong hop le")

    def show_all(self):
        if not self.products:
            print("Khong co san pham...")
            return

        print("-"*120)
        print(f"{'MA SP':<10} {'TEN SP':<20} {'GIA NHAP SP':<15} {'SO LUONG':<10} {'CHI PHI KHO':<10} {'TONG KHO':<10} {'TRANG THAI':<20}")

        for product in self.products:
            print(f"{product.id:<10} {product.name:<20} {product.import_price:<15} {product.quantity:<10} {product.storage_fee:<10} {product.total_value:<10} {product.stock_status:<20}")

    def update_product(self):
        if not self.products:
            print("KHONG CO SAN PHAM")
            return

        id_input = input("Nhap id can cap nhat: ")

        product = self.find_by_id(id_input)

        if not product:
            print("Khong tim thay san pham")
            return

        try:
            import_price = float(input("Nhap gia nhap moi: "))
            quantity = int(input("Nhap so luong moi: "))
            storage_fee = int(input("Nhap chi phi kho: "))
            if import_price < 0:
                    print("Gia san pham khong dc nho hon 0")
                    return
            
            if storage_fee < 0:
                    print("Chi phi kho khong dc nho hon 0")
                    return
            
            if quantity < 0 or quantity > 1000:
                print("Da vuot qua gioi han suc chua cua ke")
                return

            product.import_price = import_price
            product.quantity = quantity
            product.storage_fee = storage_fee
            product.calculate_total_value()
            product.classify_stock_status()

            print("CAP NHAT SAN PHAM THANH CONG")

        except ValueError:
            print("Du lieu khong hop le")

def menu():
    print("===== MENU =====")
    print("1. Hien thi danh sach san pham trong kho")
    print("2. Nhap san pham moi vao kho")
    print("3. Cap nhat thong tin san pham")
    print("4. Xoa san pham khoi kho")
    print("5. Tim khiem san pham theo ten")
    print("6. Thoat")

def main():
    manager = ProductManager()

    while True:
        menu()
        choice = input("Nhap lua chon cua ban: ")

        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_product()
            case "3":
                manager.update_product()
            case "6":
                print("Thoat chuong trinh")

            case _:
                print("Lua chon khong hop le")

if __name__ == "__main__":
    main()