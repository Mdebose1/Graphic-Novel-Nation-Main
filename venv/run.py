from app import create_app, db

app = create_app()
from app.blueprints.posts.models import Post, User

@app.shell_context_processor
def push_content():
    return {
        'db': db,
        'User': User,
        'Post': Post
    }
