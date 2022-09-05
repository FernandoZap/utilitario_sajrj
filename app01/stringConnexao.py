def strSqlServer():
     server = ''
     database = ''
     username = ''
     password = '*'
     return 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password +';TrustServerCertificate=Yes'

def strMySql():
     lista1=['user','password','host','database']
     lista2=['','','','']
     return dict(zip(lista1,lista2))
