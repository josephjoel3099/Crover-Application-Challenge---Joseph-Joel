# Instructions:
1.	***Please ensure that python 3.8 is installed.***
2.	Run x_ekf.py
    ```
    python3 x_ekf.py
    ```
    **Check if file x.csv is created in the folder**
3. Run x_ekf.py
    ```
    python3 y_ekf.py
    ```
    **Check if file y.csv is created in the folder**
4. Run car.py
   ```
   python3 car.py
   ```
5. Visualize the localization through animated plot.

# Technical Description
1. Localization is done using **Extended Kalman filter** (EKF).
2. Code requires more tuning for both X and Y position. This can be done in both x_ekf.py and y_ekf.py files.
3. Code is separated into 3 files. Can be merged into one and can be improved by using functions. 
4. Handling CSV files can be streamlined by having all data in one file.

# Results
Black line represents true path of the car.
Green dots represents estimated position of the car.
Red line represents estimated path of the car.
![Figure_1](https://user-images.githubusercontent.com/65588195/130364490-94a9e5be-d7e1-4f7c-b4fd-e1e733bcd0fe.png)

Black line represents true path of the car.
Red line represents estimated path of the car.
![Figure_2](https://user-images.githubusercontent.com/65588195/130364651-3481043a-0ab7-470b-b557-36aff176336e.png)

Red line represents estimated path of the car.
![Figure_3](https://user-images.githubusercontent.com/65588195/130364719-e66efe7f-b895-43cb-83d2-74a070da45d3.png)

