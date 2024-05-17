import { useEffect, useState } from "react"
import axios from "axios";


const useFetch = (url) => {
  const [data, setData] = useState([]); //fetched data from the API and is initialized as an empty array []
  const [loading, setLoading] = useState(false); //data is currently being fetched or not and is initialized as false.
  const [error, setError] = useState(false); //store any error that may occur during the data fetching process and is initialized as false.

  useEffect(() => {
    //The "useEffect" hook is used to perform the data fetching when the component mounts or whenever the url dependency changes
    const fetchData = async () => {
      //asynchronous function fetchData
      setLoading(true);
      try {
        const res = await axios.get(url);
        setData(res.data); //fetched data is stored in the data state using setData(res.data)
      } catch (err) {
        setError(err);
      }
      setLoading(false); //Regardless of success or error, setLoading(false) is called to indicate that the data fetching process is completed.
    };
    fetchData();
  }, [url]); // }, [url]);userFetch is depend on [url] uwhen using it.when we use [url], when we chngeing url, it's gonna refetch again.

  const reFetch = async () => {
    //reFetch function is defined to manually trigger the data fetching process again.
    setLoading(true);
    try {
      const res = await axios.get(url);
      setData(res.data);
    } catch (err) {
      setError(err);
    }
    setLoading(false);
  };

  return { data, loading, error, reFetch };
};

export default useFetch