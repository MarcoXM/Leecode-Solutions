## Hands on ML - Questions 

1. What is a continuous variable?
2. What is a categorical variable?
3. Provide 2 of the words that are used for the possible values of a categorical variable.
4. What is a "dense layer"?
5. How do entity embeddings reduce memory usage and speed up neural networks?
6. What kind of datasets are entity embeddings especially useful for?
7. What are the two main families of machine learning algorithms?
8. Why do some categorical columns need a special ordering in their classes? How do you do this in pandas?
9. Summarize what a decision tree algorithm does.
10. Why is a date different from a regular categorical or continuous variable, and how can you preprocess it to allow it to be used in a model?
11. Should you pick a random validation set in the bulldozer competition? If no, what kind of validation set should you pick?
12. What is pickle and what is it useful for?
13. How are `mse`, `samples`, and `values` calculated in the decision tree drawn in this chapter?
14. How do we deal with outliers, before building a decision tree?
15. How do we handle categorical variables in a decision tree?
16. What is bagging?
17. What is the difference between `max_samples` and `max_features` when creating a random forest?
18. If you increase `n_estimators` to a very high value, can that lead to over-fitting? Why or why not?
19. What is *out of bag error*?
20. Make a list of reasons why a model's validation set error might be worse than the OOB error. How could you test your hypotheses?
21. How can you answer each of these things with a random forest? How do they work?:
    - How confident are we in our projections using a particular row of data?
    - For predicting with a particular row of data, what were the most important factors, and how did they influence that prediction?
    - Which columns are the strongest predictors?
    - How do predictions vary, as we vary these columns?
22. What's the purpose of removing unimportant variables?
23. What's a good type of plot for showing tree interpreter results?
24. What is the *extrapolation problem*?
25. How can you tell if your test or validation set is distributed in a different way to your training set?
26. Why do we make `saleElapsed` a continuous variable, even although it has less than 9000 distinct values?
27. What is boosting?
28. How could we use embeddings with a random forest? Would we expect this to help?
29. Why might we not always use a neural net for tabular modeling?