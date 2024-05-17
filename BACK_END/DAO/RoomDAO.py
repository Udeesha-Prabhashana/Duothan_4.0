import uuid
from db_config import get_db_connection
import pymysql
import json
from flask import jsonify
import datetime


class RoomDAO:

    @classmethod
    def checkRoomWithGivenID(cls, room_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(" * from room where room_id=%s",
                           room_id)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def checkRoomWithNumber(cls, room_number):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * from room where room_number=%s",
                           room_number)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
            
    @classmethod
    def updateRoomAvailblity(cls, id, rooomnumber, date_objects):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Iterate over the date_objects list and insert each date separately
            for date in date_objects:
                cursor.execute("INSERT INTO room_numbers (room_id, room_number, unavailable_date) VALUES (%s, %s, %s)",
                            (id, rooomnumber, date))

            # Commit the transaction
            conn.commit()
            return "updated successfull"
        except Exception as e:
            print(e)
            conn.rollback()  # Rollback the transaction in case of any error

        finally:
            cursor.close()
            conn.close()


    @classmethod
    def adminCheckFromSessionID(cls, session_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * from admin where session_id=%s",
                           session_id)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getHotel(cls,id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            print(" id", id)
            # Prepare the SQL query with parameters
            sql_query = """
            SELECT * FROM hotels
            WHERE hotel_id = %s;
            """

            # Execute the query with parameter substitution to prevent SQL injection
            cursor.execute(sql_query, (id,))
            rows = cursor.fetchall()
            # Assuming cursor.description is available to get column names
            columns = [column[0] for column in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]

            print("Hotel:", result)
            return result
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getAllRooms(cls, id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            print("id", id)

            sql_query = """
            SELECT
                r.room_id,
                r.price,
                r.Average_Rating,
                r.availibility,
                r.facilities,
                r.hotel_id,
                r.maxPeople,
                r.title,
                rn.room_numbers_id,
                rn.room_number,
                rn.unavailable_date
            FROM
                room r
            INNER JOIN
                room_numbers rn ON r.room_id = rn.room_id
            WHERE
                r.hotel_id = %s;
            """

            # Execute the query with parameter substitution to prevent SQL injection
            cursor.execute(sql_query, (id,))
            rows = cursor.fetchall()

            room_details = {}
            for row in rows:
                room_id = row['room_id']
                if room_id not in room_details:
                    room_details[room_id] = {
                        'room_id': room_id,
                        'price': row['price'],
                        'Average_Rating': row['Average_Rating'],
                        'availability': row['availibility'],
                        'facilities': row['facilities'],
                        'hotel_id': row['hotel_id'],
                        'maxPeople': row['maxPeople'],
                        'title': row['title'],
                        'roomNumbers': {}
                    }
                
                room_number = row['room_number']
                if room_number not in room_details[room_id]['roomNumbers']:
                    room_details[room_id]['roomNumbers'][room_number] = {
                        'room_number': room_number,
                        'unavailableDates': []
                    }
                
                if row['unavailable_date']:
                # Check if time information is present, if not, add a default time
                    if row['unavailable_date'].time() == datetime.time(0, 0):
                        formatted_date = row['unavailable_date'].replace(hour=18, minute=30).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
                    else:
                        formatted_date = row['unavailable_date'].strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
                    room_details[room_id]['roomNumbers'][room_number]['unavailableDates'].append(formatted_date)

            # Convert the roomNumbers from dict to list
            for room_id in room_details:
                room_details[room_id]['roomNumbers'] = list(room_details[room_id]['roomNumbers'].values())

            result = list(room_details.values())

            print("Rooms:", result)
            return result
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()



    @classmethod
    def getAllRoomsADMIN(cls):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from room")
            rows = cursor.fetchall()

            # Assuming cursor.description is available to get column names
            columns = [column[0] for column in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]

            print("Rooms", result)
            return result
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getAllRoomsForUser(cls):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT room_id,room_number,price,Average_Rating,availibility,facilities from room where availibility='Yes'")
            rows = cursor.fetchall()
            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def getAllRoomsForAdmin(cls):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(" * from room")
            rows = cursor.fetchall()
            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()



    @classmethod
    def getAllDataForUser(cls):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * from room where availibility='Yes'")
            rows = cursor.fetchall()
            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


    # @classmethod
    # def addNewRoom(cls, room_number, price, Average_Rating, facilities,image):
    #     try:
    #         roomId = str(uuid.uuid4())
    #         isAvailable = 'Yes'
    #         EuroPrice = '€'
    #         conn = get_db_connection()
    #         cursor = conn.cursor()

    #         cursor.execute(
    #             "insert into room(room_id, room_number,price,Average_Rating,availibility,facilities,image) value (%s, %s, %s,%s, %s,%s,%s)",
    #             (roomId, room_number, price + EuroPrice, Average_Rating, isAvailable, facilities,image))
    #         conn.commit()
    #         cursor.execute("SELECT * from room r WHERE r.room_id = %s",
    #                        roomId)
    #         rows = cursor.fetchone()
    #         return rows
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         cursor.close()
    #         conn.close()


    @classmethod
    def addnewrooom(cls, price, facilities,hotel_id,maxPeople,title):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "insert into room(price,facilities,hotel_id,maxPeople,title) value (%s, %s,%s, %s, %s)",
                (price, facilities,hotel_id,maxPeople,title))
            conn.commit()
            # cursor.execute("SELECT * from hotels")
            # rows = cursor.fetchone()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def deleteRoomFromDB(cls, room_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("DELETE from room where room_id=%s", room_id)
            conn.commit()
            cursor.execute("SELECT room_id, room_number,price,Average_Rating,availibility,facilities from room")
            rows = cursor.fetchall()
            return rows
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def checkRoomIsAvailable(cls, room_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * from room where availibility='Yes' and room_id=%s",
                           room_id)
            row = cursor.fetchone()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def adminLogoutDAO(cls, admin_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("update admin set session_id = null where admin_id = %s",
                           admin_id)
            conn.commit()

            cursor.execute("SELECT * from admin where admin_id = %s",
                           admin_id)
            row = cursor.fetchone()
            return row
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def getCurrentRoomData(cls, room_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT room_id,room_number,price,Average_Rating,availibility,facilities from room where room_id=%s",
                           room_id)
            row = cursor.fetchone()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def changeStatusToNo(cls, room_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("UPDATE room set availibility = 'No' where room_id=%s",
                           room_id)
            conn.commit()
            cursor.execute("select room_id,room_number,price,Average_Rating,availibility,facilities from room where room_id=%s",
                           room_id)
            row = cursor.fetchone()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def changeStatusToYes(cls, room_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("UPDATE room set availibility = 'Yes' where room_id=%s",
                           room_id)
            conn.commit()
            cursor.execute("select * from room where room_id=%s",
                           room_id)
            row = cursor.fetchone()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def getAllImages(cls):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("select image from room")
            row = cursor.fetchall()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()


    @classmethod
    def Customerincident(cls):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("select * from incident")
            row = cursor.fetchall()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()


    @classmethod
    def CustomerEnquiry(cls):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("select * from query")
            row = cursor.fetchall()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()


    @classmethod
    def GetRoomID(cls):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("select room_id from room")
            row = cursor.fetchall()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()

    @classmethod
    def getHashPass(cls, username):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT password from admin where username=%s",
                           username)
            rows = cursor.fetchone()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()


    @classmethod
    def adminLoginfromAdminID(cls, username):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * from admin where username=%s",
                           username)
            rows = cursor.fetchone()
            if rows is not None:
                sessionId = str(uuid.uuid4())
                cursor.execute("update admin set session_id = %s where username = %s",
                               (sessionId, username))
                conn.commit()

                cursor.execute("SELECT * from admin where username = %s",
                               username)
                rows = cursor.fetchone()
                return rows
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
