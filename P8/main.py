# my-login: jpoconnell2
# partner-login: tgraczyk

import json, sys
from collections import namedtuple
import copy


def read_json(json_filename):
    data_json = open(json_filename)
    data = json.load(data_json)
    return data


# Function that takes in a dictionary for a particular car and a field
# to be searched and returns the value of the field. NOTE: Code this
# function using recursion
def get_value(car, field):
    global exit
    global desired
    desired = None
    exit = False
    for key in car:
        if exit:
            continue
        elif key == field:
            exit = True
            desired = car[key]
        elif type(car[key]) == dict:
            get_value(car[key], field)
    return desired


# This function takes in the jdata returned by read_json function
# and makes namedtuple objects from each of the car dictionaries.
# This function should return a list of namedtuple objects corresponding
# to each car in jdata. Use the get_value function to get values of the
# different fields
def make_namedtuple_list(jdata):
    car_list = []
    car_tuple = namedtuple("Car", ("id", 'make', 'model', 'year', 'transmission'))
    for car in jdata:
        i = car_tuple(car, get_value(jdata[car], 'Make'), get_value(jdata[car], 'Model'), get_value(jdata[car], 'Year'), get_value(jdata[car], 'Transmission'))
        car_list.append(i)
    return car_list


    return None # TODO


# This function takes in the list of namedtuple cars returned by
# make_namedtuple_list function and then filters them based on the
# fields specified in the filters dictionary
def filter_cars(cars, filters):
    # start with list of cars
    car_list = cars
    temp_list = copy.deepcopy(car_list)
    if 'make' in filters:
        for car in car_list:
            if car.make != filters['make']:
                temp_list.remove(car)
    if 'model' in filters:
        for car in car_list:
            if car.model != filters['model'] and car in temp_list:
                temp_list.remove(car)
    if 'year' in filters:
        for car in car_list:
            if car.year != filters['year'] and car in temp_list:
                temp_list.remove(car)
    return temp_list



    # for each key in the filter go through the list and remove the stuff that doesn't have that value


    # filtered_make = []
    # filtered_model = []
    # filtered_year = []
    # final_list = []
    # global s
    # s = 0
    # if 'make' in filters:
    #     for car in cars:
    #         if car.make == filters['make']:
    #             filtered_make.append(car)
    # if 'model' in filters:
    #     for car in cars:
    #         if car.model == filters['model']:
    #             filtered_model.append(car)
    # if 'year' in filters:
    #     for car in cars:
    #         if car.year == filters['year']:
    #             filtered_year.append(car)
    #
    # for i in range(len(cars)):
    #     if len(filtered_make) == 0 and len(filtered_model) == 0:
    #         final_list = filtered_year
    #     elif len(filtered_year) == 0 and len(filtered_model) == 0:
    #         final_list = filtered_make
    #     elif len(filtered_make) == 0 and len(filtered_year) == 0:
    #         final_list = filtered_model
    #     elif len(filtered_make) == 0:
    #         if cars[i] in filtered_model and filtered_year:
    #             final_list.append(cars[i])
    #     elif len(filtered_model) == 0:
    #         if cars[i] in filtered_make and filtered_year:
    #             final_list.append(cars[i])
    #     elif len(filtered_year) == 0:
    #         if cars[i] in filtered_make and filtered_model:
    #             final_list.append(cars[i])
    #     else:
    #         if cars[i] in filtered_make and filtered_model and filtered_year:
    #             final_list.append(cars[i])
    #
    # return final_list

# This function takes in the commandline arguments and calls the
# respective functions above. The function has been coded to take in
# the arguments and call the function stubs. As you complete the
# functions above this function will call them and you can see your
# grade change
def process_args(args):
    # parse commandline inputs
    if len(args) < 2:
        print("USAGE: python main.py <json file> <command> <args for command>")
        return None
    command = args[2]
    print('Command: ' + command)

    jdata = read_json(args[1])
    if jdata == None:
        print('Please implement read_json first')
        return None

    # execute car commands
    if command == "read_json":
        return jdata

    elif command == "get_value":
        car_id = args[3]
        field = args[4]
        value = get_value(jdata[car_id], field)
        return value

    elif command == "make_list":
        car_list = make_namedtuple_list(jdata)
        for car in car_list:
            print(car)

    elif command == "filter":
        filters = {}
        for pair in args[3].split(','):
            pair = pair.split('=')
            assert(len(pair) == 2)
            filters[pair[0]] = pair[1]
        cars_list = make_namedtuple_list(jdata)
        filtered_cars = filter_cars(cars_list, filters)
        for car in filtered_cars:
            print(car)

    else:
        print("Unkown command: " + command)

    return None




def main():
    result = process_args(sys.argv)
    if result != None:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
