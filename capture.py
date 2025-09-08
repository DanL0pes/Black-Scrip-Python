import time
import psutil
import pandas as pd # type: ignore
from datetime import datetime
import os


def capturar(usuarioCaptura, horarioCaptura, cpuUso, memUso, diskUso):
    df = None
    if(os.path.isfile("relatorioMonitoramento.csv")):
        df = pd.read_csv("relatorioMonitoramento.csv", sep=";")
   
    dados = {
        "usuario":[],
        "timestamp":[],
        "cpu":[],
        "ram":[],
        "disco":[]
    }       
    dados["usuario"].append(usuarioCaptura)
    dados["timestamp"].append(horarioCaptura)
    dados["cpu"].append(cpuUso)
    dados["ram"].append(memUso)
    dados["disco"].append(diskUso)

    if df is not None: 
        new_df = pd.DataFrame(dados)
        df = pd.concat([df, new_df], ignore_index=True)
    else:
        df = pd.DataFrame(dados)

    return df.to_csv("relatorioMonitoramento.csv", encoding="utf-8", sep=";", mode="w", index=False) 

while True:
    capturar(psutil.users()[0].name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), psutil.cpu_percent(), psutil.virtual_memory().percent, psutil.disk_usage('/').percent)
    time.sleep(10)
