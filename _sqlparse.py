import sqlparse

# https://pypi.org/project/sqlparse/
raw = """select CIF, Sede from Club where Nombre like '%u%'; select * form foo"""
statements = sqlparse.split(raw)  # Devuelve una lista con las consultas en una lista
print('----\n', statements)
first = statements[0]  # Coge la primera consulta

# Imprime la consulta en una linea entera seguida
print('\n', first)
# select CIF, Sede from Club where Nombre like '%u%';

# Imprime la consulta por trozos y pone en mayúsculas las palabras clave
print('\n', sqlparse.format(first, reindent=True, keyword_case='upper'))
# SELECT CIF,
#       Sede
# FROM Club
# WHERE Nombre LIKE '%u%';

parsed1 = sqlparse.parse(first)  # Objeto
print('--PARSE--\n', parsed1)
print(type(parsed1))  # class 'tuple'

parsed2 = sqlparse.parse(first)[0]  # Consulta
print('\n', parsed2)  # Devuelve la consulta tal cual
print(type(parsed2))  # class sqlparse.sql.Statement

# Tokens
print('\n--TOKENS--')
print('\n', parsed2.tokens)  # Devuelve una lista de objetos sqlparse.sql.Token
print(type(parsed2.tokens))  # class 'list'
print('\n', type(parsed2.tokens[0]))  # <class 'sqlparse.sql.Token'>

for elem in parsed2.tokens:
    print(elem)

# Sublists
print('\n--SUBLISTS--')
sublists = list(parsed2.get_sublists())
print(sublists)
sublists2 = parsed2.get_sublists()
print(type(sublists2))  # class 'generator'

for elem in sublists:
    print(elem)
