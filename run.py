from dash_app import create_app

app = create_app()
server = app.server

if __name__ == "__main__":
    app.run_server(debug=False)