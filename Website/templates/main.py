from Website import create_app


app = create_app()


#only if we run this file, the app will be running
if __name__ == "__main__":
    app.run(debug=True)

 