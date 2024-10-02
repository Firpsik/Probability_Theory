import datas as d
import numpy as np

def chosen_mean():
    mean_manual = sum(d.data) / n
    return mean_manual

def fix_dispersion():
    variance_sum = 0
    for x in d.data:
        variance_sum += (x - mode_manual) ** 2

    variance_manual = variance_sum / (n - 1)
    return variance_manual

def find_mode():
    freq_dict = {}
    for num in d.data:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    mode_value = max(freq_dict, key=freq_dict.get)
    return mode_value

def find_median():
    if n % 2 == 0:
        median_manual = (d.data_sorted[n//2 - 1] + d.data_sorted[n//2]) / 2
    else:
        median_manual = d.data_sorted[n//2]
    return median_manual

def find_excess():
    skewness_sum = 0
    for x in d.data:
        skewness_sum += ((x - mean_manual) / np.sqrt(variance_manual)) ** 3
    
    skewness_manual = skewness_sum / n
    return skewness_manual

def find_assimetr():
    kurtosis_sum = 0
    for x in d.data:
        kurtosis_sum += ((x - mean_manual) / np.sqrt(variance_manual)) ** 4

    kurtosis_manual = kurtosis_sum / n - 3
    return kurtosis_manual 

n = len(d.data)
mean_manual = chosen_mean()
mode_manual = chosen_mean()
variance_manual = fix_dispersion()