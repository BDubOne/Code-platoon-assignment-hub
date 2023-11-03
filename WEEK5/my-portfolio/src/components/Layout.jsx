import Header from './Header';
function Layout({ children}) {
    return (
        <>
        <Header title="Default Title" subtitle="Default Subtitle"/>
        <main>{children}</main>
        <footer>Default</footer>
        </>
    )
}

export default Layout