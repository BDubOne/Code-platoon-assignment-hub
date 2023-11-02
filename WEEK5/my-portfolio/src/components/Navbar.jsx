import { useState } from 'react';

function Navbar() {
    const [activeSection, setActiveSection] = useState('home')

    return (
        <nav className="nav">
            <ul>
                <li>
                    <link to="/"
                    className={activeSection === 'home' ? 'active' : ''}
                    onClick={() => setActiveSection('home')}
                    >
                        Home
                    </link>
                </li>
                <li>
                    <link to="/about"
                    className={activeSection === 'about' ? 'active' : ''}
                    onClick={() => setActiveSection('about')}
                    >
                        About
                    </link>
                </li>
                <li>
                    <link to="/portfolio"
                    className={activeSection === 'portfolio' ? 'active' : ''}
                    onClick={() => setActiveSection('portfolio')}
                    >
                        Portfolio
                    </link>
                </li>
                <li>
                    <link to="/gratitude"
                    className={activeSection === 'gratitude' ? 'active' : ''}
                    onClick={() => setActiveSection('gratitude')}
                    >
                        Gratitude
                    </link>
                </li>
                <li>
                    <link to="/contact"
                    className={activeSection === 'contact' ? 'active' : ''}
                    onClick={() => setActiveSection('contact')}
                    >
                        Contact
                    </link>
                </li>
            </ul>
        </nav>

    );
}
export default Navbar