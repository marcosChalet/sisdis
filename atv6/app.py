from typing import List
from fastapi import FastAPI

app = FastAPI()

# Dados fictícios de tarefas para simular um banco de dados
todo_list_db = [
  {"id": 1, "titulo": "Estudar a cadeira de Sistemas Distribuidos", "concluida": True},
  {"id": 2, "titulo": "Fazer compras", "concluida": True},
  {"id": 3, "titulo": "Preparar apresentação", "concluida": False},
]

@app.get("/")
def read_root():
  return {"message": "OK"}

@app.get("/tarefas/", response_model=List[dict])
def get_all_tasks():
  return todo_list_db

@app.get("/tarefas/{tarefa_id}", response_model=dict)
def get_task_by_id(tarefa_id: int):
  tarefa = next((tarefa for tarefa in todo_list_db if tarefa["id"] == tarefa_id), None)
  if tarefa:
      return tarefa
  return {"error": "Tarefa não encontrada"}

@app.post("/tarefas/", response_model=dict)
def create_task(nova_tarefa: dict):
  tarefa_id = len(todo_list_db) + 1
  nova_tarefa["id"] = tarefa_id
  todo_list_db.append(nova_tarefa)
  return nova_tarefa

@app.put("/tarefas/{tarefa_id}", response_model=dict)
def update_task(tarefa_id: int, dados_atualizados: dict):
  tarefa_index = next((index for index, tarefa in enumerate(todo_list_db) if tarefa["id"] == tarefa_id), None)
  if tarefa_index is not None:
      todo_list_db[tarefa_index].update(dados_atualizados)
      return todo_list_db[tarefa_index]
  return {"error": "Tarefa não encontrada"}

@app.delete("/tarefas/{tarefa_id}", response_model=dict)
def delete_task(tarefa_id: int):
  global todo_list_db
  todo_list_db = [tarefa for tarefa in todo_list_db if tarefa["id"] != tarefa_id]
  return {"message": "Tarefa removida com sucesso"}
