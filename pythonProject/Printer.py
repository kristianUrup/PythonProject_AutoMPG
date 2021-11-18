import DataStore as ds
import DataService as dService


def print_dataset(housing):
    print("Housing head is: ")
    print(housing.head)
    print("\n")


def print_ocean_proximity_info(housing):
    ocean_proximity_info = housing["ocean_proximity"].value_counts()
    print("The Values for ocean proximity")
    print(ocean_proximity_info)
    print("\n")


def print_describe(housing):
    print("The describe method")
    print(housing.describe())
    print("\n")


def print_train_test_set(train_set, test_set):
    print(len(train_set), "train 80% +", len(test_set), " test 20%")
    print("\n")