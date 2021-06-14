from flask import Flask, render_template, url_for
import email_validator
app = Flask(__name__)

posts = [
	{
		'author': 'Eric Liu',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'June 12, 2021'
	},
	{
		'author': 'Corey Schafer',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'June 13, 2021'
	}
]

@app.route("/")
def hello():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')

if __name__ == '__main__':
	app.run(debug=True)