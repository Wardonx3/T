from flask import Flask, request, redirect, url_for, session, render_template_string

app = Flask(__name__)
app.secret_key = "your_secret_key"  # For session management

# Approval data (used for demo purposes, can be replaced with a database)
approvals = {}

# Admin password
ADMIN_PASSWORD = "Thewardonhere"


# User approval request
@app.route("/", methods=["GET", "POST"])
def approval_request():
    if request.method == "POST":
        key = request.form.get("approval_key")
        if not key:
            return "Please enter a valid key.", 400

        # Check if the key is already approved
        if key in approvals and approvals[key]["status"] == "approved":
            return redirect(url_for("approved"))

        # Add key to approvals as pending
        approvals[key] = {"status": "pending"}
        
        return '''
        <html>
        <body style="font-family: Arial; text-align: center; background-color: #111; color: white; padding: 50px;">
            <h1 style="color: #ff4d4d;">Approval Request Sent</h1>
            <p>Wait for admin approval.</p>
            <a href="https://www.facebook.com/The.drugs.ft.chadwick.67" target="_blank" style="text-decoration: none; color: #4caf50; font-size: 18px;">Contact Admin</a>
        </body>
        </html>
        '''

    return '''
    <html>
    <head>
        <style>
            body {
                background-color: #111;
                font-family: Arial, sans-serif;
                color: white;
                text-align: center;
                padding: 50px;
            }
            h1 {
                font-size: 48px;
                color: #ff4d4d;
                text-shadow: 0px 0px 10px #ff4d4d;
                margin-bottom: 20px;
            }
            p {
                font-size: 20px;
                color: #ddd;
            }
            form {
                margin-top: 20px;
            }
            input[type="text"] {
                padding: 15px;
                width: 80%;
                max-width: 400px;
                border-radius: 5px;
                border: none;
                margin-bottom: 20px;
                font-size: 18px;
                box-shadow: 0px 0px 10px rgba(255, 77, 77, 0.8);
            }
            button {
                padding: 15px 30px;
                background-color: #ff4d4d;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 18px;
                text-transform: uppercase;
                box-shadow: 0px 0px 20px rgba(255, 77, 77, 0.8);
                transition: 0.3s;
            }
            button:hover {
                background-color: #cc0000;
                box-shadow: 0px 0px 25px rgba(255, 0, 0, 1);
            }
            .contact {
                margin-top: 20px;
                font-size: 18px;
            }
            .contact a {
                color: #4caf50;
                text-decoration: none;
                font-weight: bold;
                transition: 0.3s;
            }
            .contact a:hover {
                text-shadow: 0px 0px 10px #4caf50;
            }
        </style>
    </head>
    <body>
        <h1>Approval System</h1>
        <p>Enter your key to request approval</p>
        <form method="POST">
            <input type="text" name="approval_key" placeholder="Enter your approval key" required>
            <br>
            <button type="submit">Send Approval</button>
        </form>
        <div class="contact">
            <p>Need help? <a href="https://www.facebook.com/The.drugs.ft.chadwick.67" target="_blank">Contact Admin</a></p>
        </div>
    </body>
    </html>
    '''


# Page for approved users
@app.route("/approved")
def approved():
    return '''
    <html>
    <body style="font-family: Arial; text-align: center; background-color: #111; color: white; padding: 50px;">
        <h1 style="color: #4caf50; text-shadow: 0px 0px 10px #4caf50;">Welcome!</h1>
        <p>Your approval has been granted.</p>
        <button onclick="window.location.href='http://faizuapk.kesug.com/?i=1'" style="padding: 15px 30px; background-color: #4caf50; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 18px; text-transform: uppercase; box-shadow: 0px 0px 20px rgba(76, 175, 80, 0.8);">Open Your APK</button>
    </body>
    </html>
    '''


if __name__ == "__main__":
    # Make sure to run on 0.0.0.0 to make the server publicly accessible
    app.run(host="0.0.0.0", port=5000, debug=True)
