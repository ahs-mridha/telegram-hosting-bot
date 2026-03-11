import subprocess
import os

def run_python_bot(bot_file,requirements=None):

    if requirements:
        subprocess.run(["pip","install","-r",requirements])

    subprocess.Popen(["python",bot_file])