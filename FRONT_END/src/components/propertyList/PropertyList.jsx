import useFetch from "../../hooks/useFetch";
import React, { useEffect } from 'react';
import "./propertyList.css";

const PropertyList = () => {
  const { data, loading, error } = useFetch("/hotels/countByType");

  const generateQRCode = (text) => {
    const qrCodeUrl = `https://quickchart.io/qr?size=200&text=${encodeURIComponent(text)}`;
    const img = document.createElement('img');
    img.src = qrCodeUrl;
    const qrdiv = document.getElementById('qr-code');
    qrdiv.innerHTML = "";
    qrdiv.appendChild(img);
  }

  useEffect(() => {
    // The text to be encoded in the QR code
    const textToEncode = "Hello, this is a sample text!";// this should be vehicle reg no
    generateQRCode(textToEncode);
  }, []);


  return (

    <div className="user-row">
      <div className="qr-div">
        <h3>Your QR Code</h3>
        <div id="qr-code">

        </div>
      </div>

  
      <div className="user-details">
        <h3>Username</h3>
        <p>username</p>
        <h3>Name</h3>
        <p>name</p>
        <h3>Email</h3>
        <p>email</p>
        <h3>Mobile</h3>
        <p>mobile</p>
        <h3>Vehicle Reg No</h3>
        <p>Vehicle Reg No</p>
      </div>
    </div>
    
  );
};

export default PropertyList;