# Tailored-brewing

The principal project goal is to decide on coffee brewing method based on collected parameters. This is motivated by a business goal of the client, who is a chain of specialty brewers. The client wants to place orders for coffee beans based on the intended brewing method.

![client profile]('client_profile.PNG')

Data is composed of coffee details such as:
- region of origin
- roast
- processing methods
- blend
- and target variable: **brewing method**

The idea is for the client to be able to order coffee beans for specialty brewing based on their parameters, hence finding new coffee suppliers and potentially expanding business to new locations, to offer wider range of specialty coffees to a wider public.
Given the client's profile, it is especially important to make sure that selected coffee is indeed appropriate for specialty brewing, as damaging brand due to bad experience of a customer is higher than the risk of missing out on cheaper raw material. Nevertheless, both costs of such situations were considered in optimizing the model.
Model success is evaluated using **PPV (positive predictive rate)** metric, which makes sure that coffee offerred by the client is only the specialty beans.

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

## Results:

Some of the variables, such as roast and blend were omitted in the data classification, given their direct correlation to the target variable.
The best score was 72% on validation data, which is pretty decent but still short of assuring the client with placing orders on new beans.
Moreover, it is recommended that the client does not rely on the machine learning solution, as it is enought to order pure blends and light or medium roast of beans and such coffee will be good for specialty brewing. More factors such as processing methods surely influence the flavor, and could be used to look for particular taste notes in coffee, but the problem is easier than originally supposed and ML algorith does not contribute enough to be worthy of further development for this particular client whith his business goal.

## License:
[MIT License](https://choosealicense.com/licenses/mit/)