from flask import Flask
from start.whatsapp_quickstart import whatsapp_bp  # Import the Blueprint

def create_app():
    app = Flask(__name__)

    # Register the WhatsApp API routes
    app.register_blueprint(whatsapp_bp, url_prefix="/")

    return app
