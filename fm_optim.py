def calculate_tpr(true_positive, condition_positive):
    return true_positive/condition_positive

def calculate_fpr(false_positive, condition_negative):
    return false_positive/condition_negative

def calculate_prevalence(condition_positive, total_population):
    return condition_positive/total_population

def calculate_m_factor(prevalence, cost_negative, cost_positive): #FIXME: change to one value for both parts of the div on the right of the eq
    return ((1-prevalence)/prevalence)*(cost_negative/cost_positive)

    # (cfp-ctn) -> they are all negatives, so better put them together as a 1 number instead of two (now = cost_negative), what is the cost of mistaking negative for positive
    # (cfn-ctp) -> they are all positives, what is the cost of mistaking postitive for negative, what is the consequence (now = cost_positive)

def calculate_fm(tpr, fpr, m):
    # m = calculate_m_factor()
    return tpr - (m*fpr)

#TODO: decide how costly is it to commit false positive, false negative, and which cost I assign to true positive and true negative

# for the purpose of demo let's assume the following (FIXME:): I have a total population of 300 samples, 200 espresso, 100 drip
# my model calculated the following: 60 drip as drip, 40 drip as espresso; 150 espresso as espresso, 50 espresso as drip

all_coffees = 300
espresso = 200
drip = 100
true_positive_drip = 60
false_positive_espresso = 50
true_negative_espresso = 150
false_negative_drip = 40

tpr = calculate_tpr(true_positive_drip, drip)
fpr = calculate_fpr(false_negative_drip, espresso)
prevalence = calculate_prevalence(drip, all_coffees)
m_factor = calculate_m_factor(prevalence, 10,7) #TODO: add cost estimation, but surely cfp > cfn,
#the other two are the wanted ones; type of coffee not yet acknowledged are cheaper and could be used but if missed hence missing out of profit margine for cheap raw material (how much more cost per unit); for false positive how much financial damage (how much less revenue) to the business
fm = calculate_fm(tpr, fpr, m_factor)

print(f"The Fm value for present confusion matrix is {fm}") # figure out what is the treshold to get the highest fm score, so use this function for choosing treshold,
# use array of tresholds to check the value for each of them and and chose the higest among the ones obtained,
# put into dataframe and sort and take the top value, and then numpy.where to change probabilities to classes and FINITO :)
