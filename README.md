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

*Estimated position data is recorded to a csv after the car.py script runs.*

![Figure_4](https://github.com/josephjoel3099/Crover-Application-Challenge---Joseph-Joel/blob/7f9ce33a3c2bee8724559634681d4f55860d2177/additional_files/ekf.gif)

# Work Description
The task was very challenging and interesting. I had a lot of fun making scripts. Localization is a very important part in robotics and in my experience this is where we realize that in practice a lot of noise and other factors come into place. Whereas, in theory it is easy to understand. It is simply the systems ability to know where it is with respect to a frame of origin. I started with the mindset of since rosbag file is given the best way to do is with ROS. But I realised it is not that straight forward. I have no experience in using rosbag files. I recently learnt that we can record and play data using rosbags and visualize in rviz. I then moved to python. It was clear that I have two sensor data (GNSS and Odometry) and therefore there is a need for sensor fusion to get a good localization. I have learnt in theory that EKF is the way to fuse two data. What I have understood is that the sensors give same data with different levels of accuracy with different frequency. The first thing to note is that the total number of data are different. With this basic understanding I started writing the script. Listing issues faced  and new things learnt during the course of the challenge:
1. Learnt about UNIX time and how to convert to normal timestamp.
2. Had issues getting values from csv files, especially import float values. Learnt how to import data using pandas and fixed the importing issue.
3. Had issues with implementing EKF with the given data files. Read a bit about the filter to refresh and managed to tune the params to a certain level. Still require a good understanding of the concept.
4. I already knew about EKF and UKF but also learnt that there are other types of KFs and filters.
5. Had issues with animating the plot where the plot did not show any points on the plot. It was a logical error in indexing the array. Fixed it after finding the error.
6. Had issue with plotting the estimated path. Hacked up a solution to smooth out the curve. I believe that it will be fixed once the EKF params are tunned properly.
7. Learnt a lot about EKF.



## Reference
1. https://github.com/AtsushiSakai/PythonRobotics/blob/916b4382de090de29f54538b356cef1c811aacce/Localization/extended_kalman_filter/extended_kalman_filter.py
2. https://medium.com/@jaems33/understanding-kalman-filters-with-python-2310e87b8f48
3. https://dingyan89.medium.com/simple-understanding-of-kinematic-bicycle-model-81cac6420357
4. https://stackoverflow.com/questions/54145894/from-csv-file-convert-unix-timestamp-of-first-column-into-year-and-create-a-gra
5. https://www.geeksforgeeks.org/python-pandas-dataframe/
6. https://stackoverflow.com/questions/10952060/plot-ellipse-with-matplotlib-pyplot-python
7. https://progr.interplanety.org/en/python-how-to-find-the-polygon-center-coordinates/
