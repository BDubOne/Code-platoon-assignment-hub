

const Project = ({ title, description, imageUrl, techStack, link }) => {

    return (
        <div className="project-card">
            <img src={imageUrl} alt={`${title} screenshot`} className="project-image" />
            <h3>{title}</h3>
            <ul>
                {description.map((feature, idx)=> (
                    <li key={idx}>{feature}</li>
                ))}
            </ul>
            <ul className="tech-stack">
                {techStack.map(tech => (
                    <li key={tech}>{tech}</li>
                ))}
            </ul>
            <a href={link} target="_blank" rel="noopener noreferrer" className="project-link">View Project</a>
        </div>
    )
}

export default Project;