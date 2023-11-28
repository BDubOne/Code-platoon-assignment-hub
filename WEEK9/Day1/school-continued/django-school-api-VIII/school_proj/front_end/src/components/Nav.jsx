
import { Link } from 'react-router-dom'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Container from 'react-bootstrap/Container'

const NavBar = () => {
    return (
       
        <Navbar id="NavBar" expand="lg" className="bg-body-tertiary NavBar">
            <Container>
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="pl-4 pr-4">
                        <Link to="/">Home</Link>
                        <Link to="students/">Students</Link>
                        <Link to="subjects/">Subjects</Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
   
    )
}
export default NavBar