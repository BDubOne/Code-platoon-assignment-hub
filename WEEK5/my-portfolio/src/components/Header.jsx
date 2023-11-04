
function Header ({ title, subtitle, children}) {
    return (
        <div className ="background">
            <h1 id="title">
                {title}
                </h1>
                <div className="content">
                    <h2 id="sub-title">
                        {subtitle}
                    </h2>
                    <div id="content">
                        {children}
                    </div>
                </div>
        </div>
    );
}

export default Header