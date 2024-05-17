import "./list.scss";
import Sidebar from "../../components/sidebar/Sidebar";
import Navbar from "../../components/navbarA/NavbarA";
import Datatable from "../../components/datatable/Datatable";

const List = ({columns}) => {
    return (
        <div className="list2">
            <Sidebar />
            <div className="listContainer2">
                <Navbar />
                <Datatable columns={columns} />
            </div>
        </div>
    )
}

export default List