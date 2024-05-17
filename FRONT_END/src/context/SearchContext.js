import { createContext, useReducer } from "react";  //useful when you have data that needs to be accessed by multiple components at different levels in your React component tree.

const INITIAL_STATE = {
  city: undefined,
  dates: [],
  options: {
    adult: undefined,
    children: undefined,
    room: undefined,
  },
};

export const SearchContext = createContext(INITIAL_STATE);

const SearchReducer = (state, action) => {
  switch (action.type) {
    case "NEW_SEARCH":
      return action.payload;
    case "RESET_SEARCH": //This case resets the state to the INITIAL_STATE
      return INITIAL_STATE;
    default:
      return state;
  }
};

export const SearchContextProvider = ({ children }) => {    //"SearchContextProvider" component of the application to enable state management with the "SearchContext" and "SearchReducer".
  const [state, dispatch] = useReducer(SearchReducer, INITIAL_STATE); //"useReducer" hook is used to manage the state within the "SearchContextProvider"

  return (
    <SearchContext.Provider
      value={{
        city: state.city,
        dates: state.dates,
        options: state.options,
        dispatch,
      }}
    >
      {children}
    </SearchContext.Provider>
  );
};