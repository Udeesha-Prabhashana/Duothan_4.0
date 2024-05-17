import { faBed, faCalendarDays, faCar, faPerson, faPlane, faTaxi } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import "./header.css"
import { DateRange } from "react-date-range";
import { useContext, useState } from "react";
import 'react-date-range/dist/styles.css'; // main css file
import 'react-date-range/dist/theme/default.css'; // theme css file
import {format, setDayOfYear} from "date-fns";
import { useNavigate } from "react-router-dom"; //programmatically navigate the user to different routes within the application,like clicking on a button, submitting a form, or performing an action.
import { SearchContext } from "../../context/SearchContext";
import { AuthContext } from "../../context/AuthContext";


const Header = ({ type }) => {
    
    const { user } = useContext(AuthContext);
    const [openDate , setOpenDate] = useState(false)  //beginig it is false
    const [destination , setDestination] = useState("")
    const [dates, setDates] = useState([
        {
            startDate: new Date(),
            endDate: new Date(),
            key: 'selection',
        },
    ]);
    const [openOption, setOpenOptions] = useState(false)
    const [options, setOptions] = useState({    //initial state
        adult: 1,
        children: 0,
        room: 1,
    });

    const navigate = useNavigate()  //call to navigate to different routes in your application

    const handleOption = (name, operation) => {   //declare hanleoption function to incres and decrese count od adult,children,rooms
        setOptions((prev) => {
            return {
                ...prev,
                [name]: operation === "i" ? options[name] + 1 : options[name] - 1,
            };
        });
    };

    const { dispatch } = useContext(SearchContext);

    const handleSearch = () => {
        dispatch({ type: "NEW_SEARCH", payload: { destination, dates, options } });
        navigate("/hotel", { state: { destination, dates, options } });        //call "hotels" page
    };

    return (
        <div className="header">
            
        </div>
    )
}

export default Header