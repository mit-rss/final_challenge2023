| Deliverable | Due Date              |
|---------------|----------------------------------------------------------------------------|
| Race Day | Saturday, May 13th 11AM - 2PM
EST |
| Code Pushed to Github  | Saturday, May 13th 1PM EST |
| Briefing (15 min presentation + 5 min Q&A) OR Report ([github pages](https://github.mit.edu/rss/website2021)) | Monday, May 15th at 1:00PM EST (NB: deadline is for briefing slides, briefings are from 3-5pm) |
| [Team Member Assessment](https://forms.gle/5npgrmk8mjdRGGcL7)  | Monday, May 15th at 11:59PM EST |

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

Part B is worth 25% of your Final Challenge technical grade. You get 3 attempts and your grade is based on your best attempt out of 3. Your grade will be calculated based on timed completion through the course (best_city_time, in seconds) and the number of penalties you incur as follows. Your grade depends on what portal you exit through and what bonuses you attempt to tackle:

Portal 1: `Part B grade = min(100 + (21.5 - best_city_time), 110) - penalties`

Portal 2: `Part B grade = min(100 + (18.5 - best_city_time), 110) - penalties`

Portal 3: `Part B grade = min(100 + (13 - best_city_time), 110) - penalties`

Indicator Variable: `R = 1` if you stay on the road, `R = 0` if you go off the road

HARD bonus ending at Portal 2: 

`Part B grade = min(100 + (18 + 9*R - best_city_time) + 2.5 + R*2.5, 115) - penalties`

HARD bonus ending at Portal 3: 

`Part B grade = min(100 + (24.5 + 9*R - best_city_time) + 2.5 + R*2.5, 115) - penalties`


HARDER bonus ending at Portal 2:

`Part B grade = min(100 + (25 + 9*R - best_city_time) + 5 + R*5, 120) - penalties`

HARDER bonus ending at Portal 3: 

`Part B grade = min(100 + (25 + 9*R - best_city_time) + 5 + R*5, 120) - penalties`

Formula for Penalities: 

`penalties = 5 * num_collisions + 10 * traffic_infractions + 10 * manual_assist`

And num_collisions is the number of times the car collides with anything in the city (ie. buildings, bricks, road signs), traffic_infractions is the number of times the car passes a stop sign without coming to a full stop or stops at a non-stop sign, and manual_assist is the number of maneuvers (counted individually for turning a corner, stopping at a stop sign, resetting a car, etc.) that required manual teleop intervention.

As with Part A, it is possible to receive bonus points for a fast implementation, yet it is important to prioritize the accuracy of the maneuvers. The maximum speed of your car should be 1 m/s. However, operating at maximum speed for your entire run will be very challenging for this task. You should start slow and conduct tests to select an appropriate target speed for your car. To receive full credit over this course, you will need to cover an average of around .4 m/s (but this value will be calibrated by our staff solution completion speed). Additionally, the formula for calculating score and penalty values may change for fairness. (Less penalty for timing issues, depending on how things go).

### Part C: Rainbow Road [EXTRA CREDIT]
Part C can add an additional 10% to your Final Challenge technical grade! Your grade will be calculated based on the number of penalties you incur as follows:

Part C grade = min(100 + 2 * staff_multiplier * (5 - best_race_split), 110) - penalties

Where staff_multiplier is a calibrating constant based off of the staff solution (TBA) and penalties is calculated as follows:

penalties = 5 * num_lane_line_breaches + 5 * num_long_breaches

And num_lane_line_breaches is the number of times the car drives outside of the Rainbow Road, and num_long_breaches is the number of times the car has driven outside of the road and stayed outside of the lane for greater than 3 seconds.

The maximum speed of your car should be 1.5 m/s.

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

### Environment and Task

The City Driving challenge will take place in the "MiniCity" course set up in the center of the Johnson track.

The exact configuration (where stop signs are) of the final MiniCity is kept a secret until Race Day (the Em-tire is keeping your racecar locked inside the arena until you race!), though you were able to recreate a practice course using an occupancy map you snuck out (rss_final_challenge_map.png). 

Your job, after finishing your race successfully, is to drive from the start of the course to one of the portals that will transport you to the Rainbow Road (part C). You will have access to the map mentioned above, and your race car can either use that or road lines to navigate the course. Your car can also get a bonus boost, before it fully escapes. You have also been warned that stop signs must be observed and the car must come to a full stop or else the Em-tire will get angry! 

The Em-tire, in their infinite wisdom and with their love of buzz words, has already created a ~ machine learning ~ based stop sign detector for you (located in /city_driving)! It not only tells you if there's a stop sign, but where in your image the stop sign is (nifty!). If you don't use it, the Em-tire will be mad that their hard work went to waste, but you are free to modify the code for the detector and add higher level logic to take advantage of it.

Here are the details of the challenge:

* You can leave through one of three portals (labeled on the map):
  * For portal 1: you must stay within the road and must park in the designated area (in blue)
    * The road will have a centerline
    * This portal will have walls on the outside 
  * For portals 2 and 3: you are allowed to go off road and must park in the designed area (in blue)

You can also get bonus points in the following ways:
* HARD: Swing by the bonus boost area (part of your car must go inside the yellow box) before parking at portals 2 or 3
  * If you do this task while staying on the road on your way to the bonus boost area you get even more bonus points (but this is not a requirement)
* HARDER: Park at portal 1 (for maximum bonus boost!) and then park at portal 2 or 3
  * If you do this task while staying on the road on your way to portal 1 you get even more bonus points (but this is not a requirement)

Things to note: 
* Each square on the map is 1 ft x 1 ft
* On the github you have access to an occupancy grid file you can use for localization
* You will also encounter stop signs at random places throughout the course, where your robot must come to a FULL STOP
* Your start position will be slightly randomized within the start area (robot placed at slight angle and translation)
* You can choose the portal you park at

<img src="https://github.com/mit-rss/final_challenge2023/blob/main/city_driving/rss_map_visual.png" width="400"/>

### Tips

The City Driving Challenge is meant to be open-ended. You should make use of whatever techniques you believe will best solve the problem.

Here are some things you may consider in developing your approach:

- How do you implement the high-level logic that puts together localization, path-planning, stop sign detection, and collision avoidance?
  - Perhaps a state machine would be helpful--how would you connect the different tasks?
- How should the speed of your car be adjusted as you detect a stop sign, decide it is close enough, and turn corners?
- The stop sign detector is good, but not perfect. How might you account for this for robust city navigation?

As always, your safety controller should be turned on for this portion of the Final Challenge as well, although the city will not damage the car should you collide with anything.


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
In previous labs, the racecar was throttled to a default maximum speed of 2 m/s. You can change the max racecar speed by editing the `speed_min`/`speed_max` in this file: https://github.com/mit-racecar/racecar/blob/master/racecar/config/racecar-v2/vesc.yaml. This file can be found on the racecar, in the config folder. The full path on the racecar is /home/racecar/racecar_ws/src/base/racecar/racecar/config/racecar_v2/vesc.yaml. 

These speeds are measured in ERPM. The conversion factor is 4614 ERPM per m/s (this is a parameter at the top of the file). The hardware limit is ~20000 ERPM. *This should be the maximum value you set in `vesc.yaml`*.

Note that this does not change the max speed of the joystick. If you want the joystick to command a higher speed change the scale parameter for drive.speed in this file: https://github.com/mit-racecar/racecar/blob/master/racecar/config/racecar-v2/joy_teleop.yaml. The scale parameter multiples the joystick output which is in the range [−1,1] to produce a speed. Similar to above, within the 'config' folder in the base package, you can find joy_teleop.yaml. The full path is: /home/racecar/racecar_ws/src/base/racecar/racecar/config/racecar_v2/vesc.yaml


## FAQ

### Part A: Final Race

*Do we need to design a safety controller for this challenge?* 
* You should run some kind of safety controller during the challenge, but don't need to spend a lot of time adapting it to the race setting. The easiest way to keep the race collision-free will be for each team to design a robust lane-following solution and remain in-lane. Note: some teams showed solutions in Lab 3 that considered a fixed angle range in front of a car only when deciding when to stop the car. **You should make sure that cars racing alongside yours will not wrongly trigger your safety controller, especially when turning bends in the track!** Consider testing with objects in adjacent lanes.

*Will we be penalized if another car comes into our lane and we crash?*
* No. If you stay in your lane, you will not be considered at fault for any collision. We will give every team the opportunity to record three interference-free lap times on race day.

*Doesn't the car in the outside lane have to travel farther?*
* We will stagger the starting locations so every car travels the same distance. You should be prepared to race in any lane.

### Part B: City Driving Challenge

*How many stop signs will there be on race day?* 
* Two

*How far should the car stop before the stop sign?*
* The front of your car must stop between .75-1 meters in front of the stop sign to receive credit for the stop. On race day, there will be tape on the ground so we can check if your car has stopped at the correct distance. Stop signs will all be the same size as the ones at lab. They will always be perpendicular to the road and not visible from other sections of the city. 

*How long does the car need to stop for?*
* There is no time requirement, but your car must come to a **full stop** (no California stops!).

*Will there be anything else in the city besides buildings, red bricks, and stop signs?*
* Yes! There will be distractor signs, etc... Your car should ignore all of these extra items!

*Will we have a map of the city?*
* Yes, the map will be released soon, and the staff team is currently working on a way to test out your algorithm in simulation rather than having to wait for the city to be set up!


### Part C: Rainbow Road Challenge

Updates coming soon!

