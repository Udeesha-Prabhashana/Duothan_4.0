import base64
from wsgiref import headers
import json
from flask import session
from werkzeug.wrappers import json
from werkzeug.security import generate_password_hash, check_password_hash

from DAO.RoomDAO import RoomDAO
from DAO.BookingDAO import BookingDAO
from Exceptions.NoBookingsExist import NoBookingsExist
from Exceptions.NotAuthorized import NotAuthorized
from Exceptions.RoomNotAvailable import RoomNotAvailable
from Exceptions.RoomWithGivenIdDoesNotExist import RoomWithGivenIdDoesNotExist
from Exceptions.RoomWithGivenNumberAlreadyExist import RoomWithGivenNumberAlreadyExist
from Exceptions.WrongCredentials import WrongCredentials


class RoomService:
    roomDAO = RoomDAO()
    bookingDAO = BookingDAO()

    @classmethod
    def adminLogin(cls, data):
        if cls.adminLoginCheck(data.get('username'),data.get('password')):
            adminData = cls.roomDAO.adminLoginfromAdminID(data.get('username'))
            session['adminDataStored'] = adminData
            responseData = cls.roomDAO.getAllRooms()
        else:
            raise WrongCredentials
        return responseData


    @classmethod
    def getAllBookingsfromDBCheck(cls):
        responseData = cls.bookingDAO.getAllBookings()
        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def getAllRoomsByID(cls, id ):
        responseData = cls.roomDAO.getAllRooms( id)
        print("Rooms", responseData)
        return responseData
    
    @classmethod
    def addroom(cls,data):
        responseData = cls.roomDAO.addnewrooom(data.get('price'),data.get('facilities'),data.get('hotel_id'),data.get('maxPeople'),data.get('title') )
        if responseData is not None:
            return "Room added successful!"
        else:
            return "Room added unsuccessful!"
    
    

    @classmethod
    def getAllRooms(cls):
        responseData = cls.roomDAO.getAllRoomsADMIN( )
        print("Rooms", responseData)
        return responseData
    

    @classmethod
    def updateRoomAvailble(cls, id , roomnumber, date_objects):
        responseData = cls.roomDAO.updateRoomAvailblity( id , roomnumber, date_objects)
        print("Rooms", responseData)
        return responseData
        

    @classmethod
    def getAllRoomsForUser(cls):
        responseData = cls.roomDAO.getAllRoomsForUser()
        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def addRoom(cls,room_number,price,Average_Rating,facilities,image):

        if cls.checkRoomWithNumber(room_number):
            roomData = cls.roomDAO.addNewRoom(room_number, price, Average_Rating,facilities,image)
            responseData = cls.roomDAO.getAllRoomsForAdmin()
        else:
            raise RoomWithGivenNumberAlreadyExist
        return responseData


    @classmethod
    def deleteRoom(cls,header, data):
        if cls.adminCheckFromSessionID(header):
            if cls.checkRoomWithGivenID(data):
                responseData = cls.roomDAO.deleteRoomFromDB(data.get('room_id'))
            else:
                raise RoomWithGivenIdDoesNotExist
        else:
            raise NotAuthorized
        return responseData


    @classmethod
    def changeRoomStatus(cls,header, data):
        global responseData
        if cls.adminCheckFromSessionID(header):
            if cls.checkRoomWithGivenID(data):
                roomDataWithGivenID = cls.roomDAO.checkRoomWithGivenID(data.get('room_id'))
                print(roomDataWithGivenID)
                checkStatus = roomDataWithGivenID.get('availibility')
                if checkStatus == 'Yes':
                    responseData = cls.roomDAO.changeStatusToNo(data.get('room_id'))
                    print(responseData)
                elif checkStatus == 'No':
                    responseData = cls.roomDAO.changeStatusToYes(data.get('room_id'))
                    print(responseData)
            else:
                raise RoomWithGivenIdDoesNotExist
        else:
            raise NotAuthorized
        return responseData


    @classmethod
    def checkRoomIsAvailable(cls, data):
        responseData = cls.roomDAO.checkRoomIsAvailable(data)
        if responseData is not None:
            return True
        else:
            return None


    @classmethod
    def adminLoginCheck(cls,username,password):
        password1 = cls.roomDAO.getHashPass(username)
        passwordHash = password1.get('password')
        result = check_password_hash(passwordHash, password)
        return result


    @classmethod
    def adminCheckFromSessionID(cls, header):
        responseData = cls.roomDAO.adminCheckFromSessionID(header.get('session_id'))
        if responseData is not None:
            return True
        else:
            return None


    @classmethod
    def checkRoomWithNumber(cls, room_number):
        responseData = cls.roomDAO.checkRoomWithNumber(room_number)
        if responseData is None:
            return True
        else:
            return None


    @classmethod
    def checkRoomWithGivenID(cls, data):
        responseData = cls.roomDAO.checkRoomWithGivenID(data.get('room_id'))
        if responseData is not None:
            return True
        else:
            return None


    @classmethod
    def adminLogoutService(cls, admin_id):
        responseData = cls.roomDAO.adminLogoutDAO(admin_id)
        session.pop('adminDataStored')
        return responseData

    @classmethod
    def getCurrentRoomData(cls,room_id):
        responseData = cls.roomDAO.getCurrentRoomData(room_id)
        return responseData

