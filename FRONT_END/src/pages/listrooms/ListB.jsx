import "./list.scss";
import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbarA/NavbarA";
import Datatable2 from "../../components/datatableroom/Datatable";

const List = ({columns}) => {
    return (
        <div className="list2">
            <Sidebar />
            <div className="listContainer2">
                <Navbar />
                <Datatable2 columns={columns} />
            </div>
        </div>
    )
}

export default List