import Header from './Header';
import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {faGithub, faLinkedin } from "@fortawesome/free-brands-svg-icons";
function Contact () {


    return (
        <main>
        <div className="contact-page">
            <Card style={{ width: '18rem' }}>
                <Card.Body>
                    <Card.Title>LinkedIn</Card.Title>
                    <Card.Text>
                        Connect with me on LinkedIn
                    </Card.Text>
                    <Button variant="primary" href="https://www.linkedin.com/in/bryan-bartell-1657b646/" target="_blank">
                        <FontAwesomeIcon icon={faLinkedin} /> LinkedIn Profile
                    </Button>
                </Card.Body>
            </Card>
            <Card style={{ width: '18rem' }}>
                <Card.Body>
                    <Card.Title>GitHub</Card.Title>
                    <Card.Text>
                        Check out my projects on GitHub.
                    </Card.Text>
                    <Button variant="secondary" href="https://github.com/BDubOne" target="_blank">
                        <FontAwesomeIcon icon={faGithub} /> GitHub Profile
                    </Button>
                </Card.Body>
            </Card>

        </div>
        </main>
    )
}


export default Contact