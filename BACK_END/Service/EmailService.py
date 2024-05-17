# import smtplib
# import ssl
# from flask_mail import Mail, Message
# from app import mail


# class EmailService:

#     @classmethod
#     def sendEmail(cls, email,bookingId,room_number,price,facilities,Average_Rating):
#         try:
#             msg = Message('Room booking confirmation mail!!!', sender='mahashabdemanik@gmail.com',
#                         recipients=[email])
#             msg.html = "<h3 align='center'>Hello User</h3> <br> <p> Your room has been booked successfully</p><br>" \
#                         "<p> Below is your booking details</p><br>" \
#                        "<p>Booking ID: </p>" + bookingId + \
#                        "<p>Room Number: </p>" + room_number + \
#                        "<p>Price: </p>" + price + \
#                        "<p>Facilities include: </p>" + facilities + \
#                        "<p>Average Customer Ratings: </p>" + Average_Rating + \
#                        "<p>Regards,<br>Team Admin</p>"
#             mail.send(msg)
#             return True
#         except Exception as e:
#             return False


#     @classmethod
#     def contactUsEmail(cls, inci, desc, data):
#         try:
#             incident = inci
#             description = desc
#             msg = Message('Thanks for contacting Us', sender='mahashabdemanik@gmail.com',
#                       recipients=[data])
#             msg.html = "<h3 align='center'>Hello User</h3> <br> <p> Thanks for reaching out to us." \
#                     " We will get back to you shortly. Please find below <b>incident ID</b> for reference</p><br>" \
#                     + incident + \
#                     "<br><b>Description</b>:" + description + \
#                     "<p>Regards,<br>Team Admin</p>"
#             mail.send(msg)
#             return True
#         except Exception as e:
#             return False

#     @classmethod
#     def contactUsEmailbyHome(cls,inci, name, email, desc):
#         try:
#             msg = Message('Thanks for contacting Us', sender='mahashabdemanik@gmail.com',
#                         recipients=[email])
#             msg.html = "<h3 align='center'>Hello <b>" + name + "<b> </h3>" "<br> <p> Thanks for reaching out to us." \
#                         " We will get back to you shortly. Please find below <b>incident ID</b> for reference</p><br>" \
#                         + inci + \
#                         "<br><b>Description</b>:" + desc + \
#                         "<p>Regards,<br>Team Admin</p>"
#             mail.send(msg)
#             return True
#         except Exception as e:
#             return False


#     @classmethod
#     def custCreateMail(cls, cust_id, data):
#         try:
#             cust = cust_id
#             msg = Message('Registration successful', sender='mahashabdemanik@gmail.com',
#                       recipients=[data])
#             msg.html = "<h3 align='center'>Hello User</h3> <br> <p> You have been registered successfully." \
#                     " Please find below your customer ID</p><br>" \
#                     "<b>Customer ID:<b>" + cust + \
#                     "<p>Regards," \
#                     "<br>Team Admin</p>"
#             mail.send(msg)
#             return True
#         except Exception as e:
#             return False


#     @classmethod
#     def forgotPasswordEmail(cls, cust_id, email, otp):
#         try:
#             custID = cust_id
#             emailID = email
#             OTP = otp
#             msg = Message('Password Reset Email', sender='mahashabdemanik@gmail.com',
#                          recipients=[emailID])
#             msg.html = "<h3 align='center'>Hello User</h3> <br> <p> Thanks for reaching out to us." \
#                         " Below is the 6 digit OTP for resetting your password for customer ID" \
#                         "<br>" + custID +  \
#                         "<br>" + "<b>" + OTP + "</b>"\
#                         "<br>"\
#                         "<p>Regards,<br>Team Admin</p>"
#             mail.send(msg)
#             return True
#         except Exception as e:
#             return False

