from flask import Flask, current_app, flash, render_template, request, session
from flask.ext.session import Session

app = Flask(__name__)
sess = Session()

@app.route('/')
def hello_world():
  return render_template('index.html')


@app.route('/process_input', methods=['POST'])
def process_input():
    src_loc = request.form['src_clus']
    folder_list = request.form['dest_clus']
    output_loc = request.form['no_iter']
    service = request.form['service']
    op = request.form['op']
    print "*********************************"
    print src_loc
    print folder_list
    print output_loc
    print service
    print op
    print "*********************************"
    return render_template('/index.html')

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.debug = True
    app.run()