import psycopg2
import json
from secrets import get_secret_image_gallery

#db_host = "image-gallery.cs4qwvqazvut.us-west-1.rds.amazonaws.com"
#db_name = "image_gallery"
#db_user = "image_gallery"

#password_file = "/home/ec2-user/.image_gallery_config"

#connection = None

#def get_secret():
#   jsonString = get_secret_image_gallery()
#  return json.loads(jsonString)

#def get_password():
    #return passwordFind()
#def passwordFind():
   # f = open(password_file, "r")
    #result = f.readline()
  #  f.close()

#def get_host():
 #   return db_host

#def get_username():
#    return db_user

#def get_dbname():
 #   return db_name

#def connect():
#    global connection
    #secret = get_secret()
 #   connection = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=get_password())

#def execute(query,args=None):
 #   global connection
  #  cursor = connection.cursor()
   # if not args:
    #    cursor.execute(query)
    #else:
     #   cursor.execute(query, args)
    #return cursor

#def main():
 #   connect()
  #  res = execute('select * from users')
   # for row in res:
    #    print(row)

#if __name__ == '__main__':
 #   main()
db_host = "image-gallery.cs4qwvqazvut.us-west-1.rds.amazonaws.com"
db_name = "image_gallery"
db_user = "image_gallery"

password_file = "/home/ec2-user/.image_gallery_config"


def get_password():
    f = open(password_file, "r")
    result = f.readline()
    f.close()
    return result[:-1]

def get_host(secret):
    return secret['host']

def get_username(secret):
    return secret['username']

def get_dbname(secret):
    return secret['database_name']

def connect():
    global connection
    connection = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=get_password())
    connection.set_session(autocommit=True)

def execute(query, args=None):
    global connection
    cursor = connection.cursor()
    if not args:
        cursor.execute(query)
    else:
        cursor.execute(query, args)
        return cursor

