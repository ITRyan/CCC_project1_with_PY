# First How video games works on a general level
* The best way to think about that is to start with movies, because that is the technology video games leaked,a movie is really just a ton of images playing really fast after each other,we usually called it frames a movie has 24 frames per second so your
eye perceives this as a moving .

* image there's 3 ways to approach this ,record it with a camera ,Draw images yoursrlf,Use digital tools/use a computer to create a 3D image but the end of the daty all we're doing is creating lots of indivdual images and playing them really fast after each other.
So Videogames just show you lots of images and your brain interprets that as afluid motion

* On a video game each individual image isn't set in stone ,instead it's dynamic meaning that each individual image is created on the fly and plays dynamically depending on what the game needs, so exsample:
* is the enemy in a certain position or did the player press a certain kind  of button to movie in a certain direction , and then each individual frame is being updated automatically.

We always start by checking the player input (the event loop),so each kind of event could be a different kind of thing a player does, or something eles for example a timer running out, so we are placing all the enemies we are drawing the health indicator the coin indicator whatever we really need and well once we have all of that we have one finished frame so this is one image the player is going to see once this process is finished we are getting  rid of the entire image again and starting this process from scratch and we are doing this multiple times per second usually about 30 to 60 times depending on how fast the computer is
so that is really it. 

