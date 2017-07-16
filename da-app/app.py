from flask import Flask , request
import matplotlib.pyplot as plt
app = Flask(__name__)
@app.route('/users')
def get_user():
	return "<h1>user1,user2,user3</h1>"
@app.route('/get_bargraph',methods=['GET','POST'])
def get_graph():
	if request.method=="GET":
		return """
		<form method='POST'>
		X_VALUES: <input type='text' name='x' value='1,2,3,4'/><br>
		y_VALKUES: <input type='text' name='y' value='10,20,30,40'/><br>
		<input type='submit' value='GET GRAPH'/>
		</form>
		"""
	elif request.method=='POST':
		form = request.form 
		x=map(int,form.get('x').split(','))
		y=map(int,form.get('y').split(','))
		plt.bar(x,y)
		plt.savefig('bar.png')
		return "<img src='bar.png' alt='image not found'/>"

if __name__ == "__main__":
	app.run(debug=True,port=6001)