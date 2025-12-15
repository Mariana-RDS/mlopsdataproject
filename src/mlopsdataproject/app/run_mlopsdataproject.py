import subprocess

def run_mlopsdataproject_app():
    cmd = ["streamlit", "run", "./src/mlopsdataproject/app/app.py"]
    subprocess.run(cmd, check=True)