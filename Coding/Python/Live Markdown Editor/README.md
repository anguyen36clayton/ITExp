**Markdown Renderer**


**Required packages**
```
$sudo apt-get install python3
$pip install Flask
$pip install markdown2
```

```
Note: The app.py file is inside your desired directory
Note: Within that app.py directory, there is another one named templates
```

**Steps**
```
Step 1: Create a app.py file 
Step 2: Create a folder named templates
Step 3: Create a file named index.html in templates folder
Step 4: Run the application using terminal and cd into the folder containing app.py
$python3 app.py


The Flask development server will start, and you should see output indicating that the server is running. 
By default, Flask runs on http://127.0.0.1:5000/. 
Open this URL in your web browser to see your Markdown content rendered as HTML.
Additionally, the premade code is inside this folder and can run on any device within the network by using the IP:5000, where the IP is the IP of the device.
```

```
Status: Finished

v0.01: Added files for markdown editor
v0.02: Fixed bugs
v0.03: Corrected usage of markup 
v0.10: Added static folder for js query
v0.22: Live editor mode enabled
```

