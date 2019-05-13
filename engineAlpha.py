import pymysql
import time

connect_bank = pymysql.connect("remotemysql.com","TfqE2Q1NdP","5zRoj4aeYe","TfqE2Q1NdP")
connect_toko = pymysql.connect("remotemysql.com","AL4OPup64X","dY2yRtrg8D","AL4OPup64X")

cursor_toko = connect_toko.cursor()
cursor_bank = connect_bank.cursor()

def engineToko():

    print("PENGECEKAN DATA TOKO SEDANG BERLANGSUNG")

    select_data = "SELECT id_invoice FROM tb_integrasi WHERE id_invoice NOT IN(SELECT id_invoice FROM tb_invoice)"
    cursor_toko.execute(select_data)
    hasil_select_data = cursor_toko.fetchall()
    connect_toko.commit()

    for hasil in hasil_select_data:
        id_invoice = int(hasil[0])
        print(id_invoice)
        delete = "delete from tb_integrasi where id_invoice=%s" % (id_invoice)
        cursor_toko.execute(delete)
        cursor_bank.execute(delete)
        connect_toko.commit()
        connect_bank.commit()

        delete_bank = "delete from tb_invoice where id_invoice=%s" % (id_invoice)
        cursor_bank.execute(delete_bank)
        connect_bank.commit()
        print("TERDAPAT PENGHAPUSAN DATA pada db_bank.tb_invoice pada id_invoice = %s" % id_invoice)

    select_transaksi = "SELECT * FROM tb_invoice"
    cursor_toko.execute(select_transaksi)
    data_toko = cursor_toko.fetchall()
    connect_toko.commit()

    for data in data_toko:
        id_invoice = int(data[0])
        total_transaksi = int(data[1])
        status = data[2]
        select = "SELECT * FROM tb_integrasi WHERE id_invoice = %s" % (id_invoice)
        cursor_toko.execute(select)
        data_integrasi_toko = cursor_toko.fetchone()
        jumlah = cursor_toko.rowcount
        connect_toko.commit()
        if jumlah == 0:
            insert = "INSERT INTO tb_integrasi(id_invoice, total_transaksi, status) values(%s,%s,%s)" % (id_invoice, total_transaksi, status)
            cursor_toko.execute(insert)
            cursor_bank.execute(insert)
            connect_toko.commit()
            connect_bank.commit()

            insert_bank = "INSERT INTO tb_invoice(id_invoice, total_transaksi, status) values(%s,%s,%s)" % (id_invoice, total_transaksi, status)
            cursor_bank.execute(insert_bank)
            connect_bank.commit()
            print("TERDAPAT PENAMBAHAN DATA PADA db_bank.tb_invoice. Pada id_invoice = %s, total_transaksi = %s, status = %s" % (id_invoice, total_transaksi, status))

        else:
            id_invoice = data_integrasi_toko[0]
            status = data_integrasi_toko[2]

            if data[1] != data_integrasi_toko[1]:
                update_toko = "UPDATE tb_integrasi SET total_transaksi = %s WHERE id_invoice= %s" % (data[1], id_invoice)
                cursor_toko.execute(update_toko)
                cursor_bank.execute(update_toko)
                connect_toko.commit()
                connect_bank.commit()

                update_bank = "UPDATE tb_invoice SET total_transaksi = %s WHERE id_invoice = %s" % (data[1], id_invoice)
                cursor_bank.execute(update_bank)
                connect_bank.commit()
                print("TERDAPAT PERUBAHAN DATA pada id_invoice = %s" % data[0])


def engineBank():
    select_data = "SELECT id_invoice FROM tb_integrasi WHERE id_invoice NOT IN(SELECT id_invoice FROM tb_invoice)"
    cursor_bank.execute(select_data)
    hasil_select_data = cursor_bank.fetchall()
    connect_bank.commit()

    select_bank = "SELECT * FROM tb_invoice"
    cursor_bank.execute(select_bank)
    data_bank = cursor_bank.fetchall()
    connect_bank.commit()

    for data in data_bank:
        id_invoice = int(data[0])
        total_transaksi = int(data[1])
        status = data[2]
        select = "SELECT * FROM tb_integrasi WHERE id_invoice = %s" % (id_invoice)
        cursor_bank.execute(select)
        data_integrasi_bank = cursor_bank.fetchone()
        jumlah = cursor_bank.rowcount
        connect_bank.commit()

        id_invoice = data_integrasi_bank[0]
        status = data_integrasi_bank[2]

        if data[2] != data_integrasi_bank[2]:
            update_integrasi = "UPDATE tb_integrasi SET status = %s WHERE id_invoice= %s" % (data[2], id_invoice)
            cursor_toko.execute(update_integrasi)
            cursor_bank.execute(update_integrasi)
            connect_toko.commit()
            connect_bank.commit()

            update_toko = "UPDATE tb_invoice SET status = %s WHERE id_invoice = %s" % (data[2], id_invoice)
            cursor_toko.execute(update_toko)
            connect_toko.commit()
            print("TERDAPAT PERUBAHAN STATUS pada id_invoice = %s" % data[0])

while(1):
    engineBank()
    engineToko()
    time.sleep(5)
