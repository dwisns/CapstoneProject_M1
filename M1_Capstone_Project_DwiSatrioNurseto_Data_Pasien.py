# DWI SATRIO NURSETO
# Nama Rumah Sakit = 'Rumah Sakit Purwadhika BSD'
# Keys dictionary == 5 :
        # 'No. ID Pasien'
        # 'Nama Pasien'
        # 'Jenis Kelamin Pasien'
        # 'Berat Badan Pasien'  (BB)
        # 'Tinggi Badan Pasien' (TB)

# Menu di Welcome page : 
        # 1. Menampilkan data pasien    ✅
        # 2. Menambah data pasien       ✅
        # 3. Mengubah data pasien       ✅
        # 4. Mengetahui BMI pasien      ✅
        # 5. Menghapus data pasien      ✅
        # 6. Exit                       ✅

# KLASIFIKASI BMI BERDASARKAN WORLD HEALTH ORGANIZATION
# BMI < 18.50: underweight
# BMI >= 18.50 or BMI <= 24.90: Normal Weight
# BMI >= 25.00 or BMI <= 29.90: Overweight
# BMI >= 30.00 or BMI <= 34.90: Obesity class I
# BMI >= 35.00 or BMI <= 39.90: Obesity class II
# BMI >= 40.00 Obesity class III

# Aktifkan Data Pasien Untuk Test Menu [1,2,3,4,6]
pasien = [
{'ID' : 210501, 'Nama' : 'Romy', 'Gender' : 'L', 'BB' : 70, 'TB' : 174}, 
{'ID' : 210502, 'Nama' : 'Iva', 'Gender' : 'P', 'BB' : 58, 'TB' : 164},
{'ID' : 210503, 'Nama' : 'Ani', 'Gender' : 'P', 'BB' : 53, 'TB' : 164},
{'ID' : 210504, 'Nama' : 'Aaron', 'Gender' : 'L', 'BB' : 110, 'TB' : 170},
{'ID' : 210505, 'Nama' : 'Beami', 'Gender' : 'P', 'BB' : 53, 'TB' : 168},
]

# Aktifkan Data Pasien Untuk Test Menu [5]
# pasien = [
# {'ID' : 210501, 'Nama' : 'Romy', 'Gender' : 'L', 'BB' : 70, 'TB' : 174}
# ]



def welcome_page():
    return '\n🏥🚑🚑🚑🚑🚑🚑🚑 Data Rumah Sakit Purwadhika BSD 🚑🚑🚑🚑🚑🚑🚑🏥'

def welcome_menu():
    menu = '''
        1. Menampilkan data pasien
        2. Menambah data pasien
        3. Mengubah data pasien
        4. Mengetahui BMI pasien
        5. Menghapus data pasien
        6. Exit'''
    return menu

def banner_dp():
    print('-----------------------------------------------------')
    print('\n\tData Pasien Rumah Sakit Purwadhika BSD\t\n')
    print('-----------------------------------------------------')

def data_pasien():  # 0 start
    for j,i in enumerate(pasien):
        print(f"{j+1}. ID: {i['ID']}, Nama: {i['Nama']}, Gender: {i['Gender']}, BB: {i['BB']} kg, TB: {i['TB']} cm")

def banner_ub():
    print('-----------------------------------------------------')

def menampilkan_dp():       # 1.0
    print('\n~~~~~~~~~~ Menu Menampilkan Data Pasien ~~~~~~~~~~\n')
    print('\t1. Menampilkan seluruh data pasien')
    print('\t2. Menampilkan data pasien tertentu')
    print('\t3. Kembali ke Menu Utama ↩')

def menambah_dp():          # 2.0
    print('\n~~~~~~~~~~ Menu Menambahkan Data Pasien ~~~~~~~~~~\n')
    print('\t1. Menambah data pasien')
    print('\t2. Kembali ke Menu Utama ↩')

def mengubah_dp():          # 3.0
    print('\n~~~~~~~~~~ Menu Mengubah Data Pasien ~~~~~~~~~~\n')
    print('\t1. Ubah data pasien')
    print('\t2. Kembali ke Menu Utama ↩')

def bmi_dp():               # 4.0
    print('\n~~~~~~~~~~ Menu Mengetahui BMI dari Data Pasien ~~~~~~~~~~\n')
    print('\t1. BMI kalkulator')
    print('\t2. Kembali ke Menu Utama ↩')

def menghapus_dp():          # 5.0
    print('\n~~~~~~~~~~ Menu Menghapus Data Pasien ~~~~~~~~~~\n')
    print('\t1. Menghapus data pasien')
    print('\t2. Kembali ke Menu Utama ↩')

def PERINGATAN():
    print('\n❌ Mohon masukkan angka yang benar! ❌\n')


def choose_menu():
    while 1:
        print(welcome_page())
        print(welcome_menu())
        choose_menu = input('\n\tSilahkan Pilih Menu [1-6]: ')

        # MENU [Menampilkan data pasien]
        # MEMASUKI MENU 1
        if choose_menu == '1':
            while 1:
                menampilkan_dp()
                choose_menu1 = input('\n\tSilahkan Pilih Menu [1-3]: ')

                # MEMASUKI SUB-MENU 1.1
                # PENGECEKAN KESEDIAAN DP
                if choose_menu1 == '1':
                    if len(pasien) != 0:
                        print('\n')
                        banner_dp()
                        data_pasien()
                        banner_ub()
                        print('\n')
                    elif len(pasien) == 0:
                        print('\n\t❌ Data Pasien Kosong ❌\n')

                # MEMASUKI SUB-MENU 1.2
                # PENGECEKAN DP PILIHAN
                elif choose_menu1 == '2':
                    if len(pasien) != 0:
                        id_pasien = int(input('Masukkan ID pasien: '))
                        print(f'Pasien dengan ID: {id_pasien} ')
                   
                        list_id = []
                        for i in range(len(pasien)):
                            list_id.append(pasien[i]['ID'])

                        if id_pasien in list_id:
                            print(f"{list_id.index(id_pasien) + 1}. ID: {id_pasien}, Nama: {pasien[list_id.index(id_pasien)]['Nama']}, Gender: {pasien[list_id.index(id_pasien)]['Gender']} , BB: {pasien[list_id.index(id_pasien)]['BB']} kg, TB: {pasien[list_id.index(id_pasien)]['TB']} cm\n")
                        else:               
                            print(f'❌ data pasien dengan ID {id_pasien} tidak tersedia ❌\n')
                            

                    elif len(pasien) == 0:
                        print('\n\t❌ Data Pasien Kosong ❌\n')

                # KELUAR DARI SUB-MENU 1
                elif choose_menu1 == '3':
                    break

                # PERINGATAN
                else:
                    PERINGATAN()
                    continue
                    
        # MENU [Menambah data pasien]
        # MEMASUKI MENU 2
        elif choose_menu == '2':            
            while 1:

                menambah_dp()
                choose_menu2 = input('\n\tSilahkan Pilih Menu [1-2]: ')

                # MEMASUKI SUB-MENU 2.1
                if choose_menu2 == '1':
                    dict_pasien_baru = {}

                    while 1:
                        dict_pasien_baru['ID'] = int(input('Masukkan ID pasien (6 digit angka): '))
                        jadiinstring = str(dict_pasien_baru['ID'])
                        if len(jadiinstring) != 6:
                            print('😡 ID yang anda input tidak 6 digit! 😡')
                        elif len(jadiinstring) == 6:                        
                            list_id = []
                            for i in range(len(pasien)):
                                list_id.append(pasien[i]['ID'])
                            

                            
                            # KONDISI PENGECEKAN DUPLIKASI ID
                            if dict_pasien_baru['ID'] not in list_id:
                                dict_pasien_baru['Nama'] = (input('Masukkan Nama pasien: ')).capitalize()

                                # LOOPING PENULISAN GENDER
                                while 1:
                                    dict_pasien_baru['Gender'] = (input('Masukkan Gender pasien (L/P): ')).capitalize()
                                    if dict_pasien_baru['Gender'] == 'L' or dict_pasien_baru['Gender'] == 'P':
                                        dict_pasien_baru['BB'] = int(input('Masukkan Berat Badan pasien dalam kg: '))
                                        dict_pasien_baru['TB'] = int(input('Masukkan Tinggi Badan pasien dalam cm: '))
                                        print(f'Adapun data pasien seperti berikut:\n{dict_pasien_baru}\n')
                                        break
                                                                            
                                    elif dict_pasien_baru['Gender'] != 'L' or dict_pasien_baru['Gender'] != 'P':                                  
                                        print('😤 ♂ Masukkan Laki-Laki (L)  atau ♀ Perempuan (P) 😤')
                                        continue
                                
                                # KONFIRMASI PENAMBAHAN DP
                                while 1:
                                    tambah = input('Tekan Y untuk menambahkan dan N untuk membatalkan data: ').capitalize()
                                    if tambah == 'Y':
                                        pasien.append(dict_pasien_baru)
                                        print('\n✅✅✅ Data pasien berhasil ditambahkan ✅✅✅\n')
                                        break
                                    elif tambah == 'N':
                                        dict_pasien_baru.clear()
                                        print('\n 🛑🛑 data pasien tidak jadi ditambahkan 🛑🛑 \n')
                                        break
                                    else:
                                        print('\n😡 Masukkan Y/N! 😡 \n')
                        
                            # JIKA ID DUPLIKAT
                            elif dict_pasien_baru['ID'] in list_id:
                                print('\n🙏 Maaf ID yang anda masukkan sudah dipakai 🙏')
                                continue
                            break
                       

                # KELUAR DARI SUB-MENU 2
                elif choose_menu2 == '2':
                    break

                # PERINGATAN
                else:
                    print('\n❌ Masukkan angka yang benar! ❌\n')
                    continue
                    
        # MENU [Mengubah data pasien]
        # MEMASUKI MENU 3
        elif choose_menu == '3':
            while 1:
                mengubah_dp()
                choose_menu3 = input('\n\tSilahkan Pilih Menu [1-2]: ')

                # MEMASUKI SUB-MENU 3.1
                if choose_menu3 == '1':
                    if len(pasien) != 0:
                        banner_dp()
                        data_pasien()
                        banner_ub()
                        id_pasien = int(input('Masukkan ID pasien: '))
                        print(f'Pasien dengan ID: {id_pasien} ')
                   
                        list_id = []
                        for i in range(len(pasien)):
                            list_id.append(pasien[i]['ID'])

                        if id_pasien in list_id:
                            print(f"{list_id.index(id_pasien) + 1}. ID: {id_pasien}, Nama: {pasien[list_id.index(id_pasien)]['Nama']}, Gender: {pasien[list_id.index(id_pasien)]['Gender']} , BB: {pasien[list_id.index(id_pasien)]['BB']} kg, TB: {pasien[list_id.index(id_pasien)]['TB']} cm\n")
                            while 1:
                                mngbh = input('Tekan Y jika ingin mengubah dan N untuk membatalkan: ').capitalize()
                                if mngbh == 'Y':
                                    list_id = []
                                    for i in range(len(pasien)):
                                        list_id.append(pasien[i]['ID'])
                                    print('... ... ... Perubahan data akan dimulai ... ... ...')
                                    yg_diganti = pasien[list_id.index(id_pasien)]
                                    while 1:
                                        keyganti = str(input('Masukkan data yang ingin diganti (ID/Nama/Gender/Berat Badan/Tinggi Badan): ')).upper()
                                        
                                        # MENGUBAH ID
                                        if keyganti == 'ID':
                                            idbaru = int(input('Masukkan ID baru: '))
                                            while 1:
                                                if idbaru not in list_id:                                                    
                                                    jadikah = str(input('Jadi diupdate (Y/N)?')).capitalize()
                                                    if jadikah == 'Y':
                                                        yg_diganti['ID'] = idbaru
                                                        banner_dp()
                                                        data_pasien()
                                                        print('\n✅ Data ID pasien berhasil diganti ✅')
                                                        break
                                                    elif jadikah == 'N':
                                                        print('** ID tidak jadi dirubah **')
                                                        break
                                                    else:
                                                        print('\n😡 Cuma menerima Y/N! 😡 \n')
                                                    
                                                elif idbaru in list_id:
                                                    print('\n 🛑ID pasien tersebut sudah dipakai 🛑\n')
                                                    break
                                            break

                                        # MENGUBAH NAMA
                                        elif keyganti == 'NAMA':
                                            namabaru = input('Masukkan Nama baru: ').capitalize()                                            
                                            while 1:                                                                                                    
                                                jadikah = str(input('Jadi diupdate (Y/N)?')).capitalize()
                                                if jadikah == 'Y':
                                                    yg_diganti['Nama'] = namabaru
                                                    banner_dp()
                                                    data_pasien()
                                                    print('\n✅ Data Nama pasien berhasil diganti ✅')
                                                    break
                                                elif jadikah == 'N':
                                                    print('** Nama tidak jadi dirubah **')
                                                    break
                                                else:
                                                    print('\n😡 Cuma menerima Y/N! 😡 \n')
                                            break


                                        # MENGUBAH GENDER
                                        elif keyganti == 'GENDER':                                            
                                            while 1:
                                                genderbaru = input('Masukkan Gender baru: ').capitalize()
                                                if genderbaru == 'L' or genderbaru == 'P':
                                                    while 1:
                                                        jadikah = str(input('Jadi diupdate (Y/N)?')).capitalize()
                                                        if jadikah == 'Y':
                                                            yg_diganti['Gender'] = genderbaru
                                                            banner_dp()
                                                            data_pasien()
                                                            print('\n✅ Data Gender pasien berhasil diganti ✅')
                                                            break
                                                        elif jadikah == 'N':
                                                            print('** Gender tidak jadi dirubah **')
                                                            break
                                                        else:
                                                            print('\n😡 Cuma menerima Y/N! 😡 \n')
                                                    break
                                                else:
                                                    print('😤 ♂ Masukkan Laki-Laki (L)  atau ♀ Perempuan (P) 😤')
                                            break

                                        # MENGUBAH BB
                                        elif keyganti == 'BERAT BADAN':
                                            bbbaru = int(input('Masukkan Berat Badan baru: '))
                                            while 1:
                                                jadikah = str(input('Jadi diupdate (Y/N)?')).capitalize()
                                                if jadikah == 'Y':
                                                    yg_diganti['BB'] = bbbaru
                                                    banner_dp()
                                                    data_pasien()
                                                    print('\n✅ Data Berat Badan pasien berhasil diganti ✅')
                                                    break
                                                elif jadikah == 'N':
                                                    print('** Berat Badan tidak jadi dirubah **')
                                                    break
                                                else:
                                                    print('\n😡 Cuma menerima Y/N! 😡 \n')
                                            break

                                        # MENGUBAH TB
                                        elif keyganti == 'TINGGI BADAN':
                                            tbbaru = int(input('Masukkan Tinggi Badan baru: '))
                                            while 1:
                                                jadikah = str(input('Jadi diupdate (Y/N)?')).capitalize()
                                                if jadikah == 'Y':
                                                    yg_diganti['TB'] = tbbaru
                                                    banner_dp()
                                                    data_pasien()
                                                    print('\n✅ Data Tinggi Badan pasien berhasil diganti ✅')
                                                    break
                                                elif jadikah == 'N':
                                                    print('** Tinggi Badan tidak jadi dirubah **')
                                                    break
                                                else:
                                                    print('\n😡 Cuma menerima Y/N! 😡 \n')
                                            break


                                        else:
                                            print('\n😡 Masukkan (ID/Nama/Gender/Berat Badan/Tinggi Badan)! 😡 \n')
                                            continue                          
                                        

                                # TIDAK JADI MENGUBAH
                                # KEMBALI KE SUB-MENU 3
                                elif mngbh == 'N':
                                    print('\noke berarti gajadi ya\n')
                                    break

                                # PERINGATAN SALAH DAN MELOOPING
                                else:
                                    print('\n😡 Masukkan Y/N jangan yang lain! 😡 \n')
                                    continue
                                break

                        # LOOPING UNTUK PRIMARY KEY YANG TIDAK TERSEDIA (!=)
                        else:               
                            print(f'❌ data pasien dengan ID {id_pasien} tidak tersedia ❌\n')

                    # JIKA DATA PASIEN KOSONG
                    elif len(pasien) == 0:
                        print('\n\t❌ Data Pasien Kosong ❌\n')

                # KELUAR DARI SUB-MENU 3
                elif choose_menu3 == '2':
                    break
                else:
                    print('\n...Masukkan angka yang benar...\n')
                    continue

        # MENU [Mengetahui BMI dari data pasien]
        # MEMASUKI MENU 4
        elif choose_menu == '4':
            # print('4')
            while 1:
                bmi_dp()
                choose_menu4 = input('\n\tSilahkan Pilih Menu [1-2]: ')

                # MEMASUKI SUB-MENU 4.1
                if choose_menu4 == '1':
                    if len(pasien) != 0:
                        banner_dp()
                        data_pasien()
                        banner_ub()
                        while 1:
                            bmiid = int(input('\nSilahkan masukkan ID pasien yang ingin dihitung: '))
                            list_id2 = []
                            for i in range(len(pasien)):
                                list_id2.append(pasien[i]['ID'])                            
                            # print('... ... ... Perhitungan BMI akan dimulai ... ... ...')
                            # # namapasien = pasien[list_id2.index(bmiid)]['Nama']

                            if bmiid in list_id2:
                                print('... ... ... Perhitungan BMI akan dimulai ... ... ...')
                                while 1:
                                    nanya = input('Tekan Y untuk menghitung dan N untuk membatalkan: ').capitalize()
                                    if nanya == 'Y':  
                                        # Menghitung BMI
                                        namapasien = pasien[list_id2.index(bmiid)]['Nama']
                                        indexingbmi = pasien[list_id2.index(bmiid)]
                                        beratbadan = indexingbmi['BB']
                                        tinggibadan = indexingbmi['TB']
                                        BMI = (beratbadan/((tinggibadan/100)**2))
                                        print('-----------------------------------------------------')
                                        print('\nKLASIFIKASI BMI BERDASARKAN WORLD HEALTH ORGANIZATION\n')
                                        print('-----------------------------------------------------')
                                        print(f'Pasien dengan;\nNama: {namapasien}\nBerat: {beratbadan} kg\nTinggi: {tinggibadan} cm ')
                                        print(f'BMI pasien: {BMI:.2f} ')
                                        # Status BMI
                                        if BMI < 18.50:
                                            print('Dengan status: UNDERWEIGHT')
                                        elif BMI >= 18.50 and BMI <= 24.90:
                                            print('Dengan status: NORMAL WEIGHT')
                                        elif BMI >= 25.00 and BMI <= 29.90:
                                            print('Dengan status: OVERWEIGHT')
                                        elif BMI >= 30.00 and BMI <= 34.90:
                                            print('Dengan status: OBESITY CLASS I')
                                        elif BMI >= 35.00 and BMI <= 39.90:
                                            print('Dengan status: OBESITY CLASS II')
                                        else:
                                            print('Dengan status: OBESITY CLASS III')
                                        break
                                    elif nanya == 'N':
                                        break
                                    else:
                                        print('😡 Masukkan Y/N jangan yang lain! 😡')
                                break  
                            else:
                                print(f'\n❌ Data Pasien dengan ID {bmiid} tidak tersedia!\n')
                                break
                    elif len(pasien) == 0:
                        print('\n\t❌ Data Pasien Kosong ❌\n')


                # KELUAR DARI SUB-MENU 4
                elif choose_menu4 == '2':
                    break

                else:
                    print('\nMasukkan angka yang benar!\n')




        # MENU [Menghapus data pasien]
        # MEMASUKI MENU 5
        elif choose_menu == '5':        
            while 1:
                menghapus_dp()
                choose_menu5 = input('\n\tSilahkan Pilih Menu [1-2]: ')

                # MEMASUKI SUB-MENU 5.1
                if choose_menu5 == '1':
                    if len(pasien) != 0:
                        banner_dp()
                        data_pasien()
                        banner_ub()
                        while 1:
                            confirm = int(input('\nSilahkan masukkan ID pasien yang ingin dihapus: '))
                            list_id2 = []
                            for i in range(len(pasien)):
                                list_id2.append(pasien[i]['ID'])          
                            if confirm in list_id2:
                                kurang = input('Tekan Y untuk menghapus dan N untuk membatalkan: ').capitalize()
                                if kurang == 'Y':  
                                    del pasien[list_id2.index(confirm)]
                                    banner_dp()
                                    data_pasien()
                                    print(f'Data dengan ID {confirm} berhasil dihapus')
                                    break
                                elif kurang == 'N':
                                    print('Data tidak jadi dihapus...\n')
                                    break
                                else:
                                    print('Masukkan Y/N!')
                            else:
                                print(f'\nID {confirm} tidak tersedia!\n')
                                break
                    elif len(pasien) == 0:
                        print('\n\t❌ Data Pasien Kosong ❌\n')
                        

                # KELUAR DARI SUB-MENU 5
                elif choose_menu5 == '2':
                    break

                else:
                    print('\nMasukkan angka yang benar!\n')

        # MENU [EXIT]
        # MEMBERHENTIKAN APLIKASI
        elif choose_menu == '6':
            print('\n🚑💨\tTERIMA KASIH SEMOGA LEKAS SEMBUH\t🚑💨\n')
            break
        

        # PERINGATAN INPUT SELAIN NOMOR MENU
        else:
            PERINGATAN() 

# RUN TO START PROGRAM
choose_menu()
