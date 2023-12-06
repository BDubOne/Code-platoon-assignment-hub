import Row from "react-bootstrap/Row"
import { Link } from "react-router-dom"

const Navbar = () => {
    return (
        <>
        <Row>
            <Link to="/">Home</Link>
            <Link to="Register/">Register</Link>
            <Link to="Pokemon/">Pokemon</Link>
            <Link to="Moves/">Moves</Link>
        </Row>
        </>
    )
}
export default Navbar