import Header from './Header';


function Portfolio() {
    return (
        <Header title="Portfolio" subtitle="Some of my recent projects">
            <div className="project-table">
                {Array(6).fill().map((_, index) => (
                    <div key={index} classname="project-item">
                        <img src="#" alt={`Project ${index + 1}`}/>
                        <p> Project {index + 1} Description</p>
            </div>
                ))}
            </div>
        </Header>
    );
}

export default Portfolio;