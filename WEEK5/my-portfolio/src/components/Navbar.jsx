import { useState } from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
    const [activeSection, setActiveSection] = useState('home')

    return (
        <nav className="nav">
            <ul>
                <li>
                    <Link to="/"
                    className={activeSection === 'home' ? 'active' : ''}
                    onClick={() => setActiveSection('home')}
                    >
                        Home
                    </Link>
                </li>
                <li>
                    <Link to="/about"
                    className={activeSection === 'about' ? 'active' : ''}
                    onClick={() => setActiveSection('about')}
                    >
                        About
                    </Link>
                </li>
                <li>
                    <Link to="/portfolio"
                    className={activeSection === 'portfolio' ? 'active' : ''}
                    onClick={() => setActiveSection('portfolio')}
                    >
                        Portfolio
                    </Link>
                </li>
                <li>
                    <Link to="/gratitude"
                    className={activeSection === 'gratitude' ? 'active' : ''}
                    onClick={() => setActiveSection('gratitude')}
                    >
                        Gratitude
                    </Link>
                </li>
                <li>
                    <Link to="/contact"
                    className={activeSection === 'contact' ? 'active' : ''}
                    onClick={() => setActiveSection('contact')}
                    >
                        Contact
                    </Link>
                </li>
            </ul>
        </nav>

    );
}
export default Navbar