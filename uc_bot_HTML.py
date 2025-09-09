<!DOCTYPE html>
<html>
<head>
    <title>UC o‘yini</title>
    <style>
        body {
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: #222;
            color: #fff;
            flex-direction: column;
            font-family: Arial, sans-serif;
        }
        #gameArea {
            width: 300px;
            height: 500px;
            background: #444;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            font-size: 24px;
            border-radius: 15px;
            user-select: none;
        }
        #scoreDisplay {
            margin-top: 20px;
            font-size: 20px;
        }
    </style>
</head>
<body>
    <div id="gameArea">UC uchun bos!</div>
    <div id="scoreDisplay">Ball: <span id="score">0</span></div>

    <script>
        let score = 0;
        const scoreEl = document.getElementById('score');
        const gameArea = document.getElementById('gameArea');

        gameArea.addEventListener('click', () => {
            score += 1;
            scoreEl.innerText = score;
        });
    </script>
</body>
</html>
