#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Steve S Isenberg
# DATE CREATED: November 15, 2018
# REVISED DATE: November 25, 2018
#                   updated method of splitting pet label out of file name
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
    for i in range(0, len(list_of_filenames), 1):
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it
        # isn't an pet image file
        if in_files[idx][0] != ".":
            if list_of_filenames[i] not in results_dic:
                '''
                Based on Udacity's guidelines the below is NOT plagarism as source
                is cited.
                https://udacity.zendesk.com/hc/en-us/articles/360001451091-What-is-plagiarism-
                # found solution to remove digits at
                # https://stackoverflow.com/questions/12851791/removing-numbers-from-string
                pet_label = ''.join([j for j in list_of_filenames[i] if not j.isdigit()])
                # get rid of any underscores
                pet_label = pet_label.replace('_', ' ')
                '''

                # remove extension [:-4]
                file_name_parts = list_of_filenames[i][:-4]
                # split words and get rid of underscore
                file_name_parts = file_name_parts.split('_')
                # print("\n-------------\nfile_name_parts ", file_name_parts)
                dog_label = ''
                # only keep the parts not containing numbers
                for part in file_name_parts:
                    if part.isalpha():
                        dog_label += part + ' '
                        # print("dog_label |",dog_label,"|")
                # strip whitespace, make lowercase & store as list
                results_dic[list_of_filenames[i]] = [dog_label.strip().lower()]
            else:
                print("Warning: Key={} already exist in results_dic with value = {}".
                  format(list_of_filenames[i], results_dic[list_of_filenames[i]]))
    return results_dic
