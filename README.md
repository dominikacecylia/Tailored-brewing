# Tailored-brewing

The principal project goal is to decide on coffee brewing method based on collected parameters. This is motivated by a business goal of the client, who is a chain of specialty brewers. The client wants to place orders for coffee beans based on the intended brewing method.

![client profile]('client_profile.PNG')

## Usage:
In order to use the coffee classifier:
1. If you want to use project data:
    - start with tailored_brewing_eda.ipynb - this notebook contains exploratory data analysis and initial data modelling, which will help you understand the dataset and it's variables
    - continue with tailored_brewing_classification.ipynb - this notebook splits the data into train, validation and test, tries different learners and uses Decision tree classifier to do the final data classification
    - file 'data\coffee_desk_dataset_ead_selected.csv' is the one used for classification
    - additionally there are:
        - fm_optim.py - file with defined methods for threshold optimisation
        - 'data\coffee_desk_dataset_ead.csv' and 'data\coffee_desk_dataset_clean.csv' - two files with data used for analysis and modelling, you can reuse them and try using different variables for modelling
2. If you want to use your own data:
    - tailored_brewing_eda.ipynb - can be reused for data analysis, you will only need to change names of the variables, also noting that data used originally was all categorical
    - continue with tailored_brewing_classification.ipynb - where you can use your data following logical order in the notebook, and maybe changing the hyperparameters and costs assigned to false positive (type 1 error) and false negative (type 2 error)



## License:
[MIT License](https://choosealicense.com/licenses/mit/)