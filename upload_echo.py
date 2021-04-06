import mysql.connector
import sys
import os
import logging

class UPLOAD:

    ENDPOINT="four-db.c1jknyskc08v.us-east-2.rds.amazonaws.com"
    PORT="3306"
    USR="admin"
    PASSWD="12345678"
    DBNAME="4d"

    def upload(self, longitude, latitude, file):
        conn = None
        try:
            conn =  mysql.connector.connect(host=self.ENDPOINT, user=self.USR, passwd=self.PASSWD, port=self.PORT, database=self.DBNAME)
            cur = conn.cursor()
            sql_insert_blob_query = """ INSERT INTO 4d.echo
        					(user_id, longitude, latitude, altitude, echo_space, echo_time, echo_audio_id, echo_audio)
        						VALUES(1, longitude, latitude, 0, NULL, CURDATE(), 1, %s)"""

            # crazy = open('/Users/richardliu/project/crazy.m4a', 'rb').read()
            result = cur.execute(sql_insert_blob_query, (file,))
            conn.commit()
        except Exception as e:
            print("Database execution failed due to {}".format(e)) 
        finally:
            if conn.is_connected():
        	    cur.close()
        	    conn.close()
        	    print("MySQL connection is closed") 