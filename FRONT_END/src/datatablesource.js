export const userColumns = [
  { field: "id", headerName: "ID", width: 70 },
  {
    field: "user",
    headerName: "User",
    width: 230,
    renderCell: (params) => {
      return (
        <div className="cellWithImg">
          <img
            className="cellImg"
            src={params.row.img || "https://i.ibb.co/MBtjqXQ/no-avatar.gif"}
            alt="avatar"
          />
          {params.row.username}
        </div>
      );
    },
  },
  {
    field: "email",
    headerName: "Email",
    width: 230,
  },

  {
    field: "city",
    headerName: "City",
    width: 100,
  },
  {
    field: "phone",
    headerName: "Phone",
    width: 100,
  },
  {
    field: "country",
    headerName: "Country",
    width: 100,
  },

];

export const usersColumns = [
  { field: "customer_id", headerName: "ID", width: 250 },
  {
    field: "dtp_id",
    headerName: "DTP_NO",
    width: 150,
  },
  {
    field: "name",
    headerName: "Name",
    width: 100,
  },
  {
    field: "email",
    headerName: "E-mail",
    width: 230,
  },
  {
    field: "contact_no",
    headerName: "contact_no",
    width: 100,
  },
];

export const roomColumns = [
  { field: "room_id", headerName: "ID", width: 70 },
  {
    field: "title",
    headerName: "Title",
    width: 230,
  },
  {
    field: "facilities",
    headerName: "Description",
    width: 200,
  },
  {
    field: "price",
    headerName: "Price",
    width: 100,
  },
  {
    field: "maxPeople",
    headerName: "Max People",
    width: 100,
  },
];
