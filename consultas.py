import mysql.connector
from mysql.connector import Error

connection = None
try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='TU_CONTRASEÑA',
        db='mi_db_1'
    )
    cursor = connection.cursor()

    print("1. Primeros 5 empleados:")
    cursor.execute("SELECT Employee_ID, Full_Name, Job_Title FROM empleados LIMIT 5")
    for fila in cursor.fetchall():
        print(fila)

    print("\n2. Total de empleados:")
    cursor.execute("SELECT COUNT(*) FROM empleados")
    print(cursor.fetchone()[0])

    print("\n3. Empleados por departamento:")
    cursor.execute("SELECT Department, COUNT(*) FROM empleados GROUP BY Department ORDER BY COUNT(*) DESC")
    for fila in cursor.fetchall():
        print(fila)

    print("\n4. Salario promedio por departamento:")
    cursor.execute("SELECT Department, ROUND(AVG(Annual_Salary), 2) FROM empleados GROUP BY Department")
    for fila in cursor.fetchall():
        print(fila)

    print("\n5. Insertar un empleado nuevo:")
    cursor.execute("""INSERT INTO empleados (Employee_ID, Full_Name, Job_Title, Department,
        Business_Unit, Gender, Ethnicity, Age, Annual_Salary, Bonus)
        VALUES ('E99999', 'Empleado de Prueba', 'Analyst', 'IT', 'Corporate',
        'Female', 'Latino', 30, 50000, 0)""")
    connection.commit()
    print("Empleado E99999 insertado.")

    print("\n6. Modificar el salario del empleado nuevo:")
    cursor.execute("UPDATE empleados SET Annual_Salary = 60000 WHERE Employee_ID = 'E99999'")
    connection.commit()
    cursor.execute("SELECT Employee_ID, Full_Name, Annual_Salary FROM empleados WHERE Employee_ID = 'E99999'")
    print(cursor.fetchone())

    print("\n7. Borrar el empleado nuevo:")
    cursor.execute("DELETE FROM empleados WHERE Employee_ID = 'E99999'")
    connection.commit()
    cursor.execute("SELECT COUNT(*) FROM empleados")
    print("Total de empleados ahora:", cursor.fetchone()[0])

except Error as ex:
    print("Error en la conexion: {}".format(ex))
finally:
    if connection is not None and connection.is_connected():
        connection.close()
        print("\nConexion cerrada.")