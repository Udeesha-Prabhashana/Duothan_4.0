import "./sidebar.scss";
import DashboardIcon from '@mui/icons-material/Dashboard';          //SvgIcon components. It depends on @mui/material, which requires Emotion packages
import Person2OutlinedIcon from '@mui/icons-material/Person2Outlined';
import LocalShippingIcon from "@mui/icons-material/LocalShipping";
import CreditCardIcon from "@mui/icons-material/CreditCard";
import StoreIcon from "@mui/icons-material/Store";
import InsertChartIcon from "@mui/icons-material/InsertChart";
import SettingsApplicationsIcon from "@mui/icons-material/SettingsApplications";
import ExitToAppIcon from "@mui/icons-material/ExitToApp";
import NotificationsNoneIcon from "@mui/icons-material/NotificationsNone";
import SettingsSystemDaydreamOutlinedIcon from "@mui/icons-material/SettingsSystemDaydreamOutlined";
import PsychologyOutlinedIcon from "@mui/icons-material/PsychologyOutlined";
import AccountCircleOutlinedIcon from "@mui/icons-material/AccountCircleOutlined";
import { Link } from "react-router-dom";
import { DarkModeContext } from "../../context/darkModeContext";
import { useContext } from "react";
import { useNavigate } from "react-router-dom";

const Sidebar = () => {

    const navigate = useNavigate();
    const { dispatch } = useContext(DarkModeContext);

    return (
        <div className="Sidebar">
            <div className="top">

                  <span className="logo">Neotropolis</span>
            </div>
            <hr/>         {/*  hr use to get line */}
            <div className="center">
                <ul>
                    <p className="title">MAIN</p>
                    <Link to="/adminhome">
                    <li>
                        <DashboardIcon className="icon" />
                        <span> Dashboard</span>
                    </li>    
                    </Link>
                    <p className="title">LIST</p>
                    <Link to="/users" style={{ textDecoration: "none"}}>
                    {/* <li>
                        <Person2OutlinedIcon className="icon" />
                        <span> Users </span>
                    </li> */}
                    </Link>
                    <Link to="/customers" style={{ textDecoration: "none" }}>    
                    <li>
                        <Person2OutlinedIcon className="icon" />
                        <span> Costomers</span>
                    </li>                
                    </Link>
                    <Link to="/rooms" style={{ textDecoration: "none" }}>
                    <li>
                        <LocalShippingIcon className="icon" />
                        <span> Vehicals</span>
                    </li>
                    </Link>
                    <Link to="/locations" style={{ textDecoration: "none" }}>
                    <li>
                        <CreditCardIcon className="icon" />
                        <span> Locations</span>
                    </li>
                    </Link>
                    <p className="title">USEFUL</p>
                    <li>
                        <NotificationsNoneIcon className="icon" />
                        <span> Notification</span>
                    </li>
                    <li>
                        <InsertChartIcon className="icon" />
                        <span> Stats</span>
                    </li>
                    <p className="title">SERVICE</p>
                    <li>
                        <SettingsSystemDaydreamOutlinedIcon className="icon" />
                        <span> System Health</span>
                    </li>
                    <li>
                        <PsychologyOutlinedIcon className="icon" />
                        <span> Logs</span>
                    </li>
                    <li>
                        <SettingsApplicationsIcon className="icon" />
                        <span> Setting</span>
                    </li>
                    <p className="title">USER</p>
                    <li>
                        <AccountCircleOutlinedIcon className="icon" />
                        <span> Profile</span>
                    </li>
                    <li>
                        <ExitToAppIcon className="icon" />
                        <span onClick = {() => navigate("/login")}> Logout</span>
                    </li>
                </ul>
            </div>
            <div className="bottom">      {/*give chose color options in dashbord*/}
                <div className="colorOption" onClick={()=> dispatch({type:"LIGHT"})}></div>       
                <div className="colorOption" onClick={()=> dispatch({type:"DARK"})}></div>
            </div>
        </div>
    )
}


export default Sidebar