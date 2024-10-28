# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuration de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.yourmailprovider.com'  # Remplace avec ton serveur SMTP
app.config['MAIL_PORT'] = 587  # Port SMTP
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = ''  # Ton email
app.config['MAIL_PASSWORD'] = ''  # Ton mot de passe d'email

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Récupère les données du formulaire
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Envoie de l'email
   #msg = Message(subject=f"Message de {name}",
   #               sender=email,
    #              recipients=['tonemail@example.com'])
    #msg.body = f"Nom: {name}\nEmail: {email}\nSujet: {subject}\n\nMessage:\n{message}"
    msg = Message(subject="Message de {}".format(name),
              sender=email,
              recipients=['tonemail@example.com'])
    msg.body = "Nom: {}\nEmail: {}\nSujet: {}\n\nMessage:\n{}".format(name, email, subject, message)

    mail.send(msg)

    return "Merci ! Votre message a bien été envoyé."

if __name__ == '__main__':
    app.run(debug=True)
