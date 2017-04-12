# Smart-Home-With-Integrated-Security-Features-And-Support-For-Deaf-and-Elderly-People





A Project Report on


Modulo Smart Home


Submitted in partial fulfillment of the requirements for the degree of

BACHELOR OF TECHNOLOGY

in

Computer Science and Engineering

by
Ann Martin     1317157

Ankit Kumar   1317188

T. Keerthana    1317191



Under the Guidance of

Bijeesh T. V.



Department of Computer Science and Engineering

Faculty  of Engineering, Christ University, Kumbalagudu, Bengaluru - 560 026

November-2016







Faculty of Engineering

Department of Computer Science and Engineering




CERTIFICATE



This is to certify that Ann Martin,  Ankit  Kumar, T. Keerthana have successfully completed the project work entitled “Modulo Smart  Home” in partial fulfillment for the award of Bachelor of Technology in Department of Computer Science and En- gineering during the year 2016-2017.





Bijeesh T. V.

Assistant Professor




Dr. K. Balachandran                                   Dr. Iven Jose

Head of Department                                         Associate Dean







Faculty of Engineering

Department of Computer Science and Engineering




BONAFIDE  CERTIFICATE



It is to certify that this project titled ”Modulo Smart Home” is the bonafide work of





Name           Register  Number

Ann Martin           1317157

Ankit Kumar          1317188

T. Keerthana           1317191







Examiners  [Name and Signature]           Name of the Candidate :

1.                                                                Register Number :

2.                                                                Date of Examination :


Acknowledgement



We would like to thank Christ University Vice Chancellor, Dr.  Rev.  Fr. Thomas  C Mathew, Pro Vice Chancellor,Dr. Rev. Fr. Abraham, Director of Faculty of Engineer- ing, Fr. Benny Thomas and the Associate Dean Dr. Iven Jose for their kind patronage.



We would like to express our sincere gratitude and appreciation to the HOD of Depart- ment of Computer Science and Engineering, Faculty of Engineering Dr. K. Balachan- dran,  for giving us this opportunity to take up this project.



We  are also extremely grateful to our guide, Bijeesh T. V., who has supported and helped to carry out the project. His constant monitoring and encouragement helped us keep up to the project schedule.




We  would like to thank all faculty and non-teaching staff who have helped us in de- signing and giving a structure to our project, especially the lab assistants of Department of Electronics and Communication who allowed us to utilize the lab equipments even at odd hours.  We  thank our parents who supported and motivated us throughout the project.












Declaration



We, hereby declare that the Project titled “Modulo Smart  Home” is a record of orig- inal project work undertaken by us for the award of the degree of Bachelor of Tech- nology in Department of Computer Science and Engineering.   We have completed this study under the supervision of Bijeesh T. V., Department of Computer Science and Engineering, .



We also declare that this project report has not been submitted for the award of any degree, diploma, associate ship, fellowship or other title anywhere else. It has not been sent for any publication or presentation purpose.

Place: Faculty of Engineering, Christ University, Bengaluru
Date: 08-03-2017


Name           Register  Number               Signature


Ann Martin             1317157


Ankit Kumar            1317188


T. Keerthana            1317191


Abstract




In recent times, the older generations find it difficult to adapt to the rising growth of the smart work applications that are now dominating the world in every aspect of life. A rapid decrease in sensation in the sense organs is often noted in people as they age. For the deaf and the elderly who find it hard to hear, it is not easy to know when someone is at the door and ringing the doorbell. It is also common to overlook switching off a light bulb.  Our health depends on various factors – heart rate, blood pressure, sugar and cholesterol levels, etc. and any change in these vital signs may cause harm, even death. Due to inappropriate life style, many people have developed anomalies especially related to the heart forcing them to undergo expensive treatments if left unnoticed. For this purpose, digital equipments can be beneficial. A well equipped person will respond to the environment promptly. With this objective, we have devised a model for a deaf person who cannot hear the door bell, but can know when a person arrives, if a vibrating device or vibrator is attached to their body (using sense of touch).  A pulse sensor is attached to the person’s body in a similar way - a wrist band or a watch. A green LED light glows showing that the pulse rate of the person is normal. If the pulse drops below the normal heart rate, it alerts the user with a red alert LED light, which is embedded in the watch/wristband. A centralized computer system- in our project the Raspberry Pi- helps to control the domestic electric devices operated using an Android application over a Cloud network. A 24 x 7 information on the devices available in the house as buttons on the dashboard that can be used to toggle on or off over the Internet. All these features are employed into our project.









Contents





CERTIFICATE                                                                                                       i BONAFIDE CERTIFICATE                                                                                 ii ACKNOWLEDGEMENT                                                                                      iii

DECLARATION                                                                                                      iv

ABSTRACT                                                                                                                   v



LIST OF FIGURES                                                                                                   viii LIST OF TABLES                                                                                                        ix GLOSSARY                                                                                                                   x
1   INTRODUCTION                                                                                               1

1.1
Problem Identification   . . . . .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
2
1.2
Problem Formulation  . . . . . .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
2
1.3
Problem Statement & Objectives
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
3
1.4
Limitations   . . . . . . . . . . .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
3

2   LITERATURE SURVEY AND REVIEW                                                             4

2.1
Literature Collection & Segregation   .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
4
2.2
Critical Review of Literature  . . . . .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
6

3   ACTUAL WORK                                                                                                     7

3.1
Methodology for the Study  . . . . . . . . . . . . . . . . . . .
.
.
.
.
.
10
3.2
Experimental and/or Analytical Work Completed in the Project
.
.
.
.
.
10
3.3
Modeling, Analysis & Design   . . . . . . . . . . . . . . . . .
.
.
.
.
.
10
3.4
Prototype & testing  . . . . . . . . . . . . . . . . . . . . . . .
.
.
.
.
.
10

4   RESULTS, DISCUSSIONS AND CONCLUSIONS                                           13

4.1
Results & Analysis  . . . . . . . . . . . . . . . .
.
.
.
.
.
.
.
.
.
.
.
.
13
4.2
Comparative Study  . . . . . . . . . . . . . . . .
.
.
.
.
.
.
.
.
.
.
.
.
13




4.3
Discussions  . . . . . .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
13
4.4
Conclusions . . . . . .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
17
4.5
Scope for Future Work
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
18



BIBLIOGRAPHY




















































19

PUBLICATION DETAILS





















































21


A   Appendix A Title






















































22
A.1   Appendix A Section 1 .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
22
A.1.1   Appendix A Subsection for Section
1
.
.
.
.
.
.
.
.
.
.
.
.
.
.
22
A.2   Appendix A Section 2 . . . . . . . . . . . .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
22

B   Appendix B Title                                                                                                    23
B.1
Appendix B Section 1 .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
23
B.2
Appendix B Section 2 .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
23
B.3
Appendix B Section 3 .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
23

Index                                                                                                                             24









LIST OF FIGURES




3.1
Arduino Uno
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
7
3.2
Transmitter   .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
8
3.3
Receiver . . .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
8
3.4
Vibrator  . . .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
9
3.5
Pulse Sensor Model
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
9
3.6
Relay Board . . . .
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
10










LIST OF TABLES




3.1    Student Marks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    10











Chapter 1




INTRODUCTION





There are three modules included in this project. These are: Home Security for the Deaf and the Elderly people, Health inspection and Computerization of Home Appliances.

The first module is Home Security for the Deaf and the Elderly people.  Nowadays, physically impaired or an elderly person will find it very difficult to keep pace with, without being crushed. The aim of our project is to propose a wireless system that per- mits elderly people with physical challenges, in particular, handicapped and disabled people, to adjust to their preferred devices without moving around much. For this pur- pose, digital equipments can be beneficial. A well equipped person will respond to the environment promptly. With this objective, we have devised a model for a deaf person to know when a person is at the door and ringing the door bell. A deaf person cannot hear the door bell, but can do so if a vibrating device or vibrator is attached to their body (using sense of touch).

Sensor device senses the object and data is stored in microcontroller and after that the data is transmitted to the receiver device using RF circuits. Receiver device will catch the transmitted signal data from the sensor. This is a wireless transmission. If a person comes near the door the device will vibrate so that the person will be alert by the means of vibration and message which are displayed on the computer screen. The device is connected to a database so that the person can track who visited his/her home later.

The second module is health inspection where a pulse sensor is attached to the person’s body in a similar way - a wrist band or a watch. A green LED light glows showing that the pulse rate of the person is normal. If the pulse drops below the normal heart rate, it alerts the user with a red alert LED light, which is embedded in the watch/wristband.


The third module describes the usage of a Centralized computer system- in our project Raspberry Pi- to control the domestic electric devices such as light, fan and tempera- ture through remote operated using an Android application over a Cloud network. The switches of the electrical switchboard are available on the application dashboard and can be toggled on or off over the Internet. Android application will work as a remote control. Automation of the house or office is required with advancement of electronics and communication.



1.1    Problem Identification



Diminishing memory and feeling in the senses is notable in the old people. It gets hard to see, hear, smell and notice new changes nearby and recall them immediately. The deaf and the elderly do not find it easy when someone arrives at home. The door bell is left unanswered. If the owner is not at home, and some important guests visited and left upon finding the door locked, the person will never come to know about this episode.

Visiting the doctor to do a regular check-up is usually good for health.  Often in the present time, due to busy schedules and pressure of a lot of work, many overlook their health, which makes way for the formation of a variety of abnormalities in body. These lead to bigger issues later, and the medication costs multiply.

Forgetfulness is human nature and in our busy life, it is very easy to ignore a few but significant tasks.  When the electricity bill arrives, the realization comes with it.  A reminder is not enough sometimes.



1.2    Problem Formulation



A design to alert the deaf and the elderly of the presence of a visitor can solve this problem. The circuit can consist of a vibrator that will notify by vibrating in a wrist band or box form. A message on the mobile phone or the computer screen is another solution. Outside the house, a device with a camera that can capture image when somebody turns up on the door, and send a message to the owner reporting the arrival, will be of great assistance.

Biomedical sensors are a key to monitor the health of patient constantly and also report any irregularity.


1.3    Problem Statement & Objectives



Here, we have understood that elderly people and the deaf require different services from the normal people.  We need a system that is user friendly and provides for the need for alertness in the elderly and the deaf, the health care of people and a control of all electronic and electrical devices at home. The plan is to realize this system through Internet of Things (IoT), and an electronic tool to manage the coordination among the different equipments utilized. The objectives are stated below:


1. To equip our targeted audience with the latest gadgets so that they can be com- fortable and keep up with the speed of the world.

2. To monitor the health of a heart patient or even a normal person.

3. To build a system that can provide home automation to people, with or without special needs, so they can control their home appliances even when they are not at home, through the Internet.



1.4    Limitations



The Internet speed varies from user to user. Higher the speed, better the message trans- mission and the working of our model is successful. Another concern is that the image captured should be sent over the internet safely. Better algorithms to measure, detect and record the heart beat anomalies, can be created. There are no applications available to send direct message to the user informing them with the photo of the visitor.











Chapter 2




LITERATURE SURVEY AND REVIEW




For understanding the procedural analysis and the materials required for our project, we studied different journal articles, books and gathered important statistics and infor- mation from the concerned websites. Since a lot of information is available online, we tried to separate our problem specific needs from the rest of the records.



2.1    Literature Collection & Segregation



Robert I. Damper et al [1] paper describes an alert system which can notify a deaf/blind person of the occurrence of a lesser number of various domestic sounds has been defined such as doorbell, telephone or an alarm to inform his/her about the basis of any such sound consisting of a static location audio-analysis and recognition unit (ARU) which, on noticing and knowing a specific environmental sound, transmits information by radio to a vibrating portable unit (PU) worn by the deaf/blind person.

The three modules used in this paper are RF module, FPGA and different cryptographic algorithms. These transmit data from the intelligent system using wireless transmission methods- Bluetooth and ZigBee. B. Murali Krishna et al [2] elucidates the encryption process to restrain unwelcome unauthorized access and excessive noise.

Smitha. M et al [3] involves the operation of home appliances for physically challenged people by designing a device using Micro electromechanical Systems (MEMS) accelerometer to sense the accelerations of a hand in motion and RF to transmit the wireless protocol. The Receiver has stored the templates of received gestures and the hand gestures shown by the visually challenged is recognized and compared. The stored template pairs with the received inputs then the LCD displays the comments in regard to the home appliances controlled.

Girija Sankar Dash et al [4] has designed a device which is used as a communication aid for deaf and dumb by using vibrators attached to their body in the form of some wrist band or a watch using RF transmitter and RF receiver. And the entire system is wireless and can work effectively within a radius of 50m. Hence they named the device as WiBeD2 (Wireless Bell for Deaf and Dumb).

Pushpanjali Kumari et al [5] paper describes about the device which is effective in manner, reliable, easy to use and also improves the security of the user. The device is designed for especially deaf and dumb people to notify doorbell ringing who live alone in their house based on using raspberry pi includes camera, vibrator, wireless GSM and Bluetooth. Using GSM technology the message is sent to the owner along with visitors image with date and time is sent to the server for retrieving information later

Strengthening a patient-doctor bond over the distance using a real-time remote consultation service is a new way to address health care issues of general population. This is also popularly termed as “Telemedicine”, and the MCDL (Medical Component Design Laboratory) supports the student projects for the same. This paper by Steve Warren et al [6] involves the use of wearable and other light emitting sensors to illustrate the continuous monitoring of patient data.

Alexandros Pantelopoulos et al [7] have shown a wearable health monitoring device that encloses a number of biosensors that collect data from the patient’s body and sends it to a main control block. This is a GUI which communicates through control signals and also connects to the inmate’s database and sends alert signals to the concerned members. The concept of body area network is used here. It describes the different biosensors and how each detects and sends data.

Adrian Burns et al [8] reports their wireless, sensor-enabled platform named SHIMMER, as a flexible, intelligent, sensing platform that offers sensor readings and its storage, with its diverse sensing and connection capabilities. A micro SD Flash socket is given in SHIMMER, which allows faster signal exchange back and forth. Power is managed in SHIMMER with a board of different buttons, each having its function related to the power supply demanded according to the state conditions. The components as the USB reader, charging or the programming dock, battery charger, daughterboards, etc. comprise the peripherals of the SHIMMER design. Because of the success of the trials in biomedical research, the TRIL centre has approve of SHIMMER design and recommended it for further use in medical applications.

H. Harry Asada, et al [9] have shown about wearable biosensors will permit continuous cardiovascular monitoring in a number of novel settings and also in this article they had focused both technical and clinical issues of the wearable biosensor and combines with miniaturized data acquisition features with advanced photoplethysmographic (PPG) techniques to acquire data related to the patient’s cardiovascular state using a method that is far superior to existing fingertip PPG sensors. Secondly, it addresses based on the ring sensor technology the clinical possibilities of wearable biosensors monitoring.

A safe home is the first priority that people like to ensure before building a house. K. Vidyasagar et al [10] explain a mechanism to suppress unexpected, unwanted situations like fire or explosion due to gas leakage. Sensors like the gas sensor and the fire sensor are attached to a central control unit and together it builds a system to monitor the environment. Any abnormal sensor reading is reported and a Bluetooth-controlled Android application helps the user to toggle the loads quickly, especially in case of emergency.

Bilal Ghazal and Khaled Al-Khatib [11] researched on securing home from burglars and achieving automation by using one controller to monitor many devices. Mainly devised for the elderly and the differently abled, this device uses numerous sensors and detectors that constitute the main aim of this paper- safety and efficient interface for automation.

Shruthi Raghavan et al [12] paper describes the purpose of basic framework to advance and build on to achieve a connected home. Cloud based low cost home automation system implemented using the Digilent chipKIT Uno32 and Arduino Uno in which our home can controlled remotely and be monitored from anywhere in this world through internet. The remote monitoring demonstrates the capability of being able to know what is going on with different systems at home which can be used for control and safety and also it demonstrates using a few motors, how one can control different systems at home using the cloud service through the Internet.

Mamata Khatu et al [13] in their paper describe the use of cloud computing and storage over internet in order to keep track of all the objects. The values read by the sensor is converted to digital signals and given to the cloud workspace. Here, the data log analyzes the sensor information and produces a hardware response applying machine learning procedures. SHA 1 is the cryptographic algorithm for secure transmission to cloud over internet. Thus, supplying automation of household gadgets can be achieved by intertwining the use of Cloud and the IoT.



2.2    Critical  Review of Literature











Chapter 3




ACTUAL WORK





The Arduino Uno connects the transmitter device, the IR sensor and the vibrating device to the personal computer of the user. The Arduino board permits transfer of code from the PC through a USB cable especially fabricated to fit to the Uno board. The infrared (IR) sensor reads when a movement occurs within an effective range of 1m. The IR sensors, on identifying a movement in the surrounding, will emit a signal to the Arduino board. The board perceives the incoming data signal, does the necessary conversions and sends it to the transmitter.


FI G U R E 3.1: Arduino Uno



The transmitter sends out these data signals as electromagnetic waves that the receiver catches through the antenna. Electronic circuit of the radio transmitter is designed to transfer power from the high voltage main supply to a radio frequency alternating cur- rent, which radiates off an antenna as electromagnetic waves. Superimposing the audio and video waves over this current, simply allows easier transfer through radio waves. On contacting the radio receiver, a similar but less powerful wave is delivered. Different components of a general transmitter are – a power supply circuit, an oscillator, a


modulator and an amplifier. The oscillator generates vibrations and is often called the exciter for the same.  The amplifier or RF amplifier increases the power of the signal thus increasing the range of the radio waves.



FI G U R E 3.2: Transmitter



The receiver is connected to the Arduino Nano board on which the code for the receiver is uploaded. Hence, whenever the receiver spots a signal from the transmitter, Arduino causes the vibrator to generate vibrations in the system. Electronic filters is utilised by the receiver to extract the required data from a variety of signals that are captured by the antenna. Since the power of the signal received is low, the receiver uses an amplifier to enhance the signal which makes it easier to demodulate. Industries tend to take the term receiver to indicate radio receivers, which are generally the audio broadcasting radio receivers.



FI G U R E 3.3: Receiver


This vibrator is contained within a wrist band or a watch or even a small box which can be put under the pillow while the person is asleep.



FI G U R E 3.4: Vibrator



This is a wireless transmission that facilitates communication.  The entire system is designed to be wireless with the assistance of RF module. It, therefore, includes two components: the transmitter- a device that is connected to the door along with the door bell; and, the receiver - a device connected to the user’s body in any way or manner.

Pulse sensor detects heart beat or pulse of the person and works using the sense of touch, especially where the heart beat can be felt in the nerve. To observe the health of a patient, we need to keep an eye on various health aspects constantly. These aspects are recorded using a number of instruments, available in the hospital. One of the most significant aspects is the heart rate, and it determines a person’s fitness. The heart beat sensor is connected to two LEDs – a green LED that indicates the wellbeing of the person and glows only when the heart rate is normal, and a red LED that glows when the heart rate drops below the normal rate.  The normal heart rate of an adult 60-100 beats per minute (bpm).



FI G U R E 3.5: Pulse Sensor Model


3.1    Methodology  for the Study



3.2 	Experimental and/or Analytical Work Completed in the Project


3.3    Modeling, Analysis & Design



3.4    Prototype & testing


























Chapter 4




RESULTS,  DISCUSSIONS  AND CONCLUSIONS




Here, the results of the project work (literature survey and review along with actual work) shall be listed and discussed in detail with appropriate arguments (result analysis) leading to logical conclusions.  The list of conclusions should sync with the project objectives.  The scope for future research and development in the field of the current project work must also be included in this chapter.



4.1    Results & Analysis



4.2    Comparative Study



4.3    Discussions



Often we discussed about adding other features which may or may not be essential for our project.

Transmitters are devices which produce and communicate signals in the form of elec- tromagnetic waves, constructive in electronic industries. A transmitter generates an al- ternate current, called radio frequency alternating current, which, when passed through the antenna, the antenna sends out radio waves.


Transmitters are in use everywhere; all the latest electronic gadgets such as mobile phone, wireless networks and Bluetooth supported devices, radars, microwave ovens, navigational tools, and in ships, aircrafts, and spacecrafts as two way radio system. For industrial usage or for heating purposes, the machines used to generate radio waves op- erate on similar circuits as the transmitter, yet they are not known as the transmitter. The general idea behind the transmitter is communication and broadcasting, where the signal can be intercepted by many devices and only those devices which wish to corre- spond will do so. The transmitting devices are highly susceptible to interruption due to excessive amount of noise present in the surroundings. There is an unknown quantity of heat produced in the device during transmission, which might not be good for health.

When the transmitter is grouped with a receiver, the combination is named transceiver and in technical terms is abbreviated as ‘XMTR’ or ‘TX’. The message to be sent is in the form of digital electronic signal, and is superimposed on a carrier signal in order to add length to the distance it travels with minimum changes in the signal. This process is termed as modulation and it is the main feature of transmission in a transmitter. Mod- ulation is available in three basic types: Frequency modulation – where frequency is varied; Amplitude modulation – where the amplitude is varied; and Phase modulation – where angle or phase is varied to achieve communication. The modulated signal from the transmitter is directed to the antenna that broadcasts the radio waves in the environ- ment. Small antennae are encased in portable electronic devices like the mobile phones, while the larger antennae can be setup on roof tops or towers for transmission through transmission lines for larger devices similar to the FM radio transmitter, and TV signals transmitter.

The receiver, abbreviated as RX in technical documents and also known as radio re- ceiver or simply radio, obtains the signal sent by the transmitter through its antenna and converts the message received to the original form through the process of modulation.

The radio frequency transmitter and receiver modules when clubbed together into one circuit, is named the RF module, which stands for the Radio Frequency module because both the elements involved, work at the radio frequency which lies around 433-434
MHz . The modulation used here is Amplitude Shift Keying (ASK) and the estimated frequency range of RF module is between 30 kHz and 300 GHz.  Serial data is fed into the RF transmitter and is then wirelessly transmitted through its antenna. It is very important for both the transmitter and the receiver to be working at the same frequency for a successful communication.  Encoder and decoder are often attached to the RF


module for parallel data transmission input while the decoder receives the data and translates it.

RF module transmission is advantageous over IR (infrared radiations) due to several reasons. Transmission through RF is suitable for long distance communication as it can traverse large distances. RF signals can communicate even with a hindrance between the transmitter and the receiver devices, while the IR functions in the LOS (line-of- sight) mode. Signal communication in RF is reliable and stronger than so in IR. Both the transmitter and the receiver section in the RF run at a matching frequency, thus making it less prone to noise and interference from other signals. On the other hand, IR intercepts unwanted signals and hence the interaction is disturbed.

IR (Infrared) sensors work on the basic principle of infrared radiation or electromagnetic radiation which has radiant energy that allows it to act as a wave or as a photon. Infrared emission can be permeable in fragments of all materials and then detected when it is reflected back.  This theory helps the sensor to measure the distance of the object or obstruction sensed. Parts of the IR sensor are the emitter which emits the infrared light as short pulses; and the detector which perceives the object in front using the concept of reflection.

The company Arduino specialises in software and hardware manufacturing mainly known for its microcontroller, Arduino.  Arduino microcontroller permits digital projects to produce interactive, user friendly projects or tools, which are further used in various in- dustries based on the utility of each such venture. The software programs can be coded in languages such as C, C++, Python, etc. The distinctive trait of this board is the us- age of the Universal Serial Bus (USB), allowing the transfer of programs from user’s personal device or computer.

Pulse sensor is used in our project to measure a live heart rate of a person in real time. It is an plug and play heart rate sensor for Arduino. It can be used by students, artists, athletes who want to easily incorporate live heart rate data. The sensor clips onto a fingertip or earlobe and plugs right into Arduino. A pulse sensor is a personal monitoring device which allows one to measure his or her heart rate in real time. Widely used in hospitals for checking the health of patients.


The Android application we use in our project to connect our project to the IoT envi- ronment, is called Cayenne. It has numerous user-friendly features that make the users feel an ease as if they are using a remote control to operate on various appliances at home just as they use a remote to manoeuvre TV. Its data storage, drag and drop widget features and different sensor data requirements displayed, like the room temperature, etc. have enhanced the use of the hardware. This creates better utilization of the data available and the data that the user wishes to access. If connected to the Arduino or the Raspberry Pi platforms, project prototypes can be experimented with, straight from the Android phone -which a majority of people possess and which has now become very


common. This application has an IoT project builder which helps in building and start- ing a project effortlessly and quickly.  An online Dashboard is available that reduces much difficulties faced during the making of the project.  Cayenne Cloud facilitates contact with the server and hardware for the taking a hold of the several actions, alerts and triggers that occur due to numerous input commands given by the user. It is also responsible for the storage of user, sensor and device data and for dealing with the user actions.

Raspberry pi we use in our project is a credit card sized computer launched by the Raspberry Pi foundation. It can be pluged into your tv and a keyboard, and can be used for many of the things that your regular desktop does – spreadsheet, word processing , games and it also plays high definition video. The Raspberry Pi 3 Model B features a quad-core 64-bit ARM Cortex A53 clocked at 1.2 GHz. This puts the Pi 3 roughly 50% faster than the Pi 2. Compared to the Pi 2, the RAM remains the same – 1GB of LPDDR2-900 SDRAM, and the graphics capabilities, provided by the VideoCore IV GPU, are the same as they ever were. As the leaked FCC docs will tell you, the Pi 3 now includes on-board 802.11n WiFi and Bluetooth 4.0. WiFi, wireless keyboards, and wireless mice now work out of the box. A newer version of Raspberry Pi, Raspberry Pi 3 Model B has been released recently. What makes it different from other previous models are :
•	A faster 64 bit processor running at 1.2 GHz
•	On-board Bluetooth Low Energy (BLE)
•	Built in WiFi

The T-Cobbler Plus is an add on prototyping board from Adafruit specifically designed for the B+ and Pi 2 that can break out all those tasty power, GPIO, I2C and SPI pins from the 40-pin header onto a solderless breadboard. This set will make "cobbling together" prototypes with the Pi super easy. It only works with the Raspberry Pi Model A+/B+/Pi 2. This Cobbler is in a fancy T-shape, which is not as compact, but is a little easier to read the labels. Each order comes with a 40 way ribbon cable and assembled T-Cobbler Plus. You can plug the 40-pin GPIO cable between the Pi computer and the T-Cobbler breakout. The T-Cobbler can plug into any solderless breadboard (or even a prototyping board like the PermaProto). The T-Cobbler PCB has all the pins labeled nicely so you can go forth and build circuits without keeping a pin-out printout at your desk. We think this will make it more fun to expand the Pi and build custom circuitry with it.

Breadboards is used in our project, they are one of the most important part when learning how to build circuits. A breadboard is a solderless device for temporary prototype with electronics and test circuit designs. Most electronic components in electronic circuits can be interconnected by inserting their leads or terminals into the holes and then making connections through wires where appropriate. The breadboard has strips of metal underneath the board and connect the holes on the top of the board. We should note that the top and bottom rows of holes are connected horizontally and split in the middle while the remaining holes are connected vertically. A variety of electronic systems may be prototyped by using breadboards, from small analog and digital circuits to complete central processing units (CPUs).


4.4    Conclusions



Our System is definitely a resource which can make home environment automated. Electrical devices can be controlled by the people via the home automation devices and can set up the monitoring actions in the computer. Hence we think this product have high potential for marketing in the future.

The proposed home automation system is dedicated for elderly, people with disabilities, handicapped persons and others. It consists of remote control supported by command buttons and provided by alert LEDs and a LCD for showing messages. The braedboard toggles the ON/OFF switches of the appliances by means of relays. The remote control and its base are communicating with RF signals.

The projected approach can be implemented at any location to automate the devices. The house or office is safeguarded from the electricity situations. This device will keep the entire house or office in monitoring state.  The device is connected with database so that the person can track who is visited to his/her home.  The device will measure a person live heart rate so that he/she can know whether he/she is in normal rate or critically low. Our System is definitely a resource which can make home environment automated. Electrical devices can be controlled by the people via the home automation devices and can set up the monitoring actions in the computer.  Hence we think this product have high potential for marketing in the future.


4.5    Scope for Future Work


1. To capture the image of the visitor over a high quality camera is essential.

2. A speaker could also be embedded in the device for speech recognition.

3. A module for dumb people can be implemented where they can communicate that they heard the door bell and may or may not be coming


Bibliography



[1] R. I. Damper, M. D. Evans - “A Multifunction Domestic Alert System for the Deaf-Blind”- IEEE Transactions on Rehabilitation Engineering, Vol. 3, No. 4, pp. 354-359, December 1995. 

[2] B Murali Krishna,J Sri Varshini A Narayana Murthy- "RF Module Based Wireless Secured Home Automation System Using FPGA"- Journal of Theoretical and Applied Information Technology Vol. 77, No. 2, pp. 273-279 , 20th July 2015.

[3] Smitha.M, T. Ayesha Rumana, Sutha.P,-"Hand Gesture Based Home Automation Visually Challenged”-International Journal Of Innovations in Engineering Research and Technology [IJIERT] Vol. 2, No. 4, April 2015.

[4] Girija Sankar Dash, Swetalima Rout, Omprakash Singh-“WiBeD2: A Communication Aid for Deaf and Dumb”- International Conference On Information Communication And Embedded System,  pp. 1-4, 25-26 February 2016.

[5] Pushpanjali Kumari, Pratibha Goel, Dr. S. R. N. Reddy –“PiCam: IoT based Wireless Alert System for Deaf and Hard of Hearing” International Conference on Advanced Computing and Communications, pp. 39-44, 18-20 September 2015.

[6] Steve Warren, Jianchu Yao,, G. Edward Barnes – Wearable Sensors and Component Based Design for Home Health Care – IEEE, Vol. 3, pp. 1871-1872, October 2002.

[7] Alexandros Pantelopoulos and Nikolaos G. Bourbakis – A Survey on Wearable Sensor Based Systems for Health Monitoring and Prognosis-IEEE Transactions on Systems- Vol. 40, No. 1, pp.1-12, January 2010.

[8] Adrian Burns, Barry R. Greene, Michael J. McGrath* - SHIMMER -  A Wireless Sensor Platform for Noninvasive Biomedical Research- IEEE Sensors Journal, Vol. 10, No. 9, pp. 1527-1534, September 2010.

[9]  H. Harry Asada, Phillip Shaltis, Andrew Reisner, Sokwoo Rhee, And Reginald C. Hutchinson-“Mobile Monitoring with Wearable Photoplethysmographic Biosensors”- IEEE Engineering in Medicine and Biology Magazine, Vol. 22, No. 3, pp. 28-40, May/June 2003.

[10] K. Vidyasagar, G. Balaji, K. Narendra Reddy- “Android Phone Enabled Home Automation”- Journal of Academia and Industrial Research (JAIR), Vol. 4, No. 2,  pp. 65-68, July 2015. 

[11] Bilal Ghazal, Khalid Al-Khatib-“Smart Home Automation System for Elderly, and Handicapped People using Xbee” - International Journal of Smart Home, Vol. 9, No. 4, pp. 203-210 (2015).

[12] Shruthi Raghavan and Girma S. Tewolde –“Cloud based low-cost Home Monitoring and Automation System”- ASEE North Central Section Conference,  pp. 1-10, 2015.

[13] Mamata Khatu, Neethu Kaimal, Pratik Jadhav, Syedali Adnan Rizvi-“Implementation of Internet of Things for Home Automation”- International Journal of Emerging Engineering Research and Technology  Vol. 3, No. 2, pp. 7-11, February 2015.  




PUBLICATION DETAILS

S.K. Kenue and J.F. Greenleaf, “Limited angle multifrequency diffiaction tomography,”
IEEE Trans. Sonics Ultrason., vol. SU-29, no. 6, pp. 213-2 17, July 1982.











Appendix  A




Appendix  A Title





Since the chapters are numerically numbered, the appendices shall be numbered using alphabets (English capital letters). The items that can be inserted as appendices are (list is not exhaustive):


• Project synopsis or proposal (if submitted before starting the project)

• Photos

• Software model analysis reports (these shall not be inserted in the main body of the report)

• Project schedules

• Selected material from the data collected

• Miscellaneous analysis and reports




A.1    Appendix  A Section 1



A.1.1    Appendix A Subsection for Section 1



A.2    Appendix  A Section 2











Appendix  B




Appendix  B Title






B.1    Appendix  B Section 1



B.2    Appendix  B Section 2



B.3    Appendix  B Section 3











Index




Methodology, 10                                               Ojectives, 11
