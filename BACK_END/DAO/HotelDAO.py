import uuid
from db_config import get_db_connection
import pymysql
import json
from flask import jsonify


class HotelDAO:

    # @classmethod
    # def checkRoomWithGivenID(cls, room_id):
    #     try:
    #         conn = get_db_connection()
    #         cursor = conn.cursor()

    #         cursor.execute(" * from room where room_id=%s",
    #                        room_id)
    #         rows = cursor.fetchone()
    #         return rows
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         cursor.close()
    #         conn.close()

    # @classmethod
    # def checkRoomWithNumber(cls, room_number):
    #     try:
    #         conn = get_db_connection()
    #         cursor = conn.cursor()

    #         cursor.execute("SELECT * from room where room_number=%s",
    #                        room_number)
    #         rows = cursor.fetchone()
    #         return rows
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         cursor.close()
    #         conn.close()

    # @classmethod
    # def adminCheckFromSessionID(cls, session_id):
    #     try:
    #         conn = get_db_connection()
    #         cursor = conn.cursor()

    #         cursor.execute("SELECT * from admin where session_id=%s",
    #                        session_id)
    #         rows = cursor.fetchone()
    #         return rows
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         cursor.close()
    #         conn.close()


    @classmethod
    def getAllHotels(cls):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * from hotels")
            rows = cursor.fetchall()

            # Assuming cursor.description is available to get column names
            columns = [column[0] for column in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]

            print("HOtels", result)
            return result
        except Exception as e:

            print(e)
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def getAllFilterdHotels(cls, city, min_price, max_price):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            print(" cityy", city)
            print(" min_price", min_price)
            print(" max_price", max_price)
            # Prepare the SQL query with parameters
            sql_query = """
            SELECT * FROM hotels
            WHERE city = %s AND cheapestPrice BETWEEN %s AND %s;
            """

            # Execute the query with parameter substitution to prevent SQL injection
            cursor.execute(sql_query, (city, min_price, max_price))
            rows = cursor.fetchall()
            # Assuming cursor.description is available to get column names
            columns = [column[0] for column in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]

            print("Filtered Hotels:", result)
            return result
        except Exception as e:
            print(e)
            return []  # Return an empty list in case of an error
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


    # @classmethod
    # def getAllRoomsForUser(cls):
    #     try:
    #         conn = get_db_connection()
    #         cursor = conn.cursor()
    #         cursor.execute("SELECT room_id,room_number,price,Average_Rating,availibility,facilities from room where availibility='Yes'")
    #         rows = cursor.fetchall()
    #         return rows
    #     except Exception as e:

    #         print(e)
    #     finally:
    #         cursor.close()
    #         conn.close()


    # @classmethod
    # def getAllRoomsForAdmin(cls):
    #     try:
    #         conn = get_db_connection()
    #         cursor = conn.cursor()

    #         cursor.execute(" * from room")
    #         rows = cursor.fetchall()
    #         return rows
    #     except Exception as e:

    #         print(e)
    #     finally:
    #         cursor.close()
    #         conn.close()


    # @classmethod
    # def getAllDataForUser(cls):
    #     try:
    #         conn = get_db_connection()
    #         cursor = conn.cursor()

    #         cursor.execute("SELECT * from room where availibility='Yes'")
    #         rows = cursor.fetchall()
    #         return rows
    #     except Exception as e:

    #         print(e)
    #     finally:
    #         cursor.close()
    #         conn.close()


    @classmethod
    def addNewHotel(cls, type, city, address,title,photo, description):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            print("request", type)
            print("request", city)
            print("request", address)
            print("request", title)
            print("request", photo)
            print("request", description)
            cursor.execute(
                "insert into hotels (type, city,address,title,photo,description) value (%s, %s, %s,%s, %s,%s)",
                (type, city, address,title, photo, description))
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
    def deleteHotelsFromDB(cls, hotel_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            print("hotel_ID", hotel_id)

            hotel_id2 = int(hotel_id)

            cursor.execute("DELETE from hotels where hotel_id=%s",  (hotel_id2,))
            conn.commit()
            cursor.execute("SELECT * from hotels")
            rows = cursor.fetchall()
            return 1
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
            cursor.execute("select photo from hotels")
            row = cursor.fetchall()
            return row
        except Exception as e:

            print(e)
        finally:
            cursor.close()
