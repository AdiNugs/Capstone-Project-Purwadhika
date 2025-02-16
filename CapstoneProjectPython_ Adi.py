# CAPSTONE PROJECT 1
# ADI NUGRAHA JCDS 

# CRUD STOK BARANG

# import library
from tabulate import tabulate
import os

# DATA ===================================================================================================================
stokBarang  = [
    {'Nama Produk' : 'Macbook 2023', 'Kode Produk' : 'LAP001', 'Jumlah Stok Awal (Unit)' : 40, 'Pengeluaran (Unit)' : 20, 'Jumlah Stok Akhir (Unit)' : 30, 'Harga satuan (Rp)' : 20000000, 'Nilai Stok Akhir (Rp)' : 600000000},
    {'Nama Produk' : 'OPPO F21', 'Kode Produk' : 'MOB001', 'Jumlah Stok Awal (Unit)' : 50, 'Pengeluaran (Unit)' : 30, 'Jumlah Stok Akhir (Unit)' : 45, 'Harga satuan (Rp)' : 5000000, 'Nilai Stok Akhir (Rp)' : 225000000},
    {'Nama Produk' : 'TV LED 4K', 'Kode Produk' : 'TV001', 'Jumlah Stok Awal (Unit)' : 10, 'Pengeluaran (Unit)' : 10, 'Jumlah Stok Akhir (Unit)' : 5, 'Harga satuan (Rp)' : 12000000, 'Nilai Stok Akhir (Rp)' : 60000000},
    {'Nama Produk': 'Samsung Galaxy S23', 'Kode Produk': 'MOB002', 'Jumlah Stok Awal (Unit)': 30, 'Pengeluaran (Unit)': 10, 'Jumlah Stok Akhir (Unit)': 20, 'Harga satuan (Rp)': 14000000, 'Nilai Stok Akhir (Rp)': 280000000},
    {'Nama Produk': 'iPhone 14 Pro', 'Kode Produk': 'MOB003', 'Jumlah Stok Awal (Unit)': 25, 'Pengeluaran (Unit)': 5, 'Jumlah Stok Akhir (Unit)': 20, 'Harga satuan (Rp)': 19000000, 'Nilai Stok Akhir (Rp)': 380000000},
    {'Nama Produk': 'Dell XPS 15', 'Kode Produk': 'LAP002', 'Jumlah Stok Awal (Unit)': 35, 'Pengeluaran (Unit)': 10, 'Jumlah Stok Akhir (Unit)': 25, 'Harga satuan (Rp)': 18000000, 'Nilai Stok Akhir (Rp)': 450000000},
    {'Nama Produk': 'LG Smart TV 55"', 'Kode Produk': 'TV002', 'Jumlah Stok Awal (Unit)': 15, 'Pengeluaran (Unit)': 7, 'Jumlah Stok Akhir (Unit)': 8, 'Harga satuan (Rp)': 10000000, 'Nilai Stok Akhir (Rp)': 80000000},
    {'Nama Produk': 'Sony Bravia 65"', 'Kode Produk': 'TV003', 'Jumlah Stok Awal (Unit)': 12, 'Pengeluaran (Unit)': 6, 'Jumlah Stok Akhir (Unit)': 6, 'Harga satuan (Rp)': 15000000, 'Nilai Stok Akhir (Rp)': 90000000}
    ]

admin_data = {
    "email": "admin@example.com",
    "password": "admin123"
}

# Function

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# ADMIN ======================================================================================================================
def verify_admin():
    clear_terminal()
    print("🔑 Admin Login Required")
    
    email = input("Masukkan Email Admin: ").strip()
    password = input("Masukkan Password: ").strip()
    
    if email == admin_data["email"] and password == admin_data["password"]:
        return True
    else:
        show_error("❌ Email atau Password salah! Kembali ke sub-menu.")
        return False

# SHOW =======================================================================================================================
def show_table_data(data):
    headers = ["No"] + list(data[0].keys())
    table = [[i + 1] + list(barang.values()) for i, barang in enumerate(data)]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def show_table():
    clear_terminal()
    print("\nData Stok Barang:")
    show_table_data(stokBarang)

def show_error(e):
    clear_terminal()
    print(f"❌ Terjadi kesalahan: {e}")
    input("\nTekan Enter untuk melanjutkan...")
    clear_terminal()

def show_product_codes():
        sorted_products = sorted(stokBarang, key=lambda x: x['Kode Produk'])
        show_table_data([{'Nama Produk': b['Nama Produk'], 'Kode Produk': b['Kode Produk']} for b in sorted_products])

def show_table_sorted_by_kode():
    clear_terminal()
    sorted_data = sorted(stokBarang, key=lambda x: x['Kode Produk']) 
    print("\nℹ️ Data Stok Barang (Sorted by Kode Produk):")
    show_table_data(sorted_data)
    input("\nTekan Enter untuk kembali...")

def show_table_sorted_by_stok():
    clear_terminal()
    sorted_data = sorted(stokBarang, key=lambda x: x['Jumlah Stok Akhir (Unit)'], reverse=True)  
    print("\n📊 Data Stok Barang (Sorted by Jumlah Stok Akhir):")
    show_table_data(sorted_data)
    input("\nTekan Enter untuk kembali...")

def show_updated_item(barang):
    print("\n✅ Data berhasil diperbarui:")
    print(tabulate([barang], headers="keys", tablefmt="fancy_grid"))
    input("\nTekan Enter untuk kembali ke menu update...")

def show_added_item(barang):
    print("\n✅ Produk berhasil ditambahkan:")
    print(tabulate([barang], headers="keys", tablefmt="fancy_grid"))
    input("\nTekan Enter untuk kembali ke menu tambah...")

def confirm_update(field_name, new_value):
    konfirmasi = input(f"🤔 Apakah Anda yakin ingin mengubah {field_name} menjadi '{new_value}'? (y/n): ").strip().lower()
    return konfirmasi == 'y'

# DELETE BARANG ==============================================================================================================
def hapus_stok():
    while True:
        try:
            clear_terminal()
            print("\n🗑️ Sub Menu Hapus Stok:\n")
            menu_options = [
                ["1", "Hapus Produk"],
                ["2", "Kembali ke Menu Utama"]
            ]
            print(tabulate(menu_options, headers=["Pilihan", "Deskripsi"], tablefmt="fancy_grid"))
            pilihan = input("\nPilih sub-menu (1-2): ").strip()

            if pilihan == "1":
                if not verify_admin():
                    continue  
                
                clear_terminal()
                print("\n🗑️ Hapus Produk")
                print(tabulate(stokBarang, headers="keys", tablefmt="fancy_grid"))

                
                kode = input("\nMasukkan Kode Produk yang ingin dihapus (atau ketik 'batal' untuk kembali): ").strip().upper()

                if kode.lower() == "batal":
                    continue

                barang = next((b for b in stokBarang if b['Kode Produk'] == kode), None)

                if not barang:
                    show_error("❌ Kode Produk tidak ditemukan!")
                    continue

                clear_terminal()
                print("\nKonfirmasi Produk yang Akan Dihapus:")
                print(tabulate([barang.values()], headers=barang.keys(), tablefmt="fancy_grid"))

                konfirmasi = input("\nApakah Anda yakin ingin menghapus produk ini? (y/n): ").strip().lower()
                if konfirmasi != "y":
                    print("\n❌ Hapus produk dibatalkan.")
                    input("\nTekan Enter untuk kembali...")
                    continue

                stokBarang.remove(barang)

                clear_terminal()
                print("\n✅ Produk berhasil dihapus!")
                show_table_data(stokBarang)
                input("\nTekan Enter untuk kembali ke sub-menu...")

            elif pilihan == "2":
                break
            else:
                show_error("❌ Pilihan tidak valid, silakan pilih kembali!")

        except Exception as e:
            show_error(e)
# UPDATE BARANG ==============================================================================================================
def update_nama(barang):
    nama = input(f"Nama Produk ({barang['Nama Produk']}): ").strip()

    if not nama or nama == barang['Nama Produk']:  
        show_error("❌ Nama produk tidak boleh kosong atau sama dengan sebelumnya!")
        return  

    if confirm_update("Nama Produk", nama):  
        barang['Nama Produk'] = nama
        show_updated_item(barang)
    else:
        print("🔄 Perubahan dibatalkan.")
        input("\nTekan Enter untuk kembali...")
def update_stok_awal(barang):
    while True:
        try:
            stok_awal_input = input(f"Jumlah Stok Awal ({barang['Jumlah Stok Awal (Unit)']}): ").strip()
            stok_awal = int(stok_awal_input) if stok_awal_input else None

            if stok_awal is None or stok_awal <= 0 or stok_awal == barang['Jumlah Stok Awal (Unit)']:
                show_error("❌ Jumlah stok awal harus diisi, lebih dari 0, dan berbeda dari sebelumnya!")
                continue

            if confirm_update("Jumlah Stok Awal", stok_awal):
                barang['Jumlah Stok Awal (Unit)'] = stok_awal
                barang['Jumlah Stok Akhir (Unit)'] = stok_awal - barang['Pengeluaran (Unit)']
                barang['Nilai Stok Akhir (Rp)'] = barang['Jumlah Stok Akhir (Unit)'] * barang['Harga satuan (Rp)']
                show_updated_item(barang)
            else:
                print("🔄 Perubahan dibatalkan.")
                input("\nTekan Enter untuk kembali...")
            break  

        except ValueError:
            show_error("❌ Masukkan angka yang valid untuk stok awal!")
def update_pengeluaran(barang):
    while True:
        try:
            pengeluaran_input = input(f"Pengeluaran (Stok Akhir: {barang['Jumlah Stok Akhir (Unit)']}): ").strip()
            pengeluaran = int(pengeluaran_input) if pengeluaran_input else None

            if pengeluaran is None or pengeluaran <= 0 or pengeluaran > barang['Jumlah Stok Akhir (Unit)']:
                show_error("❌ Pengeluaran tidak boleh kosong, negatif, atau lebih besar dari stok akhir!")
                continue

            if confirm_update("Pengeluaran", pengeluaran):
                barang['Pengeluaran (Unit)'] += pengeluaran  
                barang['Jumlah Stok Akhir (Unit)'] -= pengeluaran  
                barang['Nilai Stok Akhir (Rp)'] = barang['Jumlah Stok Akhir (Unit)'] * barang['Harga satuan (Rp)']
                show_updated_item(barang)
            else:
                print("🔄 Perubahan dibatalkan.")
                input("\nTekan Enter untuk kembali...")
            break  

        except ValueError:
            show_error("❌ Masukkan angka yang valid untuk pengeluaran!")
def update_harga(barang):
    while True:
        try:
            harga_input = input(f"Harga Satuan ({barang['Harga satuan (Rp)']}): ").strip()
            harga = int(harga_input) if harga_input else None

            if harga is None or harga <= 0:
                show_error("❌ Harga satuan harus diisi dan lebih dari 0!")
                continue

            if confirm_update("Harga Satuan", harga):
                barang['Harga satuan (Rp)'] = harga
                barang['Nilai Stok Akhir (Rp)'] = barang['Jumlah Stok Akhir (Unit)'] * harga
                show_updated_item(barang)
            else:
                print("🔄 Perubahan dibatalkan.")
                input("\nTekan Enter untuk kembali...")
            break  

        except ValueError:
            show_error("❌ Masukkan angka yang valid untuk harga satuan!")
def sub_menu_update_stok():
    while True:
        clear_terminal()
        print("\n📝 Sub Menu Update Stok Barang")
        show_table_data(stokBarang)
        kode = input("\nMasukkan Kode Produk yang ingin diupdate (atau ketik 'batal' untuk kembali): ").strip().upper()
        if kode.lower() == 'batal':
            break
        
        barang = next((b for b in stokBarang if b['Kode Produk'] == kode), None)
        if not barang:
            show_error("❌ Kode Produk tidak ditemukan!")
            continue
        
        while True:
            clear_terminal()
            print(f"\nMengedit: {barang['Nama Produk']} ({barang['Kode Produk']})")
            menu_options = [
                ["1", "Nama Produk"],
                ["2", "Jumlah Stok Awal"],
                ["3", "Pengeluaran"],
                ["4", "Harga Satuan"],
                ["5", "Kembali"]
            ]
            print(tabulate(menu_options, headers=["Pilihan", "Deskripsi"], tablefmt="fancy_grid"))
            pilihan = input("Pilih data yang ingin diupdate (1-5): ").strip()
            
            if pilihan == "1":
                update_nama(barang)
            elif pilihan == "2":
                update_stok_awal(barang)
            elif pilihan == "3":
                update_pengeluaran(barang)
            elif pilihan == "4":
                update_harga(barang)
            elif pilihan == "5":
                break
            else:
                show_error("❌ Pilihan tidak valid!")
def menu_update_stok():
    while True:
        clear_terminal()
        print("\n📝 Sub Menu Update Produk:\n")
        menu_options = [
        ["1", "Update Stok Barang"],
        ["2", "Kembali ke Menu Utama"]
        ]
        print(tabulate(menu_options, headers=["Pilihan", "Deskripsi"], tablefmt="fancy_grid"))
        pilihan = input("Pilih sub-menu (1-2): ").strip()

        if pilihan == "1":
            if verify_admin():
                sub_menu_update_stok()  
        elif pilihan == "2":
            break
        else:
            show_error("❌ Pilihan tidak valid!")
# TAMBAH BARANG2 ==============================================================================================================
def tambah_stok():
    while True:
        try:
            clear_terminal()
            print("\n🆕 Sub Menu Tambah Produk:\n")
            menu_options = [
                ["1", "Tambah Produk Baru"],
                ["2", "Kembali ke Menu Utama"]
            ]
            print(tabulate(menu_options, headers=["Pilihan", "Deskripsi"], tablefmt="fancy_grid"))
            pilihan = input("\nPilih sub-menu (1-2): ").strip()

            if pilihan == "1":
                if not verify_admin():
                    continue  

                while True:  
                    try:
                        clear_terminal()
                        print("\n🆕 Tambah Produk Baru (Ketik 'q' untuk kembali ke menu)")
                        
                        # Nama Produk
                        nama = input("ℹ️ Nama Produk: ").strip()
                        if nama.lower() == "q":
                            print("\n❌ Tambah produk dibatalkan. Kembali ke sub-menu...")
                            return  
                        if not nama:
                            raise ValueError("❌ Nama Produk tidak boleh kosong!")
                        
                        # Kode Produk
                        kode = input("ℹ️ Kode Produk: ").strip().upper()
                        if kode.lower() == "Q":
                            print("\n❌ Tambah produk dibatalkan. Kembali ke sub-menu...")
                            return  
                        if not kode:
                            raise ValueError("❌ Kode Produk tidak boleh kosong!")
                        if not kode.isalnum() or kode.isalpha() or kode.isdigit():
                            raise ValueError("❌ Kode Produk harus mengandung kombinasi huruf dan angka!")
                        if any(barang['Kode Produk'] == kode for barang in stokBarang):
                            raise ValueError("❌ Kode Produk sudah ada, gunakan kode lain!")

                        # Jumlah Stok Awal
                        stok_awal = input("📊 Jumlah Stok Awal (Unit): ").strip()
                        if stok_awal.lower() == "q":
                            print("\n❌ Tambah produk dibatalkan. Kembali ke sub-menu...")
                            return  
                        if not stok_awal.isdigit() or int(stok_awal) <= 0:
                            raise ValueError("❌ Jumlah stok harus berupa angka dan lebih dari 0!")
                        stok_awal = int(stok_awal)

                        # Harga Satuan
                        harga_satuan = input("💰 Harga Satuan (Rp): ").strip()
                        if harga_satuan.lower() == "q":
                            print("\n❌ Tambah produk dibatalkan. Kembali ke sub-menu...")
                            return  
                        if not harga_satuan.isdigit() or int(harga_satuan) <= 0:
                            raise ValueError("❌ Harga satuan harus berupa angka dan lebih dari 0!")
                        harga_satuan = int(harga_satuan)

                    except ValueError as error:
                        show_error(error)
                        input("\nTekan Enter untuk mengulang dari awal...")
                        continue  # Ulang input dari awal

                    print("\n📊 Konfirmasi Produk yang Akan Ditambahkan:")
                    confirm_table = [
                        ["Nama Produk", nama],
                        ["Kode Produk", kode],
                        ["Jumlah Stok Awal", stok_awal],
                        ["Harga Satuan", harga_satuan]
                    ]
                    print(tabulate(confirm_table, tablefmt="fancy_grid"))

                    konfirmasi = input("🤔 Apakah data sudah benar? (y/n/q): ").strip().lower()
                    if konfirmasi == "q":
                        print("\n❌ Tambah produk dibatalkan. Kembali ke sub-menu...")
                        return  
                    if konfirmasi != "y":
                        print("\n❌ Tambah produk dibatalkan.")
                        input("\nTekan Enter untuk mengulang dari awal...")
                        continue  

                    stok_akhir = stok_awal
                    nilai_stok_akhir = stok_akhir * harga_satuan
                    
                    stokBarang.append({
                        'Nama Produk': nama,
                        'Kode Produk': kode,
                        'Jumlah Stok Awal (Unit)': stok_awal,
                        'Pengeluaran (Unit)': 0,
                        'Jumlah Stok Akhir (Unit)': stok_akhir,
                        'Harga satuan (Rp)': harga_satuan,
                        'Nilai Stok Akhir (Rp)': nilai_stok_akhir
                    })
                    
                    clear_terminal()
                    show_added_item(stokBarang[-1])
                    break  

            elif pilihan == "2":
                break
            else:
                show_error("❌ Pilihan tidak valid, silakan pilih kembali!")

        except Exception as e:
            show_error(f"❌ Terjadi kesalahan: {e}")
            input("\nTekan Enter untuk mengulang dari awal...")
# LIHAT BARANG ===============================================================================================================
def tampilkan_stok():
    while True:
        try:
            clear_terminal()
            print("\n👓 Sub Menu Tampilkan Stok:\n")
            menu_options = [
            ["1", "Lihat Semua Stok"],
            ["2", "Cari Stok Berdasarkan Kode Produk"],
            ["3", "Lihat Stok Berdasarkan Kode Produk (Sorted)"],
            ["4", "Lihat Stok Berdasarkan Jumlah Stok Akhir (Sorted)"],
            ["5", "Kembali ke Menu Utama"]
            ]
            print(tabulate(menu_options, headers=["Pilihan", "Deskripsi"], tablefmt="fancy_grid"))
            sub_pilihan = input("Pilih sub-menu (1-5): ")

            if sub_pilihan == "1":
                show_table()
                input("\nTekan Enter untuk kembali...")
            elif sub_pilihan == "2":
                cari_stok_kode()
            elif sub_pilihan == "3":
                show_table_sorted_by_kode()
            elif sub_pilihan == "4":
                show_table_sorted_by_stok()
            elif sub_pilihan == "5":
                clear_terminal()  
                break
            else:
                print("❌ Pilihan tidak valid, silakan pilih kembali!")
                input("\nTekan Enter untuk kembali...")
        except Exception as e:
            show_error(e)
def cari_stok_kode():
    try:
        clear_terminal()
        print("Daftar Produk yang Tersedia:")
        show_product_codes()  
        
        kode = input("\nℹ️ Masukkan Kode Produk yang ingin dicari: ").strip().upper()
        found = [barang for barang in stokBarang if barang['Kode Produk'] == kode]
        
        clear_terminal()
        if found:
            print(f"Detail Stok untuk Kode Produk: {kode}")
            headers = ["No"] + list(found[0].keys())
            table = [[1] + list(found[0].values())]  
            print(tabulate(table, headers=headers, tablefmt="double_outline"))
        else:
            print("❌ Produk dengan kode tersebut tidak ditemukan.")
        
        input("\nTekan Enter untuk kembali...")
    except Exception as e:
        show_error(e)       
#  MENU UTAMA ==============================================================================================================
def main_menu():
    while True:
        try:
            clear_terminal()
            print("\nSELAMAT DATANG DI STOK BARANG ELECTRONIC SOLUTION !")
            print("\nMenu Utama:\n")
            menu_options = [
            ["1", "🔎 Lihat stok barang"],
            ["2", "🆕 Tambah stok barang (Admin)"],
            ["3", "📝 Update stok barang (Admin)"],
            ["4", "🗑️ Hapus stok barang (Admin)"],
            ["5", "🚪 Keluar"]
            ]
            print(tabulate(menu_options, headers=["Pilihan", "Deskripsi"], tablefmt="fancy_grid"))
            choice = int(input("\nMasukkan pilihan (1-5): "))
            clear_terminal()

            if choice == 1:
                tampilkan_stok()
            elif choice == 2:
                tambah_stok()
            elif choice == 3:
                menu_update_stok()
            elif choice == 4:
                hapus_stok()
            elif choice == 5:
                print("Terima kasih sudah menggunakan sistem stok barang Electronic Solution. Sampai jumpa! ")
                input("\nTekan Enter untuk keluar...")
                break
            else:
                raise ValueError("❌ Pilihan tidak valid silahkan masukan angka 1 atau 5.")
        except Exception:
            show_error("❌ Pilihan tidak valid silahkan masukan angka 1 sampai 5.")

clear_terminal()  
main_menu()
    


 