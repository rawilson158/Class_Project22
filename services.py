import json
import csv


class services:
    def __init__(self, name, website, description, location, phone, email):
        self.name = name
        self.website = website
        self.description = description
        self.location = location
        self.phone = phone
        self.email = email
        

class housing_scvs(services):
    def __init__(self, name, website, description, location, phone, email, income, duration, single_occupancy, comm_housing):
        super().__init__(name, website, description, location, phone, email)        
        self.income = income
        self.duration = duration
        self.single_occpancy = single_occupancy
        self.comm_housing = comm_housing


class job_scvs(services):
    def __init__(self, name, website, description, location, phone, email, full_time, part_time, temporary, permanent):
        super().__init__(name, website, description, location, phone, email)  
        self.full_time = full_time
        self.part_time = part_time
        self.temporary = temporary
        self.permanent = permanent


class health_scvs(services):
    def __init__(self, name, website, description, location, phone, email, primary_care, insurance):
        super().__init__(name, website, description, location, phone, email)
        self.primary_care = primary_care
        self.insurance = insurance








    