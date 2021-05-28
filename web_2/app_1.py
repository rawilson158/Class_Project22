    
from flask import Flask, render_template
import csv

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/health')
def health():
    my_health = read_health("health_scvs.csv")
    return render_template('health.html', my_health=my_health)

@app.route('/housing')
def housing():
    my_housing = read_housing("housing_scvs.csv")
    return render_template('house.html', my_housing=my_housing) 

@app.route('/job')
def jobs():
    my_jobs = read_jobs("job_scvs.csv")
    return render_template('job.html', my_jobs=my_jobs)        


def read_housing(csvfile):
    housing_options = []

    # open the csv file
    with open(csvfile) as csv_file:
        # read the csv file
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_num = 0
        # loop through each line in csv
        for row in csv_reader:
            # skip the first line, which has the column names
            if row_num != 0:
                # create a dictionary    
                housing_option = {}
                # store interesting fields in dictionary location,phone,email,income,duration,single_occupancy,comm_housing
                housing_option['Name'] = row[0]
                housing_option['URL'] = row[1]
                housing_option['Description'] = row[2]
                housing_option['Location'] = row[3]
                housing_option['Phone'] = row[4]
                housing_option['Email'] = row[5]
                housing_option['Income'] = row[6]
                housing_option['Duration'] = row[7]
                housing_option['Single_Occupancy'] = row[8]
                housing_option['Community_housing'] = row[9]

                if row[9].upper() == "YES":
                    housing_option['Community'] = True
                else:
                    housing_option['Community'] = False

                housing_options.append(housing_option)

            row_num = row_num + 1

        return housing_options


def read_health(csvfile):
    health_options = []

    # open the csv file
    with open(csvfile) as csv_file:
        # read the csv file
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_num = 0
        # loop through each line in csv
        for row in csv_reader:
            # skip the first line, which has the column names
            if row_num != 0:
                # create a dictionary    
                health_option = {}
                # store interesting fields in dictionary - location,phone,email,primary_care,insurance
                health_option['Name'] = row[0]
                health_option['URL'] = row[1]
                health_option['Description'] = row[2]
                health_option['Location'] = row[3]
                health_option['Phone'] = row[4]
                health_option['Email'] = row[5]
                health_option['Primary_Care'] = row[6]
                health_option['Insurance'] = row[7]

                if row[7].upper() == "YES":
                    health_option['insurance'] = True
                else:
                    health_option['insurance'] = False

                health_options.append(health_option)

            row_num = row_num + 1

        return health_options  

def read_jobs(csvfile):
    job_options = []

    # open the csv file
    with open(csvfile) as csv_file:
        # read the csv file
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_num = 0
        # loop through each line in csv
        for row in csv_reader:
            # skip the first line, which has the column names
            if row_num != 0:
                # create a dictionary    
                job_option = {}
                # store interesting fields in dictionary
                job_option['Name'] = row[0]
                job_option['URL'] = row[1]
                job_option['Description'] = row[2]
                job_option['Location'] = row[3]
                job_option['Phone'] = row[4]
                job_option['Email'] = row[5]
                job_option['Full_Time'] = row[6]
                job_option['Part_Time'] = row[7]
                job_option['Temporary'] = row[8]
                job_option['Permanent'] = row[9]

                job_options.append(job_option)

            row_num = row_num + 1

        return job_options                      




