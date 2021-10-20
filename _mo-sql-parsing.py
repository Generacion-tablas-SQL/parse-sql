#pip install mo-sql-parsing

from mo_sql_parsing import parse
from mo_sql_parsing import format
import json

# La función json.dumps () convierte un objeto Python en una cadena json.
# Parsea las dos sentencias y las convierte a json
print(json.dumps(parse("select count(1) from jobs")))
print(json.dumps(parse("select a as hello, b as world from jobs")))

print('\n----')
# Pruebas de diferentes tipos de sentencias
sentencia_select = "SELECT * from XYZZY, ABC"
sentencia_select2 = "SELECT * FROM dual WHERE a>b ORDER BY a+b"
parse_select = parse(sentencia_select)
parse_select2 = parse(sentencia_select2)
print(parse_select)
print(parse_select2)
sentencia_AND = "SELECT a FROM dual WHERE a in ('r', 'g', 'b') AND b in (10, 11, 12)"
print("AND:\t", parse(sentencia_AND))
sentencia_GROUPBY = "select a, count(1) as b from mytable group by a"
print("GROUP BY:\t", parse(sentencia_GROUPBY))
sentencia_min_max = "SELECT *, min(f1,f2), max(f1,f2) FROM test1"
print("MIN, MAX:\t", parse(sentencia_min_max))
s_join = "SELECT * FROM aa CROSS JOIN bb WHERE b"
print("CROSS JOIN:\t", parse(s_join))
join = "SELECT * FROM aa JOIN bb ON aa.NIF = bb.NIF WHERE b"
print("JOIN:\t", parse(join))
join = "SELECT NIF as documento FROM persona aa JOIN bb ON aa.NIF = bb.NIF WHERE b"
print("JOIN:\t", parse(join))

# Pruebas de extracción de datos
print('\n----')
print(type(parse_select2))  # dict
print(parse_select2)
print("FROM\t", parse_select2['from'])
print("WHERE\t", parse_select2['where'])
print("ORDERBY\t", parse_select2['orderby'])


# Prueba de creacion de tablas
print('\n----')
sentencia_tablas = "CREATE TABLE doggo_info ( ID int, Name varchar(50), Color varchar(50))"
print(parse(sentencia_tablas))
sentencia_tablas2 = "CREATE TABLE puppies AS SELECT * FROM doggo_info WHERE Age < 4"
print(parse(sentencia_tablas2))
sentencia_tablas3 = "CREATE TABLE doggo_info ( ID int primary key check (ID > 10), Name varchar(50) not null unique, " \
                    "Color varchar(50) references colores(nombre))"
print(parse(sentencia_tablas3))
sentencia_tablas4 = """CREATE TABLE Persona (
Id INTEGER CHECK (Id > 50) ,
  Nombre VARCHAR(30) ,
  CONSTRAINT NombreLargo CHECK (LENGTH(Nombre) > 5)
);"""
print(parse(sentencia_tablas4))


# funcion format()
# Transforma la cadena json a formato SQL
print('\n----')
expected_json = {'select': '*', 'from': ['XYZZY', 'ABC']}
print(format(expected_json))

options = {'check': {'gt': ['Id', 50]}}
print(format(options))
