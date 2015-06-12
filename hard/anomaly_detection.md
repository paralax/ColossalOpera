# Title

Mission Impossible: Fooling the Anomaly Detector and Exfiltrating Data

# Difficulty

Hard

# Description

In data mining, anomaly detection (or outlier detection) is the identification of items, events or observations which do not conform to an expected pattern or other items in a dataset. In particular in the context of abuse and network intrusion detection, the interesting objects are often not rare objects, but unexpected bursts in activity. Usually these models are built on averages and look for outliers 3 standard deviations away; models are continually updated to account for the natural evolution of behaviors. 

For example, you may have an e-commerce business that has day-of-week and hour-of-day models of transactions. If there's a significant drop or burst of activity, you know something's afoot. Similarly, if you walk outside and see a tremendous burst of traffic on the roads - perhaps a traffic jam at that point - when it's normally flowing smoothly with intermittent cars, then you know something is odd. 

In this challenge, we're trying to throw off such an anomaly detector and cover our activity. We have a simplistic anomaly detector we're trying to bypass as we move sensitive corporate documents - the latest summer blockbuster about to be released - into the wild. Some points about the network we're attacking:

* The *x* axis is your timeline
* Values above the *y* axis are bytes leaving the network, below the *y* axis are bytes entering the network
* The anomaly detection system is very simple and based only on the history seen so far
* It's just starting out, and has no robust history
* Alarm thresholds are measured in units of standard deviations
* Calculate the volume of traffic sent by taking the area under the curve defined by the time series 

Your mission, should you choose to accept it, is to maximize the rate of data exfiltration without triggering the anomaly detector. You can do this by sending and receiving data over the network to confuse the detector into thinking the traffic rates it sees are normal. 

# Input Description

You'll be given the anomaly detector informatio on the first line. The numers *S*, *T0* and *T1* telling you how many standard devitations the alarm is set for, and the first two data points as (+y, -y) coordinates. Example:

    3 (100,-100) (200,-200)

The next line will tell you how many bytes you have to target to exfiltrate. Example:

    700000000

In this case that's about 700MB. 

# Output Description

Your program should emit the time series of data you need to send and receive to keep your exfiltration mission a quiet secret (e.g. you didn't trip the anomaly detector). 

# Challenge Input

    3 (100,-50) (125,-65)
    4000000000
