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
                <Featured />
                <PropertyList />
              
                {/* <MailList /> */}
                {/* <Footer/> */}
            </div>
        </div>

    );
};

export default Home