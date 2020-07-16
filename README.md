# mask-off
Project for 2020 Intern Hackathon

## Stack
```
Backend:
Python
twilio API

ML:
opencv
tensorflow
numpy

...
```

## License

This application is licensed under the Apache License, Version 2. Separate third-party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache License FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)


## Background

With COVID-19 infection rates on a steady decline in much of the world, the return to the in-person office environment is starting to become more and more realistic. However, returning to the office would be predicated on the ability to ensure a safe work environment for all members of a company. In many offices, maintaining physical distancing may not always be possible. Elevators, narrow hallways, and washrooms can make it hard to maintain a 2m distance from others. In scenarios where physical distancing is not possible, the wearing of masks is crucial to preventing the spread of the virus. In fact, many jurisdictions require that masks be worn when indoors as well. Given this, it is safe to assume that mask wearing will be a part of daily life in the return to in-person offices. 

## The Problem

Wearing a mask in the office is not something that we are used to, and it will likely be difficult to remember to consistently do. Regardless of the rules an office implements, if employees forget to wear their masks, the workplace will not be safe. 

## Our Solution

Mask-On is an AI system to help remind you to wear a mask in your office setting. Mask-On runs in the background of your computer and looks through your webcam, sending you SMS notification for when you forgot to put your mask on. 

Mask-On has two modes so that it works with either of the following two most common masking rules in in-person offices; that you must wear masks when moving throughout the office, but may take it off at your desk, or that you must wear masks at all times, including at your desk. 

If you must wear a mask around the office, but not at your desk, Mask-On will look through your webcam and when you have left your desk, Mask-On will send a text message reminding you to bring your mask with you. This way if you go to get a coffee or run to the bathroom, you won’t forget your mask!

If your office operates with the rule that you must always wear a mask, Mask-On will look through your webcam and if it sees that you haven’t been wearing a mask for an extended period of time, it will send a text to your phone reminding you to put one on.

Mask-On was designed with privacy in mind. It runs locally on your computer, capturing individual frames of your webcam feed live, processing them, and then immediately discarding them afterward. Your video is never stored and your video is never sent over the internet. Information on your mask wearing history is not collected, stored, nor reported anywhere. This tool is not for office places to police their employees, but for employees to help build safe mask wearing habits.  



## Technological Implementation 

Mask-On uses OpenCV’s Cascade Classifier to detect a face in the video. If Mask-On is watching for when you leave your desk it will then use a KCF (Kernelized Correlation Filter) to track your face and head and see if it leaves the frame. If Mask-On is checking if you are wearing a mask, it will use that detected face and run it through another CNN classifier that we trained on images of faces with and without masks. We also use tensorflow for model training and mask on a face detection. We use Twilio and the API's it provides to send SMS messages to users. This is all done in a Python backend. Lastly, we deployed a django app on IBM cloud as a dashboard which will provide employers with key statistics on their employees mask usages so that they can enforce mask usage if needed.

## Next Steps

Our next steps would to be to create a more comprehensive user interface and to train our mask detection classifier on more data, and for longer. We were not able to do that during this development phase because of time constraints.
