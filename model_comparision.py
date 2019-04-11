from inherently_multiclass import *
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
names=['naive_bayes_cv_with_log',
'naive_bayes_cv_selected_feature',
'naive_bayes_cv_with_all',
'naive_bayes_cv_without_log',
'knn_all',
'knn_without_log'
'knn_with_log',
'knn_selected_feature',
'naive_bayess_with_all',
'naive_bayess_without_log',
'naive_bayess_with_log',
'naive_bayess_selected_feature',
'multi_logistic_with_all',
'multi_logistic_without_log',
'multi_logistic_with_log',
'multi_logistic_selected_feature',
'multi_logsitc_cv_with_all',
'multi_logsitc_cv_with_log',
'multi_logsitc_cv_without_log',
'quadratic_discriminant_analysis_without_log',
'quadratic_discriminant_analysis_with_log',
'ridge_classfier_cv_withoulog',
'ridge_classfier_cv_withlog',
'support_vector_classfication_withlog',
'support_vector_classfication_withoutlog',
'gauss_process_with_log',
'gauss_process_without_log',
'one_vs_rest_gauss_process_with_log',
'one_vs_rest_multi_logistic_with_log',
'one_vs_rest_multi_logistic_without_log',
'one_vs_rest_multi_logsitc_cv_with_log',
'one_vs_rest_multi_logsitc_cv_without_log',
'sgd_classifer_without_log',
'sgd_classifer_with_log',
'perception_withlog',
'perception_withoutlog',
'decosion_tree_withlog',
'decosion_tree_withoutlog',
'ridge_classfier_cv_selected_feature',
'one_vs_rest_multi_logisitc_selected_feature',
'quadratic_discriminant_analysis_selected_feature',
'sgd_classifer_selected_feature',
'perception_selected_feature',
'decosion_tree_selected_feature']

naive_bayes_cv_selected_feature()
naive_bayes_cv_with_all()
naive_bayes_cv_without_log()
knn_all()
knn_without_log()
knn_with_log()
knn_selected_feature()
naive_bayess_with_all()
naive_bayess_without_log()
naive_bayess_with_log()
naive_bayess_selected_feature()
multi_logistic_with_all()
multi_logistic_without_log()
multi_logistic_with_log()
multi_logistic_selected_feature()
multi_logsitc_cv_with_all()
multi_logsitc_cv_with_log()
multi_logsitc_cv_without_log()
quadratic_discriminant_analysis_without_log()
quadratic_discriminant_analysis_with_log()
ridge_classfier_cv_withoulog()
ridge_classfier_cv_withlog()
support_vector_classfication_withlog()
support_vector_classfication_withoutlog()
gauss_process_with_log()
gauss_process_without_log()
one_vs_rest_gauss_process_with_log()
one_vs_rest_multi_logistic_with_log()
one_vs_rest_multi_logistic_without_log()
one_vs_rest_multi_logsitc_cv_with_log()
one_vs_rest_multi_logsitc_cv_without_log()
sgd_classifer_without_log()
sgd_classifer_with_log()
perception_withlog()
perception_withoutlog()
decosion_tree_withlog()
decosion_tree_withoutlog()
ridge_classfier_cv_selected_feature()
one_vs_rest_multi_logisitc_selected_feature()
quadratic_discriminant_analysis_selected_feature()
sgd_classifer_selected_feature()
perception_selected_feature()
decosion_tree_selected_feature()
plt.figure(figsize=(50,50))
plt.suptitle('comparrasion for models')

frame=pd.DataFrame(
    {'train_accurancy':train_score,
    'test_accurancy' :test_score
    },index=names)
frame.plot(kind='barh')

plt.show('comparrasion_for_models.png')








