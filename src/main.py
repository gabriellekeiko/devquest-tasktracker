import json
import argparse
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg') # Modo headless para ambientes de execução offline/sem monitor
import matplotlib.pyplot as plt

def analisar_dados_devquest(file_path, output_image='performance_dashboard.png'):
    # Validação do arquivo de entrada
    if not os.path.exists(file_path):
        print(f"Erro: O arquivo de backup '{file_path}' não foi encontrado.")
        return

    print("=" * 60)
    print("📊 DEVQUEST - ENGINE DE INTELIGÊNCIA ANALÍTICA DE PRODUTIVIDADE")
    print("=" * 60)

    # Carregamento do arquivo JSON
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    username = data.get("username", "Desconhecido")
    perfil = data.get("profile", {})
    stats = data.get("stats", {})
    missoes_lista = data.get("missoes", [])
    xp_total = data.get("xp", 0)

    fullname = perfil.get("fullname", "Não Informado")
    curso = perfil.get("course", "Não Informado")
    nivel = (xp_total // 200) + 1

    # Print de informações cadastrais básicas
    print(f"👤 Player: {username} ({fullname})")
    print(f"💼 Curso/Área: {curso}")
    print(f"⭐ Nível Atual: {nivel} | XP Acumulado: {xp_total} XP")
    print("-" * 60)

    if not missoes_lista:
        print("Aviso: Nenhuma missão ativa ou concluída encontrada neste backup para análise de dados.")
        return

    # Transformação em DataFrame do Pandas
    df = pd.DataFrame(missoes_lista)

    # Estatísticas básicas com Pandas
    total_quests = len(df)
    concluidas = len(df[df['status'] == 'Concluída']) if 'status' in df.columns else 0
    falhadas = len(df[df['status'] == 'Falhada']) if 'status' in df.columns else 0
    pendentes = len(df[df['status'] == 'Pendente']) if 'status' in df.columns else 0

    taxa_conclusao = (concluidas / total_quests * 100) if total_quests > 0 else 0

    print("📈 MÉTRICAS DE PRODUTIVIDADE (PANDAS KPI):")
    print(f"  • Total de Missões Iniciadas: {total_quests}")
    print(f"  • Missões Concluídas: {concluidas}")
    print(f"  • Missões Falhadas (Expiradas): {falhadas}")
    print(f"  • Missões Ativas (Pendentes): {pendentes}")
    print(f"  • Taxa de Sucesso Operacional: {taxa_conclusao:.2f}%")
    print("-" * 60)

    # Distribuição por Prioridade
    if 'prioridade' in df.columns:
        print("⚔️ DISTRIBUIÇÃO OPERACIONAL POR CRITICIDADE:")
        prioridade_counts = df['prioridade'].value_counts()
        for prio, count in prioridade_counts.items():
            print(f"  • Prioridade {prio}: {count} missão(ões)")
        print("-" * 60)

    # Geração dos Gráficos com Matplotlib (Foco em Ciência de Dados)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.patch.set_facecolor('#0d0e15') # Fundo Cyberpunk do App

    # Gráfico 1: Pizza do Status das Missões
    labels = []
    sizes = []
    colors = []

    if concluidas > 0:
        labels.append('Concluídas')
        sizes.append(concluidas)
        colors.append('#00f5d4') # Cyan Neon
    if falhadas > 0:
        labels.append('Falhadas')
        sizes.append(falhadas)
        colors.append('#ff006e') # Pink Neon
    if pendentes > 0:
        labels.append('Pendentes')
        sizes.append(pendentes)
        colors.append('#9d4edd') # Purple Neon

    if sizes:
        axes[0].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, 
                    colors=colors, textprops={'color': '#f0f2f5', 'weight': 'bold'})
        axes[0].set_title('Status Geral das Quests', color='#00f5d4', weight='bold', fontsize=12)
        axes[0].set_facecolor('#151824')
    else:
        axes[0].text(0.5, 0.5, 'Sem dados de status', color='#8b8f9e', ha='center', va='center')

    # Gráfico 2: Ganho de XP Estimado por Prioridade (Barras)
    if 'prioridade' in df.columns:
        df_concluidas = df[df['status'] == 'Concluída']
        if not df_concluidas.empty:
            xp_prio = df_concluidas.groupby('prioridade')['xp'].sum().reindex(['Baixa', 'Média', 'Alta'], fill_value=0)
            bars = axes[1].bar(xp_prio.index, xp_prio.values, color=['#3a86ff', '#ffbe0b', '#ff006e'], edgecolor='#9d4edd')
            axes[1].set_title('Distribuição de Recompensas (XP Ganho)', color='#9d4edd', weight='bold', fontsize=12)
            axes[1].set_ylabel('Pontos de Experiência (XP)', color='#8b8f9e')
            axes[1].tick_params(colors='#8b8f9e')
            
            # Adiciona os valores nas barras
            for bar in bars:
                height = bar.get_height()
                axes[1].annotate(f'{height} XP',
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3),  # offset vertical de 3 pontos
                            textcoords="offset points",
                            ha='center', va='bottom', color='#f0f2f5', weight='bold', fontsize=9)
        else:
            axes[1].text(0.5, 0.5, 'Nenhuma quest concluída para\nanálise de distribuição de XP.', 
                         color='#ffbe0b', ha='center', va='center', weight='bold')
    else:
        axes[1].text(0.5, 0.5, 'Sem dados de prioridade', color='#8b8f9e', ha='center', va='center')

    # Estilização Global dos Gráficos
    for ax in axes:
        ax.set_facecolor('#151824')
        ax.spines['bottom'].set_color('#252b41')
        ax.spines['top'].set_color('#252b41')
        ax.spines['left'].set_color('#252b41')
        ax.spines['right'].set_color('#252b41')

    plt.tight_layout()
    plt.savefig(output_image, dpi=150, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

    print(f"🎉 Análise de Portfólio gerada com sucesso!")
    print(f"📊 Gráfico de desempenho salvo como: '{output_image}'")
    print("=" * 60)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Processador Analítico de Produtividade do DevQuest")
    parser.add_argument('--backup', type=str, required=True, help="Caminho do arquivo backup .json exportado")
    parser.add_argument('--output', type=str, default='performance_dashboard.png', help="Nome da imagem gráfica de saída")
    args = parser.parse_args()

    analisar_dados_devquest(args.backup, args.output)
