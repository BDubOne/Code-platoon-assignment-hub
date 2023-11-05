import Header from './Header';
import Project from './Project';


const projects = [
    {
    title: "Task Manager",
    description: ["This is a simple task-manager app.","Create a Task.","View Tasks.", "Mark Complete.","Remove a Task.", "Features for tracking and timebanking coming soon!"],
    imageUrl: "./src/assets/task-manager-screenshot.png",
    techStack: ['HTML', 'CSS', 'JavaScript', 'React'],
    link: 'https://bejewelled-pothos-3e6957.netlify.app/'
    

},
{
    title: "Whack a Mole",
    description: ["This is a simple task-manager app.","Create a Task.","View Tasks.", "Mark Complete.","Remove a Task.", "Features for tracking and timebanking coming soon!"],
    imageUrl: "./src/assets/whack-a-mole.png",
    techStack: ['HTML', 'CSS', 'JavaScript', 'React'],
    link: 'https://iridescent-lebkuchen-d27d22.netlify.app/'
    

}
];


function Portfolio() {
    return (
       <div className="portfolio">
            <h2>Portfolio</h2>
            <div className="project-list">
                {projects.map((project, idx) => (
                    <Project key={idx} {...project} />

                ))}               
            </div>
       </div>
    );
}

export default Portfolio;