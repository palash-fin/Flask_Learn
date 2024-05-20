from app import app,db  # Import the app instance

with app.app_context():
    db.create_all()