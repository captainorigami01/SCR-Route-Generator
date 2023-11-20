# SCR Route Generator
![](https://img.shields.io/badge/SCR_Route_Generator-V0.11-green) ![](https://img.shields.io/badge/SCR_version-1.10.12-blue)

> [Download V0.11](https://github.com/captainorigami01/SCR-Route-Generator/releases/tag/v0.11)
>
> Please check our [requirements](#requirements)

## What is our software?

Our software is designed to be used to generate routes for both passengers and drivers.
In passenger mode you are given 2 locations; a start and end location. The catch is that you have to get from the 2 stations as qucikly as possible. We have a timer function in our software. You should start the timer when you get on a train at the start location and should stop it when you disembark the last train at your destination.

If you record a video and provide an unedited video to us via a link by reporting an [issue](https://github.com/captainorigami01/SCR-Route-Generator/issues) with the tag competiton. We can review it and descide wheter it is podium worthy.

You can also generate a working time table which will use the trains and routes you own. You have to tell the software which routes and trains you own in advance.
To edit this remove the routes, trains and operators you don't own from the `ownedRoutesTrains.json` file. It generates between 4 - 15 services per timetable. If you are unhappy with your timetable you can generate a new one.

## What are the trains and routes currently supported?

All trains and routes in SCR 1.10.12 are included. what do the train codes mean:
A train class ending with and `A` means Airlink. `D` indicates it is a double unit. `I` indicates the consist has 1 extra coach.
HST's (class 43's) have there own codes. `43` on its own is the 4 car HST. `43/5` means 5 car HST and `43 Buffer` indicates the HST with buffers.

Routes are generated by the python script and then generates an HTML5 webpage. If you want to customise the look and feel of the page then you can edit the `style.css` provided.

# Requirements
You will require [python 3](https://www.python.org/downloads/) to run our program. Please select the correct version for your system and use the installer.

Our software has been designed using Windowss 11 but should work on all windows operating systems. We cannot gaurantee that the software will run correctly on other operating systems. If it does not please alert this to us as a bug in the [issues](https://github.com/captainorigami01/SCR-Route-Generator/issues) and we will try to fix it if possible.

# Our project to do list
Our project has a to do list, each version will be given its own view. [View the to do list](https://github.com/users/captainorigami01/projects/4/views/1)

# Terms / license
The 'software` is protected by the [GNU GENERAL PUBLIC LICENSE v3](https://github.com/captainorigami01/SCR-Route-Generator/blob/main/LICENSE)