from flask import Flask, jsonify
from CustomUtils import CustomUtils
from db_config import get_db_connection
from Service.CustomerService import CustomerService
from Service.HotelsService import HotelService
from Service.RoomService import RoomService
from flask import flash, request, render_template
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
from flask_cors import CORS
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = '121333nunnehcnuhbh34h3'
CORS(app)

customerService = CustomerService()

@app.route('/')
def index():
    return "Hello!"

@app.route('/python')
def python():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    value = cursor.fetchall()
    print("Values fetched:", value)
    cursor.close()
    connection.close()
    return str(value)


@app.route("/addCustomer", methods=['POST'])
def addCustomerInDB():
    wsResponse = {"resultSet": None, "operationStatus": None}
    try:
        responseData = customerService.createCustomer(request.json)
        wsResponse['resultSet'] = responseData
        wsResponse['operationStatus'] = 1
    except InvalidContactNumber:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.INVALID_CONTACT_NUMBER
    except PasswordTooShort:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.PASSWORD_TOO_SHORT
    except InvalidEmail:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.INVALID_EMAIL
    except InvalidName:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.INVALID_NAME
    except SomethingWentWrong:
        wsResponse['resultSet'] = None
        wsResponse['operationStatus'] = CustomUtils.SOMETHING_WENT_WRONG
    return wsResponse

# Your existing login route
@app.route("/Login", methods=['POST'])
def customerLogin():
    try:
        # Print the request body for debugging
        print("Request JSON:", request.json)

        request_data = request.json  # Get the JSON data from the request
        username = request_data.get('username')  # Extract username from JSON data
        password = request_data.get('password')  # Extract password from JSON data
        
        # Print the extracted username and password for debugging
        print("Username:", username)
        print("Password:", password)
        
        data = customerService.customerLogin({'username': username, 'password': password}, app.secret_key)
        return jsonify({'res': data}), 200
    except WrongCredentials:
        return jsonify({'error': 'Wrong credentials'}), 401
    

@app.route("/customers", methods=['GET'])
def getAllCustomers():
    Response = CustomerService.getAllCustomersfromDBCheck()   
    print("Hotels3", Response) 
    return jsonify(Response)

if __name__ == "__main__":
    app.run(debug=True)
