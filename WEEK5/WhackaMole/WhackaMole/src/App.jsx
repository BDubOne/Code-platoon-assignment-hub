import React, { useState, useRef } from 'react';

function WhackaMole() {
  const [selectedBox, setSelectedBox] = useState(null);
  const [points, setPoints] = useState(0);
  const [gameStarted, setGameStarted] = useState(false);
  const gameInterval = useRef(null);

  const startGame = () => {
    if (gameInterval.current) {
      clearInterval(gameInterval.current);
    }

    setGameStarted(!gameStarted);

    gameInterval.current = setInterval(() => {
      const randomBoxIndex = Math.floor(Math.random() * 9);
      setSelectedBox(randomBoxIndex);
    }, 1000);

    setTimeout(() => {
      clearInterval(gameInterval.current);
    }, 30000);
  };

  const handleBoxClick = () => {
    if (selectedBox !== null) {
      setPoints((prevPoints) => prevPoints + 1);
    }
  };

  const renderTable = () => {
    if (gameStarted) {
      const tableRows = [];
      for (let row = 0; row < 3; row++) {
        const cells = [];
        for (let col = 0; col < 3; col++) {
          const boxIndex = row * 3 + col;
          const isBoxSelected = boxIndex === selectedBox;

          cells.push(
            <td
              key={col}
              onClick={() => handleBoxClick(boxIndex)}
              className={isBoxSelected ? 'selected-box' : ''}
            >
              {isBoxSelected ? 'Click me!' : ''}
            </td>
          );
        }
        tableRows.push(<tr key={row}>{cells}</tr>);
      }

      return (
        <table>
          <tbody>{tableRows}</tbody>
        </table>
      );
    } else {
      return (
        <button onClick={startGame}>Start</button>
      );
    }
  };

  return (
    <>
      <h1>WhackaMole</h1>
      {renderTable()}
      <p>Points: {points}</p>
    </>
  );
}

export default WhackaMole;
