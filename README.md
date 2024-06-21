# Motor Imagery based Photo Viewer / HCI project
This project focuses on developing a subject-dependent Brain-Computer Interface (BCI) using EEG data for motor imagery tasks. The interface is trained and tested using EEG data from the same subject to classify two motor imagery classes: right and left hand movements. The project utilizes freely available BCI Competition datasets, particularly the BCIC IV dataset IIa.

# Key Components
1) Dataset: The project uses the BCIC IV dataset IIa, which includes EEG recordings for multiple subjects performing motor imagery tasks.
2) Motor Imagery Classes: Only two classes are considered: right hand and left hand.
3) EEG Preprocessing: Suitable preprocessing techniques are applied to the EEG data to enhance signal quality and ensure accurate feature extraction.
4) Feature Extraction: Common Spatial Patterns (CSP) are used to extract features from the EEG data.
5) Classification: Many classifiers are employed as shown in code
6) Performance Comparison: The performance of the classifiers is compared based on the accuracy achieved.
7) User Interface (UI): A UI is designed to present a set of photos to the user. The user can navigate through the photos using arrows representing left and right movements. The detected motor imagery class determines the navigation direction (previous or next photo).

# Results
Results for at least one subject are included, showcasing the classification accuracy of the implemented models.

# Datasets
I included the datasets, which was originally here https://github.com/bregydoc/bcidatasetIV2a  
The datasets is IV2a, the description is here https://www.bbci.de/competition/iv/desc_2a.pdf  
This is link to BCI Competition IV https://www.bbci.de/competition/iv/ which contains above page

# How to Run the GUI for Motor Imagery Based Photo Viewer
## Prerequisites :
 
Before you begin, ensure you have the following installed on your system:
- Python 3.7 or higher
-  Required Python packages (listed in requirements.txt)
   
## Step-by-Step Instructions
1) Clone the Repository 
Clone the repository to your local machine using the following command:

```python
git clone https://github.com/fatma-ahmed19/motor-imagery-photo-viewer.git
cd motor-imagery-photo-viewer
```
2) Run the GUI Application

Execute the following command to start the GUI:
```python
python gui_app.py
```
# Detailed GUI Usage
1) Launching the Application

When you run the gui_app.py script, a window will pop up. This is the main interface of the application.

2) Applying Predictions

  - Step 1: Click the "Apply Prediction" button to start the prediction process.
  - Step 2: Observe the button's color change when it matches the predicted outcome (next image).
    
3) Viewing Predictions

   - The application will display the predicted outcome and the next image accordingly.
   - Continue clicking "Apply Prediction" to view subsequent predictions.

4) Exiting the Application

Close the window or press the designated exit button within the application to terminate the GUI.

5) Troubleshooting

    - If the GUI does not launch, ensure all dependencies are correctly installed.
    - Verify you are using the compatible version of Python.
    - Check for any error messages in the terminal and refer to the FAQ or open an issue in the repository for assistance.

