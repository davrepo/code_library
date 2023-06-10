function Nav(props) {
    return (
        <nav className="main-nav">
            <ul>
                <li>{props.name}'s Home</li>
                <li>Contact</li>
            </ul>
        </nav>
    );
};

export default Nav;