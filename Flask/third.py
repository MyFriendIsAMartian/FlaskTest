from flask import Flask, render_template, request
import os.path
app = Flask(__name__)

@app.route("/")
def file1():
    if "filename" not in request.args:
        filename = "file1.html"
    else:
        filename = str(request.args.get("filename"))
    if not os.path.exists("/Users/Workscape/Folders/Python/Flask/templates/"+ filename):
        filename= "file1.html"
    return render_template(filename)

@app.route("/search1")
def file1selectedlines():
    try:
        a=int(request.args.get("a"))
        z=int(request.args.get("z"))
        if a<0 or z<0:
            raise Exception("Received a negative number for the range. Please input a positive number.")
        if z<a:
            raise Exception("Final value (z) is less than initial value (a); range must go from a lesser number to a greater number (a-z).")
        with open("./templates/file1.html", "r") as f:
            content = f.readlines()
        content=content[a+1:z+2]
        return ''.join(content)
    except(Exception) as e:
        return str("An error has occured; please input a number for the range - ") + str(e)

@app.route("/file2")
def file2():
    return render_template("file2.html")

@app.route("/search2")
def file2selectedlines():
    try:
        a=int(request.args.get("a"))
        z=int(request.args.get("z"))
        if a<0 or z<0:
            raise Exception("Received a negative number for the range. Please input a positive number.")
        if z<a:
            raise Exception("Final value (z) is less than initial value (a); range must go from a lesser number to a greater number (a-z).")
        with open("./templates/file2.html", "r") as f2:
            content = f2.readlines()
        content=content[a+1:z+2]
        return ''.join(content)
    except(Exception) as e:
        return str("An error has occured; please input a number for the range - ") + str(e)

@app.route("/file3")
def file3():
    return render_template("file3.html")

@app.route("/search3")
def file3selectedlines():
    try:
        a=int(request.args.get("a"))
        z=int(request.args.get("z"))
        if a<0 or z<0:
            raise Exception("Received a negative number for the range. Please input a positive number.")
        if z<a:
            raise Exception("Final value (z) is less than initial value (a); range must go from a lesser number to a greater number (a-z).")
        with open("./templates/file3.html", "r") as f3:
            content = f3.readlines()
        content=content[a+1:z+2]
        return ''.join(content)
    except(Exception) as e:
        return str("An error has occured; please input a number for the range - ") + str(e)

@app.route("/file4")
def file4():
    return render_template("file4.html")

@app.route("/search4")
def file4selectedlines():
    try: 
        a=int(request.args.get("a"))
        z=int(request.args.get("z"))
        if a<0 or z<0:
            raise Exception("Received a negative number for the range. Please input a positive number.")
        if z<a:
            raise Exception("Final value (z) is less than initial value (a); range must go from a lesser number to a greater number (a-z).")
        with open("./templates/file4.html", "r") as f4:
            content = f4.readlines()
        content=content[a:z+1]
        return ''.join(content)
    except(Exception) as e:
        return str("An error has occured; please input a number for the range - ") + str(e)
