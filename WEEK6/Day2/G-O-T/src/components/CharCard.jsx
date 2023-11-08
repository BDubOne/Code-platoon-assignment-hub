import Button from 'react-bootstrap/Button'
import Card from 'react-bootstrap/Card'
import { Link, useNavigate } from 'react-router-dom'


function CharCard ({id, name, image}) {
    const navigate = useNavigate()
    return (
        <Card style={{width: '18rem'}}>
            <Card.Img variant="top" src={image} />
            <Card.Body>
                <Card.Title>{name}</Card.Title>
                <Button variant="primary" onclick={()=>navigate(`/character/${id}/`)}>Go someWhere</Button>
            </Card.Body>
        </Card>
    )

}
export default CharCard