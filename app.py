import os

os.system("lmdeploy serve api_server workspace --server-name 0.0.0.0 --server-port 7860 --tp 1")
os.system("lmdeploy serve api_client http://localhost:23333")
