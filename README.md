# Motor Imagery based Photo Viewer / HCI project
This project focuses on developing a subject-dependent Brain-Computer Interface (BCI) using EEG data for motor imagery tasks. The interface is trained and tested using EEG data from the same subject to classify two motor imagery classes: right and left hand movements. The project utilizes freely available BCI Competition datasets, particularly the BCIC IV dataset IIa.

#Key Components
1.Dataset: The project uses the BCIC IV dataset IIa, which includes EEG recordings for multiple subjects performing motor imagery tasks.
2.Motor Imagery Classes: Only two classes are considered: right hand and left hand.
3.EEG Preprocessing: Suitable preprocessing techniques are applied to the EEG data to enhance signal quality and ensure accurate feature extraction.
4.Feature Extraction: Common Spatial Patterns (CSP) are used to extract features from the EEG data.
5.Classification: Many classifiers are employed as shown in code
6.Performance Comparison: The performance of the classifiers is compared based on the accuracy achieved.
7.User Interface (UI): A UI is designed to present a set of photos to the user. The user can navigate through the photos using arrows representing left and right movements. The detected motor imagery class determines the navigation direction (previous or next photo).

#Results
Results for at least one subject are included, showcasing the classification accuracy of the implemented models.
