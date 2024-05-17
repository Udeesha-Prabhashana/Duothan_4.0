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
            <div className={type === "list" ? "headerContainer listMode" : "headerContainer"}>
                <div className="headerList">
                    <div className="headerListItem active">
                        <FontAwesomeIcon icon={faBed} />
                        <span>Stay</span>
                    </div>
                    <div className="headerListItem">
                        <FontAwesomeIcon icon={faPlane} />
                        <span>Flights</span>
                    </div>
                    <div className="headerListItem">
                        <FontAwesomeIcon icon={faCar} />
                        <span>Car rentals</span>
                    </div>
                    <div className="headerListItem">
                        <FontAwesomeIcon icon={faBed} />
                        <span>Attractions</span>
                    </div>
                    <div className="headerListItem">
                        <FontAwesomeIcon icon={faTaxi} />
                        <span>Airport taxis</span>
                    </div>
                </div>
                { type !== "list" &&     //devide 2 sub parts 
                    <>
                        <h1 className="headerTitle">A lifetime of discounts? It's Genius </h1>
                        <p className="headerDesc">Get rewarded for your travels - unlock instant saving of 10% or more with a free WH booking account</p>
                        {/* {!user && <button className="headerBtn"> Sign in / Register </button>} */}
                        <div className="headerSerch">
                        <div className="headerSearchItem">
                        <FontAwesomeIcon icon={faBed} className="headerIcon" />  
                            <input
                                type="text"
                                placeholder="Where are you going?"
                                className="headerSearchInput"
                                onChange={e=>setDestination(e.target.value)}  // When the input value changes, this function will be called and the 'destination' state will be updated with the new value.
                            />    
                        </div>
                        <div className="headerSearchItem">      
                        <FontAwesomeIcon icon={faCalendarDays} className="headerIcon" /> //calender
                            <span onClick={()=>setOpenDate(!openDate)} className="headerSearchtext"> {`${ format(
                                dates[0].startDate,
                                "MM/dd/yyyy"
                            )} to ${ format(dates[0].endDate, "MM/dd/yyyy") }`} </span>  
                            {openDate && <DateRange
                            editableDateInputs={true}
                            onChange={item => setDates([item.selection])}
                            moveRangeOnFirstSelection={false}
                                ranges={dates}
                                className="date"
                                minDate={new Date()}
                            />}
                        </div>
                        <div className="headerSearchItem">
                        <FontAwesomeIcon icon={faPerson} className="headerIcon" />
                            <span onClick={()=>setOpenOptions(!openOption)} className="headerSearchtext"> {`${ options.adult } adult • ${ options.children } children • ${ options.room } room`}</span>
                            {openOption && <div className="option">
                                <div className="optionItem">
                                    <span className="optionText"> Adult</span>
                                    <div className="optionCounter">
                                        <button disabled={options.adult <= 1} className="optionCounterButton" onClick={()=>handleOption("adult", "d")}> - </button>  
                                        <span className="optionCountNumber">{options.adult}</span>
                                        <button className="optionCounterButton" onClick={()=>handleOption("adult", "i")}> + </button>
                                    </div>
                                </div>
                                <div className="optionItem">
                                    <span className="optionText"> Children</span>
                                    <div className="optionCounter">
                                        <button disabled={options.children <= 0} className="optionCounterButton" onClick={()=>handleOption("children", "d")}> - </button>
                                        <span className="optionCountNumber">{options.children}</span>
                                        <button className="optionCounterButton" onClick={() => handleOption("children", "i")}> + </button>
                                    </div>
                                </div>
                                <div className="optionItem">
                                    <span className="optionText"> Room</span>
                                    <div className="optionCounter">
                                        <button disabled={options.room <= 1} className="optionCounterButton" onClick={()=>handleOption("room", "d")}> - </button>
                                        <span className="optionCountNumber">{options.room}</span>
                                        <button className="optionCounterButton" onClick={()=>handleOption("room", "i")}> + </button>
                                    </div>
                                </div>
                            </div>}
                        </div>
                        <div className="headerSearchItem">
                            <button className="headerBtn" onClick={handleSearch}>Search</button> 
                        </div>
                        </div>
                    </>
                }
            </div>
        </div>
    )
}

export default Header