from flask import Flask, render_template, redirect, url_for
from os import listdir, getcwd, chdir, remove, chmod
from os.path import isfile
from shutil import copy

option = ["Movie", "anime"]
global folder
folder = ""
tree = []
# chdir(folder)
stat = "E:\\stream\\static"
app = Flask(__name__)

port = 5000
ip = "192.168.1.10"


@app.route('/browse')
def browse():
    files = listdir(getcwd())
    t = [files[i:i + 3] for i in range(0, len(files), 3)]
    return render_template('page_temp.html', items=t, port=port, ip=ip)


@app.route('/')
def index():
    t = [option[i:i + 3] for i in range(0, len(option), 3)]
    return render_template('main.html', items=t, port=port, ip=ip)


@app.route('/browse/<file>')
def downloadFile(file):
    global folder
    if isfile(file):

        if file[-4:] == ".mp4" or file[-4:] == ".mkv" or file[-4:]=='.avi':
            r_files = listdir(stat)
            for i in r_files:
                chmod(stat + "\\" + i, 0o777)
                remove(stat + "\\" + i)
            t = folder + "\\"
            for i in tree:
                t = t + i + "\\"
            copy(t + file, stat)
            return render_template('play.html', items=file)
    else:
        chdir(file)
        tree.append(file)
        return redirect(url_for('browse'))


@app.route('/backtrack')
def back():
    tree.pop()
    chdir("..")
    return redirect(url_for('browse'))


@app.route('/<choice>')
def select(choice):
    global folder
    if choice == "Movie":
        folder = "E:\\Movie"
    elif choice == "anime":
        folder = "F:\\anime"
    chdir(folder)
    return redirect(url_for('browse'))


if __name__ == '__main__':
    app.run(host=ip, port=port, debug=True)
