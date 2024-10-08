from flask import Flask
from board import pages

def create_app():
	app = Flask(__name__)

	app.register_blueprint(pages.bp)
	return app

	@app.route("/")
	def home() :
		return "Hello, World!!!"

if __name__ == "__main__" :
	app = create_app()
	app.run(host="0.0.0.0", port=8000, debug=True)
