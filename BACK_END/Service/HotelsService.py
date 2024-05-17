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
from DAO.HotelDAO import HotelDAO

class HotelService:
    roomDAO = RoomDAO()
    bookingDAO = BookingDAO()
    hotelDAO = HotelDAO()


    @classmethod
    def getAllHotelsfromDBCheck(cls):
        responseData = cls.hotelDAO.getAllHotels()
        print("Hotel2", responseData)
        return responseData
    
    @classmethod
    def getAllCustomersfromDBCheck(cls):
        responseData = cls.hotelDAO.getAllCustomers()
        print("Customers", responseData)
        return responseData

    @classmethod
    def getAllHotelsfromDBCheck23(cls, city, min_price, max_price):
        responseData = cls.hotelDAO.getAllFilterdHotels(city, min_price, max_price)
        print("Hotel2", responseData)
        return responseData
    
    @classmethod
    def gethotelbyID(cls, id):
        responseData = cls.hotelDAO.getHotel(id)
        print("Hotel2", responseData)
        return responseData

    # @classmethod
    # def getAllRooms(cls):
    #     responseData = cls.roomDAO.getAllRooms()
    #     if responseData is not None:
    #         return True
    #     else:
    #         return False


    # @classmethod
    # def getAllRoomsForUser(cls):
    #     responseData = cls.roomDAO.getAllRoomsForUser()
    #     if responseData is not None:
    #         return True
    #     else:
    #         return False

    @classmethod
    def addHotel(cls,data):
        responseData = cls.hotelDAO.addNewHotel(data.get('type'), data.get('city'), data.get('address'),data.get('title'),data.get('photo'),data.get('description') )
        if responseData is not None:
            return "Registration successful!"
        else:
            return "Registration unsuccessful!"


    @classmethod
    def deleteHotel(cls, data):
        responseData = cls.hotelDAO.deleteHotelsFromDB(data.get('hotel_id'))        
        if responseData is not None:
            return "Deleted successful!"
        else:
            return "Deleted unsuccessful!"