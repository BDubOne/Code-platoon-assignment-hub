import App from '../App'
import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'



const CharacterCard = ({name, image, species}) => {

   return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src={image} />
      <Card.Body>
        <Card.Title>{name}</Card.Title>
        <Card.Text>
          Species: {species}
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
    </Card>
  );
}

export default CharacterCard
