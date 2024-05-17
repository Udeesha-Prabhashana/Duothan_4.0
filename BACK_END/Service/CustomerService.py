import uuid
from wsgiref import headers
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, jsonify
from DAO.CustomerDAO import CustomerDAO
from DAO.RoomDAO import RoomDAO
from Exceptions.InvalidContactNumber import InvalidContactNumber
from Exceptions.InvalidEmail import InvalidEmail
from Exceptions.InvalidName import InvalidName
from Exceptions.NewPasswordCannotBeSameAsOldPassword import NewPasswordCannotBeSameAsOldPassword
from Exceptions.OTP_Not_Correct import OTP_Not_Correct
from Exceptions.PasswordTooShort import PasswordTooShort
from Exceptions.WrongCredentials import WrongCredentials
from Exceptions.NoCustomersExist import NoCustomersExist
from Exceptions.RoomNotAvailable import RoomNotAvailable
from Exceptions.SomethingWentWrong import SomethingWentWrong
# from Service.EmailService import EmailService
from Service.RoomService import RoomService
import jwt

class CustomerService:
    customerDAO = CustomerDAO()
    # emailService = EmailService()
    roomService = RoomService()
    roomDAO = RoomDAO()

    @classmethod
    def forgotPassword(cls, data):
        if cls.forgotPasswordCheck(data):
            otp = str(uuid.uuid4())
            OTP = otp[0:6]
            responseData = cls.customerDAO.forgotPasswordDB(data.get('customer_id'), data.get('email'), OTP)
            # cls.emailService.forgotPasswordEmail(responseData.get('customer_id'), responseData.get('email'), OTP)
        else:
            raise WrongCredentials
        return responseData

    @classmethod
    def newPassword(cls, data):
        if cls.OTPCheck(data):
            custData = cls.customerDAO.OTPCheck(data.get('OTP'))
            newPassword = data.get('password')
            if len(newPassword.strip()) >= 8:
                oldPassword = custData.get('password')
                result = check_password_hash(oldPassword, newPassword)
                if result:
                    raise NewPasswordCannotBeSameAsOldPassword

                else:
                    hashedPassword = generate_password_hash(newPassword)
                    responseData = cls.customerDAO.UpdateNewPassword(hashedPassword, data.get('OTP'))
            else:
                raise PasswordTooShort
        else:
            raise OTP_Not_Correct
        return responseData

    @classmethod
    def getAllCustomers(cls):
        global responseData
        if cls.getAllCustomersCheck():
            responseData = cls.customerDAO.getAllCustomersfromDB()
        return responseData

    @classmethod
    def getAllCustomersfromDBCheck(cls):
        responseData = cls.customerDAO.getAllCustomers()
        print("Customers", responseData)
        return responseData
    
    @classmethod
    def getAllCustomersLocations(cls):
        responseData = cls.customerDAO.getAllLocations()
        print("Customers", responseData)
        return responseData
    
    @classmethod
    def createCustomer(cls, data):
        global responseData
        z = data.get('name')
        count = 0

        for j in z:
            if j in "0, 1, 2, 3, 4, 5, 6, 7, 8, 9,@,#,$,%,&,*":
                count = count + 1
        if count == 0:
            x = data.get('email')
            count2 = 0
            count1 = 0
            for i in x:
                if i == '@':
                    count2 = count2 + 1
                elif i == '.':
                    count1 = count1 + 1
            if count2 == 1 and count1 == 1:
                y = data.get('contact_no')
                count3 = 0
                for j in y:
                    if j not in "0, 1, 2, 3, 4, 5, 6, 7, 8, 9":
                        count3 = count3 + 1
                if count3 != 0:
                    raise InvalidContactNumber
                else:
                    password1 = data.get('password')
                    if len(password1.strip()) >= 8:

                        hashedPassword = generate_password_hash(password1)

                        responseData = cls.customerDAO.createNewCustomer(data.get('name'), data.get('username'),
                                                                             hashedPassword,
                                                                             data.get('email'),
                                                                             data.get('contact_no'),
                                                                             data.get('vehical_number'))
                        # cls.emailService.custCreateMail(responseData.get('customer_id'), responseData.get('email'))
                        return "Registration successful!"
                    else:
                        raise PasswordTooShort

            else:
                raise InvalidEmail
        else:
            raise InvalidName


    @classmethod
    def customerLogin(cls, data, secret_key):
        if cls.customerLoginCheck(data.get('username'), data.get('password')):
            # Assuming you have customer_id and user_role in customerData
            customerData = cls.customerDAO.customerDetails(data.get('username'))
            customer_id = customerData[0]  # Accessing the first element
            user_role = customerData[-1]   # Accessing the last elemen

            print("customerData :", customerData)
            print("customer_id :", customer_id)
            print("user_role :", user_role)

            jwt_token = jwt.encode({'customer_id': customer_id, 'user_role': user_role}, secret_key, algorithm='HS256')
        
            # Return a dictionary containing both the JWT token and the user role
            return {'jwt_token': jwt_token, 'user_role': user_role}
        else:
            raise WrongCredentials

    @classmethod
    def checkCustomerFromSessionID(cls, headerData):
        responseData = cls.customerDAO.checkCustomerFromSessionID(headerData)

        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def getAllCustomersCheck(cls):
        responseData = cls.customerDAO.getAllCustomersfromDB()
        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def customerLoginCheck(cls,username,password):
        print("username2 :", username)
        print("password2 :", password)
        
        password_hash = cls.customerDAO.getHashPass(username)
        print("password_hash :", password_hash)
        if password_hash is None:
            return False  # Handle case where password hash is not found
        # passwordHash = password1.get('password')

        # Extract the password hash from the tuple
        password_hash2 = password_hash[0]
        print("password_hash2 :", password)
        result = check_password_hash(password_hash2, password)
        return result

    @classmethod
    def forgotPasswordCheck(cls, data):
        responseData = cls.customerDAO.forgotPasswordCheck(data.get('customer_id'), data.get('email'))
        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def OTPCheck(cls, data):
        responseData = cls.customerDAO.OTPCheck(data.get('OTP'))
        if responseData is not None:
            return True
        else:
            return False

    @classmethod
    def userLogoutService(cls, customer_id):
        responseData = cls.customerDAO.userLogoutDAO(customer_id)
        session.pop('loginData')
        return responseData
