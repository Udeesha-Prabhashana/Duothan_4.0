import "./hotel.css"
import Navbar from "../../components/navbar/Navbar";
import Header from "../../components/header/Header";
import MailList from "../../components/MailList/MailList";
import Footer from "../../components/footer/Footer";
import { faCircleArrowLeft, faCircleArrowRight, faCircleXmark, faLocationDot } from "@fortawesome/free-solid-svg-icons";
import { useContext, useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";   /* for import icon */
import { useLocation, useNavigate } from "react-router-dom";
import useFetch from "../../hooks/useFetch";
import { SearchContext } from "../../context/SearchContext";
import { AuthContext } from "../../context/AuthContext";
import Reserve from "../../components/reserve/Reserve";

const Hotel = () => {


    const location = useLocation();
    const id = location.pathname.split("/")[2] //use to get hotel_id using location
    console.log("HOTEL-ID",id)
    const [slideNumber, setSlideNumber] = useState(0); 
    const [open, setOpen] = useState(false);
    const [openModel, setOpenModel] = useState(false);    //used to reserve the hotel

    const { data, loading, error } = useFetch(`http://127.0.0.1:5000/getHotelByID?id=${ id }`);   //get all data in specific Hotel 
    const { dates, options } = useContext(SearchContext);       //get dates and options in Searchcontext in INITIAL_STATE using "useContext()" fun
    console.log("Dayes-",dates)
    const { user } = useContext(AuthContext);
    const navigate = useNavigate();

    const MILLISECONDS_PER_DAY = 1000 * 60 * 60 * 24;
    function dayDifference(date1, date2) {                     //calculates the difference in days between two Dates
        const timeDiff = Math.abs(date2.getTime() - date1.getTime());
        const diffDays = Math.ceil(timeDiff / MILLISECONDS_PER_DAY);   //rounding up the result using Math.ceil.
        return diffDays;
    }

    const days =  dayDifference(dates[0].endDate, dates[0].startDate);

    const handleOpen = (i) => {
        setSlideNumber(i)
        setOpen(true);
    };

    const handleMove = (direction) => {   /* declare fun for increase and decrese the slidenumber */
        let newSlideNumber;

        if (direction === "l") {
            newSlideNumber = slideNumber === 0 ? 5 : slideNumber - 1;    /* slideNumber === 0 ? 5 use to when slideNumber be 0, it go to slideNumber 5 */
        } else {
            newSlideNumber = slideNumber === 5 ? 0 : slideNumber + 1;
        }

        setSlideNumber(newSlideNumber)       /* set SlideNumber by newSlideNumber */
    };

    const handleClick=() => {             //used to reserve the hotel
        if(user){
            setOpenModel(true);
        } else {
            navigate("/login");
        }
    }

    console.log("Dayes1",data)
    // console.log("Dayes2",data[0].address)
    // console.log("Dayes3",data[1])
    return (
        <div>
            <Navbar/>
            <Header type="list" />
            {loading ?
                ("loading "
                ) : (
                <>
                <div className="hotelContainer">
                {open && (
                        <div className="slider">
                    <FontAwesomeIcon icon={faCircleXmark} className="close" onClick={()=>setOpen(false)}/>
                    <FontAwesomeIcon icon={faCircleArrowLeft} className="arrow" onClick={()=>handleMove("l")}/>
                    <div className="sliderWrapper">
                        <img src={data.photos[slideNumber]} alt="" className="sliderImg" />
                    </div>
                    <FontAwesomeIcon icon={faCircleArrowRight} className="arrow" onClick={() => handleMove("r")} />
                    </div>
                    )}
                    <div className="hotelWrapper">
                        <button className="bookNow">
                            Reserve or Book Now!
                        </button>
                        <h1 className="hotelTitle">{data[1]} </h1>
                        <div className="hotelAddress">
                            <FontAwesomeIcon icon={faLocationDot} />
                            <span> {data.address}</span>
                        </div>
                        <span className="hotelDistance"> Excellent location {data.distance}m from center</span>
                        <span className="hotelPriceHighlight"> Book a stay over ${data.cheapestPrice} at this property and get a free airport taxi </span>
                        <div className="hotelImages">
                            {data.photos?.map((photo,i )=> (
                                <div className="hotelImgWrapper">
                                    <img onClick={()=>handleOpen(i)} src={photo} alt="" className="hotelImg" />
                                </div>
                            ))}
                        </div>
                        <div className="hotelDetails">
                            <div className="hotelDetailsTexts">
                                <h1 className="hotelTitle">{data.title}</h1>
                                <p className="hotelDesc">
                                    {data.desc}
                                </p>
                            </div>
                            <div className="hotelDetailsPrice">
                                <h1>Perfect for a {days}-night stay!</h1>
                                <span>
                                    Located in the real heart of Krakow, this property has an
                                    excellent location score of 9.8!
                                </span>
                                <h2>
                                    <b>${days * data.cheapestPrice * options.room}</b> ({days} nights)
                                </h2>
                                <button onClick={handleClick}> Reserve or Book Now!</button>
                            </div>
                        </div>
                    </div>
                    <MailList />
                    <Footer/>
                </div>
                </>
                )}
            {openModel && <Reserve setOpen={setOpenModel} hotelId={id}/>}
        </div>
    )
}

export default Hotel