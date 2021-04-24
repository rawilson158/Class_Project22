import csv

# with open ("housing_scvs.csv", "r") as f:
#     reader = csv.reader(f)
#     next(reader)
#     data = {"name": []}
#     for row in reader:
#         data["name"].append({"name":
#         row[0], "website": row[1]})
#     print(data)

class health_scv():
    
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
                    health_option = {}
                    # store interesting fields in dictionary
                    health_option['Name'] = row[0]
                    health_option['URL'] = row[1]
                    health_option['Description'] = row[2]

                    if row[6].upper() == "YES":
                        health_option['Primary Care'] = True
                    else:
                        health_option['Primary Care'] = False

                    self.health_options.append(health_option)

                row_num = row_num + 1

	# Initialization function
    def __init__(self, csvfile):
        self.health_options = []
        self.__read_csv__(csvfile)
        
    def get_primary_care(self):
        # init empty list
        primary_care = []
        # loop through each health option read from csv earlier
        for health_option in self.health_options:
            # if primary_care is 'Yes', append to list
            if health_option['Primary Care'] == True:
                primary_care.append(health_option)

        return primary_care

if __name__ == '__main__':
    my_health = health_scv("health_scvs.csv")
    
    primary_care = my_health.get_primary_care()
    
    for health_scv in primary_care:
        print(health_scvs['Name'])

