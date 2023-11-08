import { Link } from 'react-router-dom'


const Header = () => {
    return (
        <>
        <h1></h1>
        <nav>
            <Link to="/">Home</Link>
            <Link to="about/">About</Link>
            <Link to="characters/">All Characters</Link>
            <Link to="acharacter/">A Character</Link>
        </nav>
        </>
    )
}

export default Header