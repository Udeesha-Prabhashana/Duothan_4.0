import Navbar from "../../components/navbar/Navbar";
import Header from "../../components/header/Header";
import Featured from "../../components/featured/Featured";
import PropertyList from "../../components/propertyList/PropertyList";
import "./home.css"
import FeaturesProperties from "../../components/featuredProperties/FeaturedProperties";
import MailList from "../../components/MailList/MailList";
import Footer from "../../components/footer/Footer";
import Featured2 from "../../components/featured2/Featured";

const Home = () => {
    return (
        <div>
            <Navbar />
            <Header />
            <div className="homeContainer">
                <h1 className="homeTitle"> Cities</h1> 
                <Featured />
                <Featured2 />
                <h1 className="homeTitle"> Brows by properties</h1>
                <PropertyList />
                {/* <h1 className="homeTitle"> home guest love</h1>
                <FeaturesProperties /> */}
                <MailList />
                <Footer/>
            </div>
        </div>

    );
};

export default Home