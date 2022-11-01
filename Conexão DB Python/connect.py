import pymysql.cursors

connection = pymysql.connect(host='localhost', user= 'root', password='123456', database='database')
print("Database connection made!") #Estabelecendo conexão com o banco

conn = connection.cursor() #Criando Cursor do sql

conn.execute("SELECT * FROM database") #Aplicando comando no Mysql

result = conn.fetchone() #Pegando o primeiro resultado encontrado
# result = conn.fetchall() #Pegando todos os resultados encontrados


print(result)






