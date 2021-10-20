from sql_metadata import Parser
import sql_metadata

# https://github.com/macbre/sql-metadata


select_query = """select CIF, Sede from Club where Nombre like '%u%'; select * form foo"""
create_query = """create table table1(id integer not null)"""

select_parser = Parser(select_query)
create_parser = Parser(create_query)

print('\n', type(select_parser))  # Class Parser
print(select_parser.query_type)  # QueryType.SELECT
print(create_parser.query_type)  # QueryType.CREATE

print(create_parser.query)  # Imprime la consulta

# Imprime las columnas a las que hace referencia
print("\n-> Columnas")
print(select_parser.columns)  # ['CIF', 'Sede', 'Nombre']
print(select_parser.columns_dict)  # {'select': ['CIF', 'Sede'], 'where': ['Nombre']}
print(create_parser.columns)  # ['id]
print(create_parser.columns_dict)  # None

# Imprime las tablas a las que hace referencia
print("\n-> Tablas")
print(select_parser.tables)  # ['Club']
print(create_parser.tables)  # ['table1']

# Generalización de consultas y extracción de comentarios
select_comment_query = "SELECT /* Test */ foo FROM bar WHERE id in (1, 2, 56)"
select_comment_parser = Parser(select_comment_query)

# Generalizar consulta (también quita comentarios)
print('\n', select_comment_parser.generalize)

# Solamente elimina comentarios
print(select_comment_parser.without_comments)

# Imprime solo los comentarios
print(select_comment_parser.comments)
