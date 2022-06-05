from flask import Flask
from flask import render_template


def create_app(test_config=None):
    app = Flask(__name__, template_folder='templates')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    @app.route('/', methods=['GET'])
    def home():
        return render_template(
            '/index.html',
            phrase_output="",
            isSubmit=False
        )

    from . import activity
    app.register_blueprint(activity.bp)

    return app