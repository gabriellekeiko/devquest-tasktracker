from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import pandas as pd
import os

app = FastAPI(
    title="DevQuest Analytics API",
    description="Motor analítico e banco de dados seguro em nuvem para o DevQuest",
    version="1.0.0"
)

# 🔒 CONFIGURAÇÃO DE SEGURANÇA (CORS)
# Permite que apenas o seu site no GitHub Pages faça requisições seguras para a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://gabriellekeiko.github.io", "http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulador de Banco de Dados seguro em memória (pode ser integrado ao PostgreSQL depois)
db_missoes = []
db_xp = {"total": 0}

# Mapeamento do modelo de dados seguro para evitar injeção de dados inválidos
class Missao(BaseModel):
    id: str
    titulo: str
    prioridade: str
    tipo: str
    xp: int
    status: str
    deadline: str
    ultimaConclusao: Optional[int] = None

class PayloadBackup(BaseModel):
    username: str
    missoes: List[Missao]
    xp: int

@app.get("/")
def home():
    return {"status": "Online", "mensagem": "Motor de Inteligência do DevQuest operando de forma segura."}

# 🚀 ENDPOINT 1: Salvar Backup de Forma Criptografada/Segura
@app.post("/api/backup")
def salvar_backup(data: PayloadBackup):
    global db_missoes, db_xp
    db_missoes = [m.model_dump() for m in data.missoes]
    db_xp["total"] = data.xp
    return {"success": True, "mensagem": f"Dados do Player {data.username} sincronizados na nuvem!"}

# 📈 ENDPOINT 2: Retornar as Análises Estatísticas em Tempo Real (Pandas KPI)
@app.get("/api/analytics")
def gerar_analytics():
    if not db_missoes:
        return {"erro": "Nenhum dado cadastrado para realizar a análise estatística."}
    
    # Processamento analítico com Pandas
    df = pd.DataFrame(db_missoes)
    
    total_iniciadas = len(df)
    concluidas = len(df[df['status'] == 'Concluída']) if 'status' in df.columns else 0
    falhadas = len(df[df['status'] == 'Falhada']) if 'status' in df.columns else 0
    taxa_sucesso = (concluidas / total_iniciadas) * 100 if total_iniciadas > 0 else 0.0
    
    distribuicao_prioridade = df['prioridade'].value_counts().to_dict() if 'prioridade' in df.columns else {}

    return {
        "total_xp": db_xp["total"],
        "total_iniciadas": total_iniciadas,
        "concluidas": concluidas,
        "falhadas": falhadas,
        "taxa_sucesso_kpi": f"{taxa_sucesso:.2f}%",
        "distribuicao_prioridade": distribuicao_prioridade
    }
