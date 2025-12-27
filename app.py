cat > app.py << 'EOF'
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from CI/CD!"
EOF
