import React, { useState, useEffect } from 'react';
import Board from './Board';
import './App.css';

function App() {
  const [board, setBoard] = useState(Array(9).fill(null));
  const [isGameOver, setIsGameOver] = useState(false);
  const [status, setStatus] = useState('Loading...');

  // Effect to load the initial state when the component mounts
  useEffect(() => {
    handleReset();
  }, []);

  function handleSquareClick(i) {
    // Ignore clicks if the game is over or the square is already filled
    if (isGameOver || board[i]) {
      return;
    }

    fetch('http://localhost:5000/api/move', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ location: i }),
    })
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        console.error(data.error); // Log errors from the backend
        return;
      }
      setBoard(data.board);
      if (data.winner) {
        setStatus(`Winner: ${data.winner}`);
        setIsGameOver(true);
      } else if (data.is_draw) {
        setStatus('Draw');
        setIsGameOver(true);
      } else {
        setStatus(`Next player: ${data.current_player}`);
      }
    });
  }

  // Resets the game to the initial state
  function handleReset() {
    fetch('http://localhost:5000/api/reset', { method: 'POST' })
      .then(res => res.json())
      .then(data => {
        setBoard(data.board);
        setStatus(`Next player: ${data.current_player}`);
        setIsGameOver(false);
      });
  }

  return (
    <div className="game">
      <div className="game-board">
        <Board board={board} status={status} onSquareClick={handleSquareClick} />
      </div>
      <div className="game-info">
        <button onClick={handleReset}>Reset Game</button>
      </div>
    </div>
  );
}

export default App;