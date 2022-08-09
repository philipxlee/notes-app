from website import create_app

app = create_app()

# Runs the Flask Server
if __name__ == "__main__": # Only if run and not import
    app.run(debug=True) # Everytime there is a change in python code, the server is re-ran



