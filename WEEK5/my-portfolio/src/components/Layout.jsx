import Header from './Header';
import NavBars from './Navbar';

function Layout({ title, subtitle, children}) {
    return (
        <>
        <NavBars />
        <Header title= {title} subtitle = {subtitle} />
        <main>
            {children}
        </main>
        <footer>
            <p>
                Created By  
                <a href="mailto:bryan.t.bartell@gmail.com"> Bryan Bartell </a> 
                2023
            </p>
        </footer>
        </>
    )
}

export default Layout