from db import get_connection
try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call consulta_alumnos()')
        resultset=cursor.fetchall()
        for row in resultset:
            print(row)
    connection.close()
except Exception as ex:
    print('ERROR')
    
""" try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call agrega_alumno(%s,%s,%s)',('jazmin','rios','rios@gmail.com'))
        
    connection.commit()
    connection.close()
except Exception as ex:
    print('ERROR') """