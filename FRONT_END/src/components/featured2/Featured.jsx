import useFetch from "../../hooks/useFetch"
import "./featured.css"

const Featured2 = () => {

    return (
        <div className="featured">
                <div className="featuredItem">
                <img
                    src="https://www.intltravelnews.com/sites/default/files/20200317msrse-b.jpg"
                    alt=""
                    className="featuredImg"
                />
                <div className="featuredTitles">
                    <h1> Bristol</h1>
                    <h2> 100 Rooms</h2>
                </div>
                </div>
                <div className="featuredItem">
                    <img
                        src="https://th.bing.com/th/id/R.59c6d1d9a7ece1a10c339a49b2b81a4c?rik=otIf1tKvJnnKEg&pid=ImgRaw&r=0"
                        alt=""
                        className="featuredImg"
                    />
                    <div className="featuredTitles">
                        <h1> Cardiff</h1>
                        <h2> 90 Rooms</h2>
                    </div>
                </div>
                <div className="featuredItem">
                    <img
                        src="https://th.bing.com/th/id/OIP.QEiwrDDVB8uI9BNyP-XKDQHaE8?rs=1&pid=ImgDetMain"
                        alt=""
                        className="featuredImg"
                    />
                    <div className="featuredTitles">
                        <h1> Edinburgh</h1>
                        <h2> 120 Rooms</h2>
                    </div>
                    </div>
        </div>
    )
}

export default Featured2;