#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER:
# DATE CREATED:
# REVISED DATE:
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function

    list_of_filenames = listdir(image_dir)
    results_dic = dict()

    # Print 10 of the filenames from folder pet_images/ - for testing
    ''' *** FOR TESTING ***
    print("\nPrints 10 filenames from folder pet_images/")
    for i in range(0, 10, 1):
        print("{:2d} file: {:>25}".format(i + 1, list_of_filenames[i]) )
    '''

    for i in range(0, len(list_of_filenames), 1):
      if list_of_filenames[i] not in results_dic:
          # found solution to remove digits at
          # https://stackoverflow.com/questions/12851791/removing-numbers-from-string
          pet_label = ''.join([j for j in list_of_filenames[i] if not j.isdigit()])
          # get rid of any underscores
          pet_label = pet_label.replace('_', ' ')
          # remove extension [:-4], strip whitespace, make lowercase
          results_dic[list_of_filenames[i]] = [pet_label[:-4].strip().lower()]
      else:
          print("Warning: Key={} already exist in results_dic with value = {}".
            format(list_of_filenames[i], results_dic[list_of_filenames[i]]))
    return results_dic


def main():
    results_dic = get_pet_labels('pet_images/')
    for key, value in results_dic.items():
        print("key = {} | value = [{}]".format(key, value))
    # print(results_dic)


# Call to main function to run the program
if __name__ == "__main__":
    main()