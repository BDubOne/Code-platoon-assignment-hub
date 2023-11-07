import Carousel from 'react-bootstrap/Carousel';

const EpisodeCarousel = ({ episodes }) => {
    return (
        <Carousel>
            {episodes.map((episode, idx) => (
                <Carousel.Item key={idx}>
                    <img className="d-block w-100"
                    src={episode.backgroundImage}
                    alt={episode.title}
                    />
                    <Carousel.Caption>
                        <h3>{episode.title}</h3>
                        <p>Release Date: {episode.releaseDate}</p>
                        <p>Episode Number: {episode.episodeNumber}</p>                        
                    </Carousel.Caption>
                </Carousel.Item>
            ))}
        </Carousel>
    )
}
export default EpisodeCarousel;