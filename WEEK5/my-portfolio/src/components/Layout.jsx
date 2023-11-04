import Header from './Header';
import NavBars from './Navbar';

function Layout({ title, subtitle, children}) {
    return (
        <>
        <NavBars />
        <Header title= {title} subtitle = {subtitle} />
        <main>{children}</main>
        <footer>Default Footer</footer>
        </>
    )
}

export default Layout