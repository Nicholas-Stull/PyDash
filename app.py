from flask import Flask, render_template
import psutil

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to the Computer Stats Dashboard!"


@app.route("/dashboard")
def dashboard():
    cpu_usage = psutil.cpu_percent()
    virtual_memory = psutil.virtual_memory()
    disk_usage = psutil.disk_usage("/")

    return render_template(
        "dashboard.html",
        cpu_usage=cpu_usage,
        virtual_memory=virtual_memory,
        disk_usage=disk_usage,
    )


if __name__ == "__main__":
    app.run(debug=True)
