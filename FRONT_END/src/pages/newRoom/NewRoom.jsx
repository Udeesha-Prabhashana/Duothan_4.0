import "./newRoom.scss";
import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbarA/NavbarA";
import DriveFolderUploadOutlinedIcon from "@mui/icons-material/DriveFolderUploadOutlined";
import { useState } from "react";
import useFetch from "../../hooks/useFetch";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const NewRoom = ({ inputs, title }) => {
    
    const [info, setInfo] = useState({});
    const [hotelId, setHotelId] = useState(undefined);
    const [rooms, setRooms] = useState([])
    const navigate = useNavigate();

    const { data, loading, error } = useFetch("/hotels");

    const handleChange = (e) => {
        setInfo(prev => ({ ...prev, [e.target.id]: e.target.value }));
    };

    console.log("hotelID", hotelId)
    console.log("hotelID", info)
    console.log("hotelID", hotelId)
    console.log("hotelID", hotelId)
    console.log("hotelID", hotelId)

    const handleClick = async (e) => {
    e.preventDefault();

    // Prepare the data object to be sent in the request
    const dataToSend = {
        hotel_id: hotelId, // Including the hotel ID from the dropdown
        ...info, // Spread the 'info' object to merge all its properties into 'dataToSend'
    };

        console.log("dataToSend", dataToSend)
    try {
        const response = await axios.post(`http://127.0.0.1:5000/addroom`, dataToSend);
        console.log('Response:', response.data);
        // Optionally, handle any post-request actions here, such as redirecting or updating UI
        navigate("/rooms");
        
    } catch (err) {
        console.log('Error:', err.response ? err.response.data : err.message); // More specific error
    }
}


    return (
        <div className="new"> 
            <Sidebar />
            <div className="newContainer">
                <Navbar />
                <div className="top">
                    <h1>{title}</h1></div>
                <div className="bottom">
                    <div className="right">
                        <form>
                            {inputs.map((input) => (
                                <div className="formInput" key={input.id}>
                                    <label>{input.label}</label>
                                    <input onChange={handleChange} id={input.id} type={input.type} placeholder={input.placeholder} />
                                </div>
                            ))}
                            <div className="formInput">
                                <label>Rooms</label>
                                <textarea
                                onChange={(e) => setRooms(e.target.value)}
                                placeholder="give comma between room numbers."
                                />
                            </div>
                            <div className="formInput" >
                                <label>Choose a hotel</label>
                                <select id="hotelId" onChange={e=>setHotelId(e.target.value)}> 
                                    { loading ? "loading" : data && data.map(hotel => (
                                        <option key={hotel.hotel_id} value={hotel.hotel_id}> { hotel.name}</option>
                                    ))}
                                </select>
                                </div>
                            <button onClick={handleClick}> Send </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default NewRoom