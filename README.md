| Deliverable | Due Date              |
|---------------|----------------------------------------------------------------------------|
| Race Day | Saturday, May 13th (TIME TBD) EST |
| Code Pushed to Github  | Saturday, May 13th 1PM EST |
| Briefing (15 min presentation + 5 min Q&A) OR Report ([github pages](https://github.mit.edu/rss/website2021)) | Wednesday, May 10th at 1:00PM EST (presentation time TBA) |
| [Team Member Assessment](https://forms.gle/5npgrmk8mjdRGGcL7)  | Wednesday, May 10th at 11:59PM EST |

# Final Challenge 2023


## Introduction

Congratulations on completing the six labs of RSS! 

This semester, you've learned how to implement real-time robotics software on a widely-used software framework (ROS). You know how to read sensor data (LIDAR, Camera, Odometry) and convert it into a useful representation of the world (homography, localization). You've written algorithms which make plans over the world's state (parking, line following, path planning) and couple with controllers (PD control, pure pursuit) to accomplish tasks. 

Now, your team will synthesize all that you've learned to design a competitive entry for the *2023 RSS Final Challenge*! 

## Introduction
In a world far, far away...

Your beloved racecar that you've spent three months bonding with has been kidnapped by the evil RACECAR Em-tire and transported to a new world! It seems very similar to our own, though there seem to be a couple of differences:
- The cities seem to be built on a smaller scale
- Beyond the city, there are colorful roads
- The only moving agents seem to be autonomous racecars!
You've heard that there's a portal back to Earth at the end of the Rainbow Road outside of the city, but the Em-tire has demanded that your car participate in a race for the entertainment of the populace before it is to be allowed to leave the city gates. Moreover, once your racecar leaves the racetrack arena, it must drive safely through the city to get to the Rainbow Road or else the Em-tire will get angry and keep your car hostage (apparently, they're particular about the stop signs!).

Luckily, you're armed with your knowledge from RSS and a good SSH connection! Let's get your racecar back home to MIT!

## Grading

| Deliverable  Grade | Weighting             |
|---------------|----------------------------------------------------------------------------|
| Part A: Final Race (out of 100)  | 35% |
| Part B: City Driving  | 25% |
| Part C: Rainbow Road [BONUS]  | 10% |
| Briefing OR Report Grade (out of 10) | 40% |

### Part A: Final Race
Part A is worth 35% of your Final Challenge technical grade. Your grade will be calculated based on the time your car takes to drive around the track (`best_race_split`, in seconds) as follows:

  `Part A grade = min(100 + (50 - best_race_split), 110)  - penalties`

Where `penalties` is calculated as follows:

  `penalties = 15 * num_collisions + 5 * num_lane_line_breaches + 5 * num_long_breaches`
  
And `num_lane_line_breaches` is the number of times the car drives outside of either lane line, and `num_long_breaches` is the number of times the car has driven outside of its lane and stayed outside of the lane for greater than 3 seconds.

As you can see from this grading scheme, it is possible to receive bonus points for a very fast and precise solution. The **maximum speed of your car should be capped at 4 m/s**; you should be able to get full points (with bonus!) with a good controller. You should, above all, prioritize avoiding collisions, and if your car leaves its lane, it should quickly recover. More information about race day can be found below in this handout.

### Part B: City Driving

Coming soon! :-)

### Part C: Rainbow Road [EXTRA CREDIT]

Coming Soon! :-)

**Your team will choose between completing a final briefing or report (you do not need to complete both).**

### Briefing Evaluation (see [technical briefing rubric](https://docs.google.com/document/d/1NmqQP7n1omI9bIshF1Y-MP70gfDkgEeoMjpWv8hjfsY/edit?usp=sharing) for grading details)
When grading the Technical approach and Experimental evaluation portions of your briefing, we will be looking specifically for **illustrative videos of your car following the track lane and Rainbow Road as well as executing city driving maneuvers.** Specifically, we would like videos highlighting:
- Visualization of lane / marker tracking and stable drive control within a lane
- Stopping at stop signs and making turns through the course
- Recovery of your car if it is outside of its assigned track lane
- Segmentation using machine learning of the Rainbow Road

### Report Evaluation (see [technical report rubric](https://docs.google.com/document/d/1B6l7vKJFN3CPPcMn8cKKArHUU_Bq_YUZ5KxKoP6qMk0/edit?usp=sharing) for grading details)
When grading the Technical approach and Experimental evaluation portions of your report, we will be looking specifically for the following items:

- **Numerical evidence that your algorithms work in the form of charts/data**
  - Numerical evaluation of the success of your lane tracking + following
    - Make sure to mention your method for finding the lane and tuning the controller to closely track it.
  - Numerical evidence evaluating the success of your city driving algorithm
    - Make sure to mention your method for recognizing stop signs and driving through the buildings as well.
  - Numerical evidence evaluating the success of your Rainbow Road segmentation algorithm
    - Make sure to mention your method for training your model and tuning the controller to closely follow the road.

## Part A: Final Race

### Environment and Task

The Final Race will take place on the entire Johnson track loop. This is a standard-size 200m track. Cars may be assigned to follow any of the track's six lanes and will be informed of their lane assignment the morning of the race. Lanes are numbered from left to right as shown in the image below.


<!-- <img src="media/final_race.PNG" width="300" /> -->
<img src="media/start_area.jpg" width="400" />

Your car's task is to complete the 200-meter loop around the track as fast as possible, while staying in your assigned lane. Any kind of collision (with another car or with something in Johnson) will be penalized heavily. You should have some kind of safety controller running on your car, but be careful that this doesn't stop your car if there is another car driving next to it on the track! 

### Race Day
On race day, multiple teams will set up on the track at the same time. A TA will give the start signal, at which point the race begins! You must have a member of your team closely follow your car along the track with the controller ready to take manual control at any moment (yes, a great opportunity to exercise). Your car's split will be recorded at the finish line, and TAs will also be stationed at various points along the track recording lane breaches, if they occur (but hopefully no collisions). Each team will have the opportunity to race **three** times, and we will take the best score.

### Tips

Here are some things you may consider in developing your approach:

- How can you reliably segment the lane lines?
- How can you obtain information about the lane lines in the world frame?
- How can you detect if the car has drifted into a neighboring lane?

Please note that Hough Transforms will very likely be useful; helpful resources are [here](https://towardsdatascience.com/lines-detection-with-hough-transform-84020b3b1549) and here(https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html).

## Part B: City Driving

Coming very soon! :-)

## Part C: Rainbow Road [EXTRA CREDIT]

Coming soon! Stay tuned!

### Race Day!


## General Notes

### Structuring your code

The final challenge is the most open-ended assignment in RSS, and comes with minimal starter code. We suggest referring to previous labs for good practices in structuring your solution:
- Start by defining what nodes you will create, what they will subscribe to, and what they will publish. From this plan, write skeleton files, then split up the work of populating them with working code.
- Make useful launchfiles and set launch-time variables via rosparams. Refer to previous labs for syntax.

### Leveraging previous labs

You are encouraged to build your solution on code written in previous labs! If you are using your old homography solution, it's good idea to verify its accuracy. 

### Increasing the speed limit
In previous labs, the racecar was throttled to a default maximum speed of 2 m/s. You can change the max racecar speed by editing the `speed_min`/`speed_max` in this file: https://github.com/mit-racecar/racecar/blob/master/racecar/config/racecar-v2/vesc.yaml. This file can be found on the racecar, in the config folder. The github link is just an example of what it should look like. 

These speeds are measured in ERPM. The conversion factor is 4614 ERPM per m/s (this is a parameter at the top of the file). The hardware limit is ~20000 ERPM. *This should be the maximum value you set in `vesc.yaml`*.

Note that this does not change the max speed of the joystick. If you want the joystick to command a higher speed change the scale parameter for drive.speed in this file: https://github.com/mit-racecar/racecar/blob/master/racecar/config/racecar-v2/joy_teleop.yaml. The scale parameter multiples the joystick output which is in the range [−1,1] to produce a speed. Similar to the one above, the config file can be found on the racecar in the root directory, but the Github link is there so you have a reference as to what it looks like!

## FAQ

### Part A: Final Race

*Do we need to design a safety controller for this challenge?* 
* You should run some kind of safety controller during the challenge, but don't need to spend a lot of time adapting it to the race setting. The easiest way to keep the race collision-free will be for each team to design a robust lane-following solution and remain in-lane. Note: some teams showed solutions in Lab 3 that considered a fixed angle range in front of a car only when deciding when to stop the car. **You should make sure that cars racing alongside yours will not wrongly trigger your safety controller, especially when turning bends in the track!** Consider testing with objects in adjacent lanes.

*Will we be penalized if another car comes into our lane and we crash?*
* No. If you stay in your lane, you will not be considered at fault for any collision. We will give every team the opportunity to record three interference-free lap times on race day.

*Doesn't the car in the outside lane have to travel farther?*
* We will stagger the starting locations so every car travels the same distance. You should be prepared to race in any lane.

### Part B: City Driving Challenge

Will be updated soon!

### Part C: Rainbow Road Challenge

Updates coming soon!

