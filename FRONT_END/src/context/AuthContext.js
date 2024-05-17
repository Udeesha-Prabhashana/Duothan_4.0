import { createContext, useEffect, useReducer } from "react";  //useful when you have data that needs to be accessed by multiple components at different levels in your React component tree.

const getStoredUser = () => {            //retrieve the user data from the localStorage
  try {
    const storedUser = localStorage.getItem("user");
    return storedUser ? JSON.parse(storedUser) : null; //JSON.parse function is used to parse the retrieved value
  } catch (error) {
    // console.error("Error parsing stored user data:", error);
    return null;
  }
};

const INITIAL_STATE = {
  user: getStoredUser(), //JSON.parse(localStorage.getItem("user")) || null,
  loading: false, //application is in a loading state .
  error: null,
};

export const AuthContext = createContext(INITIAL_STATE);   //used to store and share the state related to user authentication across various components in the application.

const AuthReducer = (state, action) => {      //state (representing the current state) and action (representing the type of action dispatched to update the state)
  switch (action.type) {
    case "LOGIN_START":
      return {
        user: null,
        loading: true, //waiting for the API response
        error: null,
      };
    case "LOGIN_SUCCESS":
      return {        
        user: action.payload,
        loading: false,
        error: null,
      };
    case "LOGIN_FAILURE":
      return {
        user: null,
        loading: false,
        error: action.payload,
      };
    case "LOGOUT":
      return {
        user: null,
        loading: false,
        error: null,
      };
    default:
      return state;
  }
};

export const AuthContextProvider = ({ children }) => {    //"AuthContextProvider" component of the application to enable state management with the "AuthContext" and "AuthReducer".
  const [state, dispatch] = useReducer(AuthReducer, INITIAL_STATE); //"useReducer" hook is used to manage the state within the "AuthContextProvider"


  useEffect(() => {          //useEffect hook is used to automatically update the localStorage whenever the state.user changes
    localStorage.setItem("user", JSON.stringify(state.user));
  }, [state.user]);

  return (
    <AuthContext.Provider
      value={{
        user: state.user,
        loading: state.loading,
        error: state.error,
        dispatch,                       //dispatch is a function, it can use to bring the data through the any root
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};                           //Overall, this code sets up an authentication context using React's context API and manages the state related to user authentication using the useReducer hook. It provides a convenient way to share authentication state across different components in the application and persists the user data in localStorage for a seamless user experience.