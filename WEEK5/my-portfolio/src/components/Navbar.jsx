
import { Link, NavLink } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropDown from 'react-bootstrap/NavDropDown';

function Navbars() {
  

    return (
        <Navbar fixed="top" expand='lg' className="bg-body-tertiary">
            <Container>
                
                <Navbar.Brand as= {Link} to="/">Bryan Bartell</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">      
                        <Nav.Link as={NavLink} to="/">
                            Home
                        </Nav.Link>
                        <Nav.Link as={NavLink} to="/about">
                            About
                        </Nav.Link>
                        <Nav.Link as={NavLink} to="/gratitude">
                            Gratitude
                        </Nav.Link>
                        <NavDropDown title="Portfolio" id="basic-nav-dropdown">
                            <NavDropDown.Item as={Link} to="/portfolio">
                                All Projects
                            </NavDropDown.Item>
                            <NavDropDown.Item as={Link} to="/task-manager">
                                Task Manager
                            </NavDropDown.Item>
                            <NavDropDown.Item as={Link} to="/whackamole">
                                Whack a Mole
                            </NavDropDown.Item>
                            
                        </NavDropDown>
                        <Nav.Link as={NavLink} to="/contact">
                            Contact
                        </Nav.Link>
                    
                     
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>

    );
}
export default Navbars