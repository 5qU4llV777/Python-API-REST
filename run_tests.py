import subprocess

# Inicia o servidor Uvicorn em segundo plano
server = subprocess.Popen(["uvicorn", "main:app", "--reload"])

# Roda os testes com pytest
subprocess.run(["python", "-m", "pytest", "-v"])


# Finaliza o servidor depois dos testes
server.terminate()
