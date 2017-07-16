from flask import Flask , request, render_template
import matplotlib.pyplot as plt
app = Flask(__name__)
users={"user1":"user1 info",'user2':'user2 info','user3':'user3 info'}

@app.route('/get_user',methods=['GET','POST'])
def send_user_info():
	user=request.form.get('x')
	if user:
		user_info=users.get(user)
	else:
		user_info=""
		
	return render_template('form.html',user_info={"user1":"user1 info",'user2':'user2 info','user3':'user3 info'})


@app.route('/users')
def get_user():
	return "<h1>user1,user2,user3</h1>"
@app.route('/get_bargraph',methods=['GET','POST'])
def get_graph():
	if request.method=="GET":
		return render_template('form.html')
	elif request.method=='POST':
		form = request.form 
		x=map(int,form.get('x').split(','))
		y=map(int,form.get('y').split(','))
		plt.bar(x,y)
		plt.savefig('./static/bar.png')
		return render_template('form.html')

if __name__ == "__main__":
	app.run(debug=True,port=6001)