
function Header ({ title, subtitle, children }) {
    return (
        <div className ="background">
            <div className="foreground">
                <h1 id="title">
                    {title}
                </h1>
             
                    <h2 id="sub-title">
                        {subtitle}
                    </h2>                
            </div>
        </div>
    );
}

export default Header