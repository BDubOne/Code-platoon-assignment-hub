
import { Link } from "react-router-dom"

import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

function NavBar() {
  return (
    <Navbar expand="lg" className="bg-body-tertiary">
      <Container>
        <Navbar.Brand>LVX-Gematria</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link to="/">Home</Nav.Link>
            <Nav.Link to="global-dictionary/">Global Dictionary</Nav.Link>
            <Nav.Link to="personal-dictionary/">Personal Dictionary</Nav.Link>
            <Nav.Link to="calculator/">LVX Calculator</Nav.Link>
            <Nav.Link to="about/">About</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavBar;

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