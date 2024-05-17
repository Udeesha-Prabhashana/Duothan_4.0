import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import "./reserve.css"
import { faCircleXmark } from "@fortawesome/free-solid-svg-icons";
import useFetch from "../../hooks/useFetch";
import { useContext, useState } from "react";
import { SearchContext } from "../../context/SearchContext";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Reserve = ({ setOpen, hotelId }) => {
    console.log(" HotelID", hotelId)
    const { data, loading, error } = useFetch(`http://127.0.0.1:5000/getRooms?hotelId=${ hotelId }`);
    console.log("RoomDetails", data)
    const [selectedRooms, setSelectedRooms] = useState([])
    const { dates } = useContext(SearchContext)
    
    console.log(" dates",dates)

    const handleSelect = (e) => {
    const checked = e.target.checked;
    const roomId = e.target.value;
    const roomNumber = e.target.getAttribute('data-room-number'); // Assume you will set this data attribute on the checkbox

    console.log('Selected Room ID:', roomId); // Should log the correct room ID
    console.log('Room Number:', roomNumber); // Should log the corresponding room number

    const roomDetails = { roomId, roomNumber };

    if (checked) {
        setSelectedRooms([...selectedRooms, roomDetails]); // Add the room details
    } else {
        setSelectedRooms(selectedRooms.filter((item) => item.roomId !== roomId)); // Remove by roomId
    }
};

    const navigate = useNavigate();

    console.log("selected_ROOM", selectedRooms)

    const handleClick = async () => {
        try {
            await Promise.all(
                selectedRooms.map(({ roomId, roomNumber }) => {
                    const res = axios.post(`http://127.0.0.1:5000/updateRoomAvailable?roomid=${ roomId }&roomnumber=${roomNumber}`, {
                        dates: alldates
                    });
                    return res.data;
                })   
            );
            setOpen(false)
            // navigate("/");
        }
        catch(err){
            
        };
    }

    // console.log(selectedRooms);

    const getDatesInRange = (startDate,endDate) => {
        const start = new Date(startDate);
        const end = new Date(endDate);
        const date = new Date(start.getTime());
        let list = [];
        
        while (date <= end) {
            list.push(new Date(date).getTime());   //when use getTime() func its give timestamps, its easier to copmir dates 
            date.setDate(date.getDate() + 1);
        }

        return list;
    }

    const alldates = getDatesInRange(dates[0].startDate, dates[0].endDate) //get all dates using user given dates
    console.log("alldates ", alldates)

    const isAvailable = (roomNumber) => {
        if (!roomNumber || !roomNumber.unavailableDates) {
            return false; // Handle the case where roomNumber or its properties are undefined or not of the expected type
        }

        // If unavailable_date is not an array, convert it into an array with a single element
        const dates = Array.isArray(roomNumber.unavailableDates) ? roomNumber.unavailableDates : [roomNumber.unavailableDates];

        // Check if any of the dates are found in alldates
        const isFound = dates.some(date =>
            alldates.includes(new Date(date).getTime())
        );

        return !isFound; // If any date is found in alldates, it's not available; otherwise, it's available
    };

    return (
        <div className="reserve">
            <div className="rContainer">
                <FontAwesomeIcon
                    icon={faCircleXmark}
                    className="rClose"
                    onClick={() => setOpen(false)}
                />
                <span> Select your rooms:</span>
                {data.map((item) => (
                    <div className="rItem" key={item.room_id}>
                        <div className="rItemInfo">
                            <div className="rTitle">{item.title}</div>
                            <div className="rDesc">{item.facilities}</div>
                            <div className="rMax">
                                MAx people: <b>{item.maxPeople}</b>
                            </div>
                            <div className="rPrice">{ item.price}</div>
                        </div>
                        <div className="rSelectRooms">
                            {item.roomNumbers.map(roomNumber => (
                            <div className="room">
                                <label>{roomNumber.room_number}</label>
                                    <input
                                        type="checkbox"
                                        value={item.room_id}
                                        data-room-number={roomNumber.room_number} // This attribute will be used to store room number
                                        onChange={handleSelect}
                                        disabled={!isAvailable(roomNumber)}
                                    />
                            </div>
                            ))}
                        </div>
                    </div>                   
                ))}
                <button onClick={handleClick} className="rButton"> Reserve Now!</button>
            </div>
        </div>
    );
};

export default Reserve