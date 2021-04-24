import csv

# make a class called housing_scvs
class housing_scvs():

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
                    housing_option = {}
                    # store interesting fields in dictionary
                    housing_option['Name'] = row[0]
                    housing_option['URL'] = row[1]
                    housing_option['Description'] = row[2]

                    if row[9].upper() == "YES":
                        housing_option['Community'] = True
                    else:
                        housing_option['Community'] = False

                    self.housing_options.append(housing_option)

                row_num = row_num + 1

	# Initialization function
    def __init__(self, csvfile):
		# initialize books attribute
        self.housing_options = []
        self.__read_csv__(csvfile)
        
    def get_community_housing(self):
        # init empty list
        community_housing = []
        # loop through each housing_scvs(csvfile) option read from csv earlier
        for housing_option in self.housing_options:
            # if community housing_scvs(csvfile) is supported, append to list
            if housing_option['Community'] == True:
                community_housing.append(housing_option)

        return community_housing

if __name__ == '__main__':
    my_housing = housing_scvs("housing_scvs.csv")
    
    community_housing = my_housing.get_community_housing()
    
    for housing_scvs in community_housing:
        print(housing_scvs['Name'])