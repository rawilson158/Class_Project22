import csv

# make a class called job_scvs
class job_scvs():

    def __read_csv__(self, csvfile):
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

                    if row[6].upper() == "YES":
                        job_option['Full Time'] = True
                    else:
                        job_option['Full Time'] = False

                    self.job_options.append(job_option)

                row_num = row_num + 1

	# Initialization function
    def __init__(self, csvfile):
		# initialize books attribute
        self.job_options = []
        self.__read_csv__(csvfile)
        
    def get_full_time(self):
        # init empty list
        full_time = []
        # loop through each job_scvs(csvfile) option read from csv earlier
        for job_option in self.job_options:
            # if community job_scvs(csvfile) is supported, append to list
            if job_option['Full Time'] == True:
                full_time.append(job_option)

        return full_time

if __name__ == '__main__':
    my_job = job_scvs("job_scvs.csv")
    
    full_time = my_job.get_full_time()
    
    for job_scvs in full_time:
        print(job_scvs['Name'])