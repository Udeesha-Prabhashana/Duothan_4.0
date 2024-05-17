import useFetch from "../../hooks/useFetch"
import "./featured.css"

const Featured = () => {

    return (
        <div className="featured">
                <div className="featuredItem">
                <img
                    src="https://files.oursocalledlife.co.uk/wp-content/uploads/2020/03/12114248/IMG_3917-1-1536x1152.jpg"
                    alt=""
                    className="featuredImg"
                />
                <div className="featuredTitles">
                    <h1> Aberdeen</h1>
                    <h2> 90 Rooms</h2>
                </div>
                </div>
                <div className="featuredItem">
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
                    </div>
        </div>
    )
}

export default Featured;