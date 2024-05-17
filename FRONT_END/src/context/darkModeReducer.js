const DarkModeReducer = (state, action) => {
    switch (
      action.type //"action.type" represent which action want to change, besically it represent some switch case.
    ) {
      case "LIGHT": {
        return {
          darkMode: false,
        };
      }
      case "DARK": {
        return {
          darkMode: true,
        };
      }
      case "TOGGLE": {
        return {
          darkMode: !state.darkMode,
        };
        }
    default:
        return state;
    }
}

export default DarkModeReducer;
//"state" represent which state we want to chane when changing action