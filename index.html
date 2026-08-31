<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevQuest - TaskTracker Gamificado</title>
    <style>
        /* Estilo Dark RPG Futurista (Neon Cyberpunk) */
        :root {
            --bg-color: #0d0e15;
            --card-bg: #151824;
            --text-color: #f0f2f5;
            --neon-purple: #9d4edd;
            --neon-cyan: #00f5d4;
            --neon-pink: #ff007f;
            --low-priority: #3a86ff;
            --medium-priority: #ffbe0b;
            --high-priority: #ff006e;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .container {
            width: 100%;
            max-width: 800px;
            background: var(--card-bg);
            border-radius: 12px;
            border: 2px solid var(--neon-purple);
            box-shadow: 0 0 20px rgba(157, 78, 221, 0.2);
            padding: 30px;
            display: none; /* Controlado via JS */
        }

        /* Tela de Autenticação (Login/Cadastro) */
        .auth-container {
            width: 100%;
            max-width: 400px;
            background: var(--card-bg);
            border-radius: 12px;
            border: 2px solid var(--neon-cyan);
            box-shadow: 0 0 20px rgba(0, 245, 212, 0.15);
            padding: 30px;
            text-align: center;
        }

        h1 {
            color: var(--neon-cyan);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 5px;
            text-shadow: 0 0 10px rgba(0, 245, 212, 0.4);
        }

        h2 {
            color: var(--neon-purple);
            text-transform: uppercase;
            font-size: 1.2rem;
            margin-bottom: 20px;
        }

        .subtitle {
            color: #8b8f9e;
            margin-bottom: 30px;
            font-size: 0.95rem;
        }

        /* Inputs e Formulários */
        .input-group {
            margin-bottom: 15px;
            text-align: left;
        }

        .input-group label {
            display: block;
            margin-bottom: 5px;
            font-size: 0.85rem;
            color: #8b8f9e;
            text-transform: uppercase;
        }

        input[type="text"], input[type="password"], select {
            width: 100%;
            box-sizing: border-box;
            background: #1c2030;
            border: 1px solid #32384e;
            color: var(--text-color);
            padding: 12px 15px;
            border-radius: 6px;
            font-size: 1rem;
            outline: none;
            transition: 0.3s;
        }

        input[type="text"]:focus, input[type="password"]:focus, select:focus {
            border-color: var(--neon-cyan);
            box-shadow: 0 0 8px rgba(0, 245, 212, 0.3);
        }

        /* Botões */
        .btn {
            width: 100%;
            background: var(--neon-cyan);
            color: #000;
            border: none;
            padding: 12px;
            border-radius: 6px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
            text-transform: uppercase;
            margin-top: 10px;
        }

        .btn:hover {
            background: #00d2b4;
            box-shadow: 0 0 12px rgba(0, 245, 212, 0.5);
            transform: translateY(-2px);
        }

        .btn-secondary {
            background: transparent;
            color: var(--neon-purple);
            border: 2px solid var(--neon-purple);
            margin-top: 15px;
        }

        .btn-secondary:hover {
            background: var(--neon-purple);
            color: #fff;
            box-shadow: 0 0 10px rgba(157, 78, 221, 0.3);
        }

        .header-dashboard {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #252b41;
            padding-bottom: 15px;
            margin-bottom: 20px;
        }

        .user-welcome {
            font-size: 1.1rem;
            font-weight: bold;
        }

        .btn-logout {
            background: rgba(255, 0, 110, 0.1);
            color: var(--high-priority);
            border: 1px solid var(--high-priority);
            padding: 6px 12px;
            border-radius: 4px;
            cursor: pointer;
            transition: 0.3s;
            font-size: 0.85rem;
        }

        .btn-logout:hover {
            background: var(--high-priority);
            color: #fff;
        }

        /* Dashboard de XP */
        .dashboard {
            background: rgba(0, 0, 0, 0.4);
            border-radius: 8px;
            padding: 20px;
            text-align: center;
            border: 1px solid rgba(157, 78, 221, 0.3);
            margin-bottom: 30px;
        }

        .xp-display {
            font-size: 2.5rem;
            font-weight: bold;
            color: var(--neon-purple);
            text-shadow: 0 0 15px rgba(157, 78, 221, 0.6);
            margin: 10px 0;
        }

        /* Form Cadastro de Tarefas */
        .form-group {
            display: flex;
            gap: 15px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }

        .form-group input[type="text"] {
            flex: 2;
            min-width: 200px;
        }

        .form-group select {
            flex: 1;
            min-width: 150px;
        }

        /* Lista de Missões */
        .quest-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .quest-item {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid #252b41;
            padding: 15px 20px;
            border-radius: 8px;
            margin-bottom: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: 0.3s;
        }

        .quest-item:hover {
            border-color: rgba(157, 78, 221, 0.4);
            background: rgba(255, 255, 255, 0.04);
        }

        .quest-info {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }

        .quest-title {
            font-size: 1.1rem;
            font-weight: 500;
        }

        .quest-meta {
            display: flex;
            gap: 10px;
            font-size: 0.8rem;
            align-items: center;
        }

        .badge-priority {
            padding: 3px 8px;
            border-radius: 4px;
            font-weight: bold;
            text-transform: uppercase;
        }

        .priority-baixa { background: rgba(58, 134, 255, 0.15); color: var(--low-priority); }
        .priority-media { background: rgba(255, 190, 11, 0.15); color: var(--medium-priority); }
        .priority-alta { background: rgba(255, 0, 110, 0.15); color: var(--high-priority); }

        .badge-xp {
            color: var(--neon-cyan);
            font-weight: 600;
        }

        .btn-complete {
            background: transparent;
            border: 2px solid var(--neon-purple);
            color: var(--neon-purple);
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }

        .btn-complete:hover {
            background: var(--neon-purple);
            color: #fff;
            box-shadow: 0 0 10px rgba(157, 78, 221, 0.4);
        }

        .quest-completed {
            opacity: 0.5;
            background: rgba(0, 0, 0, 0.3);
            border-color: #1e2435;
        }

        .quest-completed .quest-title {
            text-decoration: line-through;
            color: #8b8f9e;
        }

        .badge-status {
            background: rgba(0, 245, 212, 0.15);
            color: var(--neon-cyan);
            padding: 3px 8px;
            border-radius: 4px;
            font-weight: bold;
            text-transform: uppercase;
            font-size: 0.8rem;
        }
    </style>
</head>
<body>

<!-- TELA DE AUTENTICAÇÃO -->
<div class="auth-container" id="auth-panel">
    <h1>DevQuest</h1>
    <p class="subtitle">TaskTracker Gamificado</p>
    
    <h2 id="auth-title">Acessar Portal</h2>
    
    <div class="input-group">
        <label for="username">Nome de Usuário (Login)</label>
        <input type="text" id="username" placeholder="Seu apelido de player...">
    </div>
    
    <div class="input-group">
        <label for="password">Senha de Acesso</label>
        <input type="password" id="password" placeholder="Sua senha secreta...">
    </div>
    
    <button class="btn" id="btn-primary-auth" onclick="processarAutenticacao()">Entrar na Jornada</button>
    <button class="btn btn-secondary" id="btn-switch-auth" onclick="alternarModoAuth()">Criar Nova Conta</button>
</div>

<!-- PAINEL DO USUÁRIO (DASHBOARD PRINCIPAL) -->
<div class="container" id="main-panel">
    <div class="header-dashboard">
        <div class="user-welcome">Player: <span id="display-username" style="color: var(--neon-cyan);">Gabrielle</span></div>
        <button class="btn-logout" onclick="fazerLogout()">Sair da Conta</button>
    </div>

    <!-- Painel de XP -->
    <div class="dashboard">
        <div>NÍVEL DE EXPERIÊNCIA ATUAL</div>
        <div class="xp-display" id="xp-total">0 XP</div>
        <div style="font-size: 0.85rem; color: #8b8f9e;">Complete missões para evoluir o seu painel!</div>
    </div>

    <!-- Cadastro de Tarefas (Entradas da Fase 1) -->
    <div class="form-group">
        <input type="text" id="quest-title" placeholder="Digite o título da sua missão (Ex: Refatorar Código)...">
        <select id="quest-priority">
            <option value="">Selecionar Prioridade</option>
            <option value="Baixa">Baixa (10 XP)</option>
            <option value="Média">Média (25 XP)</option>
            <option value="Alta">Alta (50 XP)</option>
        </select>
        <button class="btn btn-add" style="width: auto; margin: 0;" onclick="cadastrarMissao()">Iniciar Quest</button>
    </div>

    <!-- Lista de Saídas da Fase 1 -->
    <h3 style="border-bottom: 1px solid #252b41; padding-bottom: 10px; margin-bottom: 15px;">Suas Quests Ativas</h3>
    <ul class="quest-list" id="quest-list">
        <!-- Inseridas dinamicamente via JS com isolamento por conta -->
    </ul>
</div>

<script>
    // Controle de Sessão e Estado do Sistema
    let currentUser = null;
    let modoCadastro = false; // Alterna entre Login e Registro

    // Inicialização da aplicação
    window.onload = function() {
        const userSalvo = sessionStorage.getItem('devquest_session_user');
        if (userSalvo) {
            currentUser = userSalvo;
            carregarDashboardUsuario();
        }
    };

    // Alternar entre tela de Login e tela de Cadastro
    function alternarModoAuth() {
        modoCadastro = !modoCadastro;
        const authTitle = document.getElementById('auth-title');
        const btnPrimary = document.getElementById('btn-primary-auth');
        const btnSwitch = document.getElementById('btn-switch-auth');

        if (modoCadastro) {
            authTitle.innerText = "Criar Nova Conta";
            btnPrimary.innerText = "Registrar Jogador";
            btnSwitch.innerText = "Já tenho uma conta (Fazer Login)";
        } else {
            authTitle.innerText = "Acessar Portal";
            btnPrimary.innerText = "Entrar na Jornada";
            btnSwitch.innerText = "Criar Nova Conta";
        }
    }

    // Processamento de Login ou Registro de Usuário
    function processarAutenticacao() {
        const usernameInput = document.getElementById('username').value.trim();
        const passwordInput = document.getElementById('password').value.trim();

        if (usernameInput === "" || passwordInput === "") {
            alert("Erro: Preencha todos os campos para prosseguir.");
            return;
        }

        // Carrega a base de usuários registrados no LocalStorage
        let usuariosRegistrados = JSON.parse(localStorage.getItem('devquest_registered_users')) || [];

        if (modoCadastro) {
            // Fluxo de Cadastro de Usuário
            const usuarioExiste = usuariosRegistrados.some(u => u.username.toLowerCase() === usernameInput.toLowerCase());
            if (usuarioExiste) {
                alert("Erro: Este nome de usuário já está sendo usado por outro player.");
                return;
            }

            // Registra novo usuário
            usuariosRegistrados.push({ username: usernameInput, password: passwordInput });
            localStorage.setItem('devquest_registered_users', JSON.stringify(usuariosRegistrados));
            alert("Sucesso! Conta criada com êxito. Faça o seu login agora!");
            alternarModoAuth();
        } else {
            // Fluxo de Login
            const usuarioValido = usuariosRegistrados.find(u => u.username.toLowerCase() === usernameInput.toLowerCase() && u.password === passwordInput);
            
            if (usuarioValido) {
                currentUser = usuarioValido.username;
                sessionStorage.setItem('devquest_session_user', currentUser);
                carregarDashboardUsuario();
            } else {
                alert("Erro: Nome de usuário ou senha incorretos.");
            }
        }
    }

    // Carregar os dados exclusivos do usuário logado
    function carregarDashboardUsuario() {
        document.getElementById('auth-panel').style.display = 'none';
        document.getElementById('main-panel').style.display = 'block';
        document.getElementById('display-username').innerText = currentUser;

        // Limpa os inputs da tela de login
        document.getElementById('username').value = "";
        document.getElementById('password').value = "";

        renderizarMissoes();
    }

    // Realizar Logout e fechar sessão
    function fazerLogout() {
        sessionStorage.removeItem('devquest_session_user');
        currentUser = null;
        document.getElementById('main-panel').style.display = 'none';
        document.getElementById('auth-panel').style.display = 'block';
    }

    // Buscar as tarefas exclusivas do usuário logado
    function obterMissoesDoUsuario() {
        return JSON.parse(localStorage.getItem(`devquest_missoes_${currentUser}`)) || [];
    }

    // Buscar o XP exclusivo do usuário logado
    function obterXpDoUsuario() {
        return parseInt(localStorage.getItem(`devquest_xp_${currentUser}`)) || 0;
    }

    // Cadastrar Missão isolada por conta (Regras 1 e 2)
    function cadastrarMissao() {
        const tituloInput = document.getElementById('quest-title');
        const prioridadeSelect = document.getElementById('quest-priority');

        const titulo = tituloInput.value.trim();
        const prioridade = prioridadeSelect.value;

        if (titulo === "") {
            alert("Erro: O título da missão é obrigatório.");
            return;
        }

        if (prioridade === "") {
            alert("Erro: Por favor, selecione uma prioridade.");
            return;
        }

        // Regra de XP automático (Regra 3)
        let xpCalculado = 0;
        if (prioridade === "Baixa") xpCalculado = 10;
        else if (prioridade === "Média") xpCalculado = 25;
        else if (prioridade === "Alta") xpCalculado = 50;

        const novaMissao = {
            titulo: titulo,
            prioridade: prioridade,
            xp: xpCalculado,
            status: "Pendente"
        };

        let lista = obterMissoesDoUsuario();
        lista.push(novaMissao);

        localStorage.setItem(`devquest_missoes_${currentUser}`, JSON.stringify(lista));

        tituloInput.value = "";
        prioridadeSelect.value = "";

        renderizarMissoes();
    }

    // Concluir Missão (Regra 4)
    function concluirMissao(index) {
        let lista = obterMissoesDoUsuario();
        let xpAcumulado = obterXpDoUsuario();
        const missao = lista[index];

        if (missao.status === "Pendente") {
            missao.status = "Concluída";
            xpAcumulado += missao.xp;

            localStorage.setItem(`devquest_missoes_${currentUser}`, JSON.stringify(lista));
            localStorage.setItem(`devquest_xp_${currentUser}`, xpAcumulado);

            renderizarMissoes();
        }
    }

    // Renderizar dados na tela de forma isolada
    function renderizarMissoes() {
        const listContainer = document.getElementById('quest-list');
        listContainer.innerHTML = "";

        const lista = obterMissoesDoUsuario();
        const xpAcumulado = obterXpDoUsuario();

        if (lista.length === 0) {
            listContainer.innerHTML = `<li style="text-align: center; color: #8b8f9e; padding: 20px;">Você não tem missões cadastradas no seu painel. Comece a sua jornada técnica agora!</li>`;
            document.getElementById('xp-total').innerText = `${xpAcumulado} XP`;
            return;
        }

        lista.forEach((missao, index) => {
            const isCompleted = missao.status === "Concluída";
            const li = document.createElement('li');
            li.className = `quest-item ${isCompleted ? 'quest-completed' : ''}`;

            li.innerHTML = `
                <div class="quest-info">
                    <span class="quest-title">${missao.titulo}</span>
                    <div class="quest-meta">
                        <span class="badge-priority priority-${missao.prioridade.toLowerCase()}">${missao.prioridade}</span>
                        <span class="badge-xp">+${missao.xp} XP</span>
                        ${isCompleted ? '<span class="badge-status">Concluída</span>' : ''}
                    </div>
                </div>
                ${!isCompleted ? `<button class="btn-complete" onclick="concluirMissao(${index})">Concluir</button>` : '<span></span>'}
            `;

            listContainer.appendChild(li);
        });

        document.getElementById('xp-total').innerText = `${xpAcumulado} XP`;
    }
</script>

</body>
</html>
