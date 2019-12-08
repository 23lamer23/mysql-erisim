import mysql.connector
host = input("bağlanacağınız mysql host adresini giriniz:")
user = input("bağlanacağınız user adını giriniz: ")
pswd = input("kullanıcı parolasını giriniz: ")




def Conn(host, user , pswd):
    while True:    
        try:
            connect = mysql.connector.connect(host = host, 
                                              user = user, 
                                              password = pswd,
                                              auth_plugin = "mysql_native_password",
            )
        except mysql.connector.errors as err:
            print("bağlantı hatası : ", err)
        finally:
            if(connect.is_connected()):
                cursor = connect.cursor()
                islem = input("lütfen yapmak istediğiniz işlemi seçiniz\n***********\n1- Database oluşturma\n2-varolan bir database'i kullanma\n3- tabloya veri ekleme\n4- çıkış\n*******\n =>")
                if(islem=="1"):
                    dbadi = input("\ndatabase inize bir isim veriniz:")
                    str2 = "create database "+dbadi
                    cursor.execute(str2)
                elif(islem == "2"):
                    dbadi = input("\nbağlanmak istediğiniz db adini yaziniz: ")
                    str1 = "use "+dbadi
                    cursor.execute(str1) 
                    cursor.execute("show tables")
                    print(cursor.fetchall())
                    tablosec = input("\nmevcut tablolar bunlardır lütfen birini yazınız:")
                    str3 = "select * from "+tablosec
                    cursor.execute(str3)
                    print(cursor.fetchall())
                elif(islem =="3"):
                    dbadi = input("\nbağlanmak istediğiniz db adini yaziniz: ")
                    cursor.execute("use "+ dbadi) 
                    cursor.execute("show tables")
                    print(cursor.fetchall())
                    tablosec = input("\nmevcut tablolar bunlardır lütfen birini yazınız:")    
                    cursor.execute("select * from "+ tablosec)
                    table1 = cursor.fetchall()
                    print("\ntablodaki kayıtlı kişi sayısı:",len(table1))
                    tablodizi = []
                    k = 0
                    value = ""
                    while k<len(table1[0]):
                        print("\n ekleyecek olduğunuz",(k+1),".degeri giriniz: ")
                        temp= input("=>")
                        tablodizi.append(temp)
                        
                        if k ==0:
                            value = value+"'"+tablodizi[k]+"'"
                        else:    
                            value = value+", "+"'"+tablodizi[k]+"'"
                        k+=1    
                    cursor.execute("insert into "+tablosec+" values("+value+")")
                    cursor.execute("select * from "+tablosec)
                    print(cursor.fetchall())
                    print("\ntablonun son hali bu şekildedir.")
                    connect.commit()
                    connect.close()
                    break
                else:
                    
                     break
                    
              
Conn(host, user, pswd, db)
print("bye :D")

            
 

