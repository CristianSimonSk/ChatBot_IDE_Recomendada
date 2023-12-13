<?php
session_start();

if (!isset($_SESSION['chat_messages'])) {
    $_SESSION['chat_messages'] = array();
    
}

// Função para adicionar uma nova mensagem ao chat
function adicionarMensagem($mensagem, $classe) {
    $_SESSION['chat_messages'][] = '<div class="message ' . $classe . '">' . $mensagem . '</div>';
}


// Verifica se a mensagem foi enviada
if (isset($_POST['btn-enviar'])) {
    if (isset($_POST['message'])) {
        $userMessage = $_POST['message'];

        file_put_contents("MensagemUser.txt", $userMessage);

        adicionarMensagem($userMessage, 'user-message');

        exec('/usr/bin/python3 /var/www/html/ChatBot_IDE_Recomendada/app.py');

        $botMessage = file_get_contents("MensagemBot.txt");

        adicionarMensagem($botMessage, 'bot-message');
    }
}

// Limpa o chat (session) quando o botão "Limpar Chat" é pressionado
if (isset($_POST['limpar_chat'])) {
    $_SESSION['chat_messages'] = array();
    unset($_SESSION['chat_messages']); // Remove a resposta da variável de sessão
}

?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Ide Recomendada</title>
    <script src='https://code.jquery.com/jquery-3.6.0.min.js'></script>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
        }

        .container {
            width: 600px;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            margin-bottom: 20px;
        }

        #chat-container {
            height: 200px;
            border: 1px solid #ccc;
            overflow-y: auto;
            padding: 10px;
            margin-bottom: 20px;
        }

        .message {
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
            clear: both;
        }

        .user-message {
            background-color: #e2f0cb;
            float: left;
            width: 50%;
        }

        .bot-message {
            background-color: #e5e5e5;
            float: right;
            width: 50%;
        }

        form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        button {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            color: #fff;
            cursor: pointer;
            font-size: 16px;
        }

        button[type="submit"] {
            background-color: #4CAF50;
            margin-bottom: 10px;
        }

        button[name="limpar_chat"] {
            background-color: #f44336;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Bem vindo ao Qual a IDE Recomendada</h1>
        <a>Sinta-se a vontate para conversar com o nosso bot que fará uma recomendação conforme a sua preferencia!!</a>

        <div id="chat-container">
            <?php
            // Exibe todas as mensagens armazenadas na variável de sessão se existir o cookie
            if (isset($_SESSION['chat_messages'])){
                foreach ($_SESSION['chat_messages'] as $message) {
                    echo $message;
                }
            }
            ?>
        </div>
        <form method="post" action="" id="chat-form">
            <input type="text" name="message" placeholder="Digite sua pergunta" id="message-input">
            <button type="submit" name="btn-enviar">Enviar</button>
            <button type="submit" name="limpar_chat">Limpar Chat</button>
        </form>
    </div>

    <script>
        
        var chatContainer = document.getElementById('chat-container');

        var messageInput = document.getElementById('message-input');

        chatContainer.scrollTop = chatContainer.scrollHeight;

        messageInput.focus();
    </script>
</body>
</html>
