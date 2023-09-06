import os
from flask import Flask, render_template

app = Flask(__name__)

# Define the folder whose contents you want to display
folder_path = "C:/GUI/CHA"

@app.route('/')
def display_folder_contents():
    # Get a list of all files and subdirectories in the folder
    folder_contents = os.listdir(folder_path)
    
    return render_template('folder_contents.html', folder_contents=folder_contents)

if __name__ == '__main__':
    app.run(debug=True)
