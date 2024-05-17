import axios from "axios";
import { useContext, useState } from "react";
import { useNavigate } from "react-router-dom";          //use to navigate
import { AuthContext } from "../../context/AuthContext";  
import "./register.css";

const Register = () => {
  const [credentials, setCredentials] = useState({
    username: undefined,
    password: undefined,
    email: undefined,
    name: undefined,
    contact_no: undefined,
    vehicle_reg_no: undefined,
  });

  const { user,loading, error, dispatch } = useContext(AuthContext); //

  console.log(user)
  const navigate = useNavigate()      //allows you to programmatically navigate to different routes in your application

  const handleChange = (e) => {
    setCredentials((prev) => ({ ...prev, [e.target.id]: e.target.value }));   //example, if the id of the username input is "username", the code will update credentials.username with the new value entered by the user.
  };


  const handleClick = async (e) => {       //axios can use only in async 
    e.preventDefault();      //cann't lord given page     
    try {
      const res = await axios.post("http://127.0.0.1:5000/addCustomer", credentials);         //sends a POST request to the /auth/login endpoint with the credentials object as the payload. The credentials object contains the username and password entered by the user
      console.log(" response", res.data.res)

      navigate("/login")    

    } catch (err) {
      dispatch({ type: "LOGIN_FAILURE", payload: err.response.data });
    }
  };

  return (
    <div className="login">
      <div className="lContainer">
        <h3 className='header'> REGISTER TO NEOTROPOLIS</h3>
        <span> USERNAME</span>
        <input
          type="text"
          placeholder="username"
          id="username"
          onChange={handleChange}
          className="lInput"
        />
        <span> PASSWORD</span>
        <input
          type="password"
          placeholder="password"
          id="password"
          onChange={handleChange}
          className="lInput"
        />
        <span>EMAIL</span>
        <input
          type="email"
          placeholder="Enter email"
          id="email"
          onChange={handleChange}
          className="lInput"
        />
        <span>NAME</span>
        <input
          type="text"
          placeholder="Enter name"
          id="name"
          onChange={handleChange}
          className="lInput"
        />
        <span>CONTACT NUMBER</span>
        <input
          type="tel"
          placeholder="Enter contact number"
          id="contact_no"
          onChange={handleChange}
          className="lInput"
        />
        <span>VEHICLE REG NO</span>
        <input
          type="tel"
          placeholder="Enter vehicle reg number"
          id="vehiclE_reg_no"
          onChange={handleChange}
          className="lInput"
        />
        <button disabled={loading} onClick={handleClick} className="lButton">
          Register
        </button>
        {error && <span>{error.message}</span>}
      </div>
    </div>
  );
};

export default Register;