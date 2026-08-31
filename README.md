# DevQuest | TaskTracker Gamificado

> **"Transforme suas tarefas diárias em missões épicas e acompanhe sua evolução profissional em tempo real."**

O **DevQuest** é um sistema de gerenciamento de tarefas (*TaskTracker*) totalmente gamificado, projetado especialmente para estudantes de tecnologia e desenvolvedores de software. O projeto substitui as listas de tarefas estáticas e monótonas por uma dinâmica de RPG (*Role-Playing Game*), onde suas entregas e rotinas de estudo tornam-se missões que rendem Pontos de Experiência (XP).

Este projeto é desenvolvido como parte integrante das atividades do **Bootcamp II (Ciência de Dados e Machine Learning - CEUB)**.

---

## Como Funciona o DevQuest?

1. **Cadastre uma Missão (Quest):** Defina o título da sua atividade (ex: *Estudar Pandas*) e selecione a prioridade (**Baixa**, **Média** ou **Alta**).
2. **Atribuição Automática de XP:** O sistema calcula a recompensa de XP proporcionalmente ao nível de desafio selecionado.
3. **Conclua e Evolua:** Marque a missão como concluída para somar os pontos de experiência ao seu **Painel Geral de XP**, monitorando visualmente o seu ganho de produtividade diário.

---

## Regras de Negócio e Matriz de XP

Para garantir a integridade e o engajamento do ecossistema, o DevQuest respeita quatro regras principais:

*   **Validação de Título:** O título da missão é obrigatório. Não são aceitos campos em branco ou vazios.
*   **Prioridades Restritas:** O sistema aceita estritamente os níveis de prioridade **Baixa**, **Média** ou **Alta**.
*   **Cálculo Automatizado de XP:** O XP é atrelado automaticamente à prioridade:
    *   Prioridade **Baixa** ➔ **10 XP**
    *   Prioridade **Média** ➔ **25 XP**
    *   Prioridade **Alta** ➔ **50 XP**
*   **Ciclo de Vida Único:** Apenas missões com status `"Pendente"` podem ser concluídas, e o XP correspondente só é computado e adicionado ao Painel Geral após a conclusão bem-sucedida da missão.

---

## Arquitetura do Repositório

O projeto segue uma estrutura modular e limpa de diretórios, separando as documentações de modelagem lógica do código-fonte:

```text
devquest-tasktracker/
├── README.md                             # Apresentação e documentação do projeto
├── .gitignore                            # Configuração para ignorar arquivos temporários do Python
├── docs/                                 # Pasta para armazenamento de documentos de planejamento
│   └── planejamento_logico_devquest.pdf  # Documentação de Arquitetura de Software (Fase 1)
└── src/                                  # Pasta que armazena os códigos do programa
    └── main.py                           # Script principal da aplicação em Python (Fase 2)

```
## Autoria e Contato

Fique à vontade para se conectar comigo, explorar meus outros projetos de dados ou enviar um feedback:

*  **LinkedIn:** [Acesse meu perfil profissional](https://www.linkedin.com/in/gabrielle-keiko-9baa6a2b3/)
*  **E-mail Pessoal:** [gkeiko.05@gmail.com](mailto:gkeiko.05@gmail.com)
*  **E-mail Institucional:** [gkeiko.05@gmail.com](mailto:gabrielle.keiko@sempreceub.com)
*  **Meu Portal Principal:** (https://gabriellekeiko.github.io/devquest-tasktracker/)

---
