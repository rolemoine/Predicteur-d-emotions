import mysql.connector
import pymysql
import pandas as pd
import sys

#connexion au bases de données
db = mysql.connector.connect(
  host = "localhost",
  #chacun met son id et son propre mdp Mysql
  user = "",
  password = "",
  database = "PROJET"
)
#créer un curseur de base de données pour effectuer des opérations SQL
cur = db.cursor()

#Créer une DB:
#cur.execute("CREATE DATABASE PROJET")

#Afficher toutes les DB qui existe deja:
#cur.execute("SHOW DATABASES")
#for db in cur:
  #print(db)

#Créer une Table dans une DB:
#cur.execute("CREATE TABLE data(name VARCHAR(255), review VARCHAR(255), sentiment VARCHAR(255))")

#Afficher les Tables dans une DB:
#cur.execute("SHOW TABLES")
#for tb in cur:
  #print(tb)

def csv_to_mysql(load_sql,host,user,password):
  try:
    connexion = pymysql.connect(
      host=host,
      user=user,
      password=password,
      autocommit=True,
      local_infile=1
      )
    print("Conneted to DB:{}".format(host))

    #Create cursor
    cursor=connexion.cursor()
    cursor.execute(load_sql)
    print("Successfully loaded the table from csv")
    connexion.close()

  except Exception as e:
    print("Error:{}".format(str(e)))
    sys.exit(1)


def mysql_to_csv(sql, file_path, host, user, password): #pas fonctionnel
    try:
        connexion = pymysql.connect(host=host,
                                user=user,
                                password=password)
        print('Connected to DB: {}'.format(host))
        # Read table with pandas and write to csv
        df = pd.read_sql(sql, connexion)
        df.to_csv(file_path, encoding='utf-8', header = True,\
         doublequote = True, sep=',', index=False)
        print('File, {}, has been created successfully'.format(file_path))
        connexion.close()

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)


#lecture fichier
load_sql = "LOAD DATA LOCAL INFILE 'C:/Users/ThinkPad/Desktop/datasetTest.txt' INTO TABLE PROJET.data\
 FIELDS TERMINATED BY ';' ENCLOSED BY '\n' IGNORE 1 LINES;"

host = 'localhost'
#chacun met son id et son propre mdp Mysql
user = ''
password = ''
sql = 'Select * From PROJET.data'
file_path = '' #chacun met son propre chemin pour le nouveau fichier qui sera crée

#Appel de fonctions :
#mysql_to_csv(sql, file_path, host, user, password)

#fonction d'injection a utiliser une seule fois sinon elle dupliquera les données:
#csv_to_mysql(load_sql, host, user, password)


#Suppression de toutes les données d'une table :
#cur.execute("TRUNCATE data")

#faire un Select sur une table :
#cur.execute("SELECT name FROM data")

print("end")