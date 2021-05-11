from flask import Flask , render_template, request
import pandas as pd
import csv

# Setup flask on current file

app = Flask(__name__)


#creating basic website framwork below
@app.route('/', method=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', method=['GET', 'POST'])
def data():
    if request.method == 'POST':
        f = request.form['csvfile']
        data = []
        with open(f) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                data.append(row)
        return render_template('data.html', data=data)



if __name__ == "__main__":
    app.run(debug=True)

# @app.route is specific to (Flask) & must be follow function (In python in gen, decorator must be follow by a function or another decorator)

# @app.route("/", methods=["GET", "POST"]) 

#execute the function below
# def submit():
#   if request.method == "GET":
#     return redirect(url_for('index'))

# elif request.method == "POST":
#     userdata = dict(request.form)
#     city = userdata["city"][0]
        # (Main.py 69 - 75)
      #first_name = input('What is your first name?: ')
      #last_name = input('What is your Last name?: ')
      #sex_at_birth = input('Sex at Birth - Male/ or Female?: ')
      #gender_identity = input('Gender Identity: Heterosexual, Gay, Lesbian, Transgender, or Non-binary?: ')
      #age = input('How old are you?: ')
      #email_address = input('What is your email address?: ')
      #release_status = input('Are you currently on probation or parole?: ')



#     attraction = userdata["attraction"][0]
#     gif_url = userdata["gif"][0]
#     if len(city) < 2 and len(attraction) < 3 and (len(gif_url) < 10 or "gif" not in gif_url):
#       return "Please submit valid data."
#     with open('.data/places.csv', mode='a') as csv_file:
#       data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#       data.writerow([city, attraction, gif_url])
#   return "Thank you!"        