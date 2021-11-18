import pandas as pd
import DataStore as ds
import DataService as dService
import Printer as printer

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

DataSet = []
Housing = []

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ds.fetch_housing_data(housing_url=ds.HOUSING_URL, housing_path=ds.HOUSING_PATH)
#    ds.fetch_automobile_data(automobile_url=ds.AUTOMOBILE_URL, automobile_path=ds.AUTOMOBILE_PATH)
    housing = ds.loading_housing_data(housing_path=ds.HOUSING_PATH)
    Housing = housing
    DataSet = housing.head()
    housing.reset_index()
    printer.print_dataset(housing)
    printer.print_describe(housing)
    printer.print_ocean_proximity_info(housing)

    # split the train set into test and train set
    housing_by_id = housing.reset_index()
    train_set, test_set = dService.split_train_test_by_id(housing_by_id, 0.2, "index")

    printer.print_train_test_set(train_set, test_set)

    automobiles = ds.loading_housing_data()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
