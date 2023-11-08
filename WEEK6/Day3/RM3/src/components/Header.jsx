
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom'

export const Header = () => {
    return (
        <>
    <Navbar bg="dark" data-bs-theme="dark"expand="lg" className="bg-body-tertiary">
    <Container>
      <Navbar.Brand as={Link} to="/">Rick and Morty</Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="me-auto">
          <Nav.Link as={Link} to="about/">About</Nav.Link>   
          <Nav.Link as={Link} to="characters/">Characters</Nav.Link>
            
        </Nav>
      </Navbar.Collapse>
    </Container>
  </Navbar>
  </>
);
}

