import Row from "react-bootstrap/Row"
import { useEffect, useState } from 'react';
import axios from 'axios'

export const Moves=()=>{

    const [moves, setMoves] = useState([]);

    const getAllMoves = async () => {
        let response = await axios
        .get("http://127.0.0.1:8000/api/v1/moves/")
        .catch((err) => {
            console.log(err);
            alert("something went wrong");
        });
        setMoves(response.data)
    };
    useEffect(() => {
        getAllMoves();
        console.log(moves)
    }, [])
    return(
        <Row style={{padding: "0 10vmin"}}>
            <h1 style={{textAlign: "center" }}>Moves</h1>
            <ul>
                {moves.map((move) => (
                    <li key={move.id}
                    style={{
                        margin: "3vmin",
                        display: "flex",
                        flexDirection: "column",
                    }}
                    >
                        Name: {move.name} <br /> Power: {move.power} <br /> Accuracy: {move.accuracy} <br />
                        <ul>
                            pokemon
                            {move.pokemon.map((poke, idx) => (
                                <li key={`${move.id}${idx}`}>{poke}</li>
                            ))}
                        </ul>
                    </li>
                ))}
            </ul>
        </Row>


    );
};