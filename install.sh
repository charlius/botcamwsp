rm -rf venv
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt  --no-cache-dir