from flask import Flask, render_template, redirect, url_for
from os import listdir, getcwd, system, chdir
from os.path import isfile

folder = "E:/stream/static/Movie"
lis = ["Movie"]
chdir(folder)
app = Flask(__name__)

port = 5000

ip = "192.168.1.10"


def to_matrix(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


@app.route('/')
def index():
    files = listdir(getcwd())
    t = to_matrix(files, 3)
    return render_template('page_temp.html', items=t, port=port, ip=ip)


@app.route('/<file>')
def downloadFile(file):
    if isfile(file):

        if file[-4:] == ".mp4" or file[-4:] == ".mkv":
            tes = ""
            for i in lis:
                tes = tes + i + "/"
            file = tes + file
            print(file)
            return render_template('play.html', items=file)
    else:
        chdir(file)
        lis.append(file)
        return redirect(url_for('index'))


@app.route('/backtrack')
def back():
    chdir("..")
    lis.pop()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=ip, port=port, debug=False)
