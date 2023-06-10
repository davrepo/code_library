import { useState } from "react";

function ModeToggler() {
    // Hooks can only be called from React function components, not regular Javascript functions
    // Hooks can be called only from the top level of a function component
    // Cannot call hooks inside loops or conditions
    const [darkModeOn, setDarkModeOn] = useState(true);
    
    const darkMode = <h1 style={{color: "black"}}>Dark Mode</h1>;
    const lightMode = <h1 style={{color: "grey"}}>Light Mode</h1>;

    function handleClick() {
        setDarkModeOn(!darkModeOn);
    }

    return (
        <div>
            {darkModeOn ? darkMode : lightMode}
            <button onClick={handleClick}>Toggle Mode</button>
        </div>
    );
}

export default ModeToggler;