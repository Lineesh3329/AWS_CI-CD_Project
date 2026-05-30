from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AWS DevOps Project</title>

        <style>
            body {
                background: linear-gradient(135deg, #fde68a, #cbd5e1, #93c5fd);
                font-family: "Times New Roman", Times, serif;
                text-align: center;
                color: #111827;
                margin-top: 100px;
            }

            .card {
                background: rgba(255,255,255,0.35);
                backdrop-filter: blur(10px);
                padding: 20px;
                border-radius: 15px;
                width: 450px;
                margin: auto;
                box-shadow: 0 10px 25px rgba(0,0,0,0.15);
                border: 1px solid rgba(255,255,255,0.4);
            }

            h1 {
                color: #1e3a8a;
                font-size: 28px;
                margin-bottom: 10px;
            }

            h2 {
                color: #374151;
                font-size: 20px;
                margin-bottom: 15px;
            }

            p {
                font-size: 15px;
                margin: 8px 0;
            }

            .pipeline {
                color: #2563eb;
                font-weight: bold;
            }

            .status {
                color: #15803d;
                font-weight: bold;
                text-align: left;
                display: inline-block;
                margin-top: 10px;
            }

            .status ul {
                list-style: none;
                padding: 0;
                margin: 0;
            }

            .status li {
                margin: 5px 0;
            }

            .footer {
                margin-top: 15px;
                color: #4b5563;
                font-size: 13px;
            }

            .btn {
                margin-top: 15px;
                padding: 10px 20px;
                background-color: #2563eb;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 15px;
                cursor: pointer;
                font-family: "Times New Roman", Times, serif;
            }

            .btn:hover {
                background-color: #1d4ed8;
            }
        </style>
    </head>

    <body>

        <div class="card">

            <h1>Hello, Lineeswaran! 🚀</h1>

            <h2>AWS CI/CD Project</h2>

            <p>Automated deployment using AWS.</p>

            <p class="pipeline">
                GitHub → CodePipeline → CodeBuild → CodeDeploy → EC2
            </p>

            <div class="status">
                <ul>
                    <li>✅ Build Successful</li>
                    <li>✅ Deployment Successful</li>
                    <li>✅ Application Running</li>
                </ul>
            </div>

            <br>

            <button class="btn">DevOps Project</button>

            <div class="footer">
                Built by Lineeswaran
            </div>

        </div>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
