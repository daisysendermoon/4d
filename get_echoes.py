import mysql.connector
import sys
import os
import logging
import json

def write_file(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)

class DOWNLOAD:

    ENDPOINT="four-db.c1jknyskc08v.us-east-2.rds.amazonaws.com"
    PORT="3306"
    USR="admin"
    PASSWD="12345678"
    DBNAME="4d"
    DOMAIN=0.0001
    ECHO_ID="echo_id"
    ECHO_TIME="echo_time"


    def getEchoes(self, longitude, latitude):
        long_low=float(longitude)-self.DOMAIN
        long_high=float(longitude)+self.DOMAIN
        lat_low=float(latitude)-self.DOMAIN
        lat_high=float(latitude)+self.DOMAIN
        try:
            conn =  mysql.connector.connect(host=self.ENDPOINT, user=self.USR, passwd=self.PASSWD, port=self.PORT, database=self.DBNAME)
            cur = conn.cursor()
            cur.execute("""SELECT id, echo_time FROM 4d.echo WHERE longitude >= %s AND longitude <= %s AND
                           latitude >= %s AND latitude <= %s  ORDER BY echo_time """, (long_low, long_high, lat_low, lat_high,))

            record = cur.fetchall()
            retList = []
            for row in record:
                    echo_id = row[0]
                    echo_time = row[1]
                    retList.append({self.ECHO_ID: echo_id, self.ECHO_TIME: str(echo_time)})
            return json.dumps(retList)
            print("Query successful")
        except Exception as e:
            print("Database connection failed due to {}".format(e))  
        finally:
            if conn.is_connected():
        	    cur.close()
        	    conn.close()
        	    print("MySQL connection is closed") 

    def getAudioFile(self, echoId):
        try:
            conn =  mysql.connector.connect(host=self.ENDPOINT, user=self.USR, passwd=self.PASSWD, port=self.PORT, database=self.DBNAME)
            cur = conn.cursor()
            cur.execute("SELECT echo_audio FROM 4d.echo WHERE id = %s ", (echoId,))

            record = cur.fetchall()
            for row in record:
                    echo = row[0]
                    break
            return echo
        except Exception as e:
            print("Database connection failed due to {}".format(e))  
        finally:
            if conn.is_connected():
                cur.close()
                conn.close()
                print("MySQL connection is closed") 
