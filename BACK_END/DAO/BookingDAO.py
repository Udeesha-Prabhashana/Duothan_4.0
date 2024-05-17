import uuid
from db_config import get_db_connection
import pymysql
import json
from flask import jsonify

class BookingDAO:


    @classmethod
    def getAllBookings(cls):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * from booking")
            rows = cursor.fetchall()
            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def addRoomBooking(cls, customer_id, room_id,email):
        try:
            bookingId = str(uuid.uuid4())
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "insert into booking (booking_id, customer_id,room_id,email) value (%s, %s, %s,%s)",
                (bookingId, customer_id, room_id,email))
            conn.commit()
            cursor.execute("UPDATE room set availibility='No' where room_id=%s ",
                           room_id)
            conn.commit()
            cursor.execute("SELECT * from booking r WHERE r.booking_id = %s",
                           bookingId)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def contactUS(cls, customer_id, username,description):
        try:
            incidentId = str(uuid.uuid4())
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "insert into incident(incident_id,customer_id, username,description) value (%s,%s, %s, %s)",
                (incidentId,customer_id, username,description))
            conn.commit()

            cursor.execute("SELECT * from incident WHERE incident_id = %s",
                           incidentId)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def contactUsViaHome(cls, name, email, description):
        try:
            query_id = str(uuid.uuid4())
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "insert into query(query_id,name, email,description) value (%s,%s, %s, %s)",
                (query_id, name, email, description))
            conn.commit()

            cursor.execute("SELECT * from query WHERE query_id = %s",
                           query_id)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

