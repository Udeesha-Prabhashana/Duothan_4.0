import useFetch from "../../hooks/useFetch"
import "./featured.css"

const Featured = () => {

    

    return (
        <div className="featured">

                <h1>Welcome user</h1>
                
                <div className="featuredItem">

                    <div className="ticket">
                        <div className="ticket-content">
                            <div className="ticket-id">
                                <h2>Ticket ID: </h2>
                                <h1 className="ticketid">T035</h1>

                            </div>
                            <h3 className="username">User name</h3>
                        </div>

                        <div className="ticket-logo">
                            <h1>Neotripolis Parkingslot</h1>
                        </div>
                        
                    </div>


            



                </div>
                {/* <div className="featuredItem">
                    <img
                        src="https://cf.bstatic.com/xdata/images/city/max500/690334.webp?k=b99df435f06a15a1568ddd5f55d239507c0156985577681ab91274f917af6dbb&o="
                        alt=""
                        className="featuredImg"
                    />
                    <div className="featuredTitles">
                        <h1> Belfast</h1>
                        <h2> 80 Rooms</h2>
                    </div>
                </div>
                <div className="featuredItem">
                    <img
                        src="https://th.bing.com/th/id/OIP.2KxuVJzNj_-QRQ-35rmEKwHaFE?rs=1&pid=ImgDetMain"
                        alt=""
                        className="featuredImg"
                    />
                    <div className="featuredTitles">
                        <h1> Birmingham</h1>
                        <h2> 110 properties</h2>
                    </div>
                    </div> */}
        </div>
    )
}

export default Featured;