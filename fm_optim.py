def calculate_prevalence(condition_positive, total_population):
    return condition_positive/total_population

def calculate_m_factor(prevalence, cost_negative, cost_positive):
    return ((1-prevalence)/prevalence)*(cost_negative/cost_positive)


def calculate_fm(tpr, fpr, m):
    return tpr - (m*fpr)