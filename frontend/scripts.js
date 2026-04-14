
let board = Array(9).fill('');
let currentPlayer = 'X';

const turnInfo = document.getElementById('turn-info');
const winnerDisplay = document.getElementById('winner-info');

const resetGame = () => {
    fetch('/reset', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        board = data.board;
        currentPlayer = 'X';
        turnInfo.textContent = 'Turn: X';
        winnerDisplay.textContent = '';
        document.querySelectorAll('.cell').forEach(cell => {
            cell.textContent = '';
            cell.disabled = false;
        });
    });
}

const makeMove = (row, col, btn) => {
    if (btn.textContent !== '') return;

    const index = row * 3 + col;
    board[index] = currentPlayer;
    btn.textContent = currentPlayer;
    btn.disabled = true;
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    turnInfo.textContent = `Turn: ${currentPlayer}`;

    fetch('/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ board })
    })
    .then(response => response.json())
    .then(data => {
        if (data.winner) {
            winnerDisplay.textContent = `Winner: ${data.winner}`;
            turnInfo.textContent = '';
            document.querySelectorAll('.cell').forEach(cell => cell.disabled = true);
        }
    });
}
