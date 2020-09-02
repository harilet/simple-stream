from flask import Flask, render_template, redirect, url_for
from os import listdir, getcwd, chdir, remove, chmod
from os.path import isfile
from shutil import copy


global folder,option,tree,stat
app = Flask(__name__)


@app.route('/')
def browse():
    files = listdir(getcwd())
    t = [files[i:i + 3] for i in range(0, len(files), 3)]
    return render_template('page_temp.html', items=t, port=port, ip=ip)


@app.route('/<file>')
def downloadFile(file):
    global folder
    if isfile(file):

        if file[-4:] == ".mp4":
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


if __name__ == '__main__':

    folder =str(input("Enter movie folder location:"))
    tree = []
    chdir(folder)
    stat = str(input("Enter static folder location:"))
    port = 5000
    ip = str(input("Enter IP address:"))
    app.run(host=ip, port=port, debug=True, use_reloader=False)

