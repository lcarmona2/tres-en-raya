
let currentPlayer = 'X';

const resetGame = () => {
    fetch('/reset', { method: 'POST' })
    .then(response => response.json())
    .then(() => {
        currentPlayer = 'X';
        document.querySelectorAll('.cell').forEach(cell => {
            cell.textContent = '';
            cell.disabled = false;
        });
    });
}

const turnInfo = document.getElementById('turn-info');

const makeMove = (row, col, btn) => {
    if (btn.textContent !== '') return; // celda ya marcada

    btn.textContent = currentPlayer;
    btn.disabled = true;
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    turnInfo.textContent = `Turn: ${currentPlayer}`;

    fetch('/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ row, col })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });
    checkWinner();
}

const winnerDisplay = document.getElementById('winner-info');
const checkWinner = () => {
    fetch('/winner')
    .then(response => response.json())
    .then(data => {
        if (data.winner) {
            winnerDisplay.textContent = `Winner: ${data.winner}`;
        }
    });
}

