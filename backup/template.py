import os
import webbrowser
import codecs
import subprocess



f = open('testingbase.html', 'w')

template = """

<html>
<head>
    <title>Animation</title>
</head>
</body>
<div style="background-color:#BFC0C2; width:1920px; height:1080px;"> 
    <!-- scores, fayble, and influencers -->
    <div style="float: left; width:1280px;">
        <div style="background-color:#62affc;  width:1280px; height:360px; text-align:center">SCORES</div> 
        <div style="width: 1280px;">
            <div style="background-color:#FDD963;  width:640px; height:360px; text-align:center; float: left;">Influencer Here </div>
            <div style="background-color:#F248FE;  width:640px; height:360px; text-align:center; float: right;">Influencer Here </div>
        </div>
        <div style="width:1280px; height:360px; background-color:#66F836; text-align:center;">FAYBLE</div>
    </div>
    <!-- scores, fayble, and influencers -->

    <div style="float: right; width:640px; height: 1080px;">
        <div style="background-color:#A45EF7; width:638px; height:178px; border: 1px solid #000000;">
            <img style="float: left; width: 60px; height: 60 px; margin: 25px; 
            border-radius: 40px; background-color:#000000; border:1px solid #000000;" src='usa.png'/>
            <h3 style= "margin-top: 30px;"> USA </h3>
            <p style="margin: 10px; overflow: hidden;"> He did it again! The series is now tied 3-3! Next game will be held at Staples
                center! Come and see the final round at the NBA playoffs! </p>
        </div>
        <div style="background-color:#FF5E1D; width:638px; height:178px; border: 1px solid #000000;">
            <img style="float: left; width: 60px; height: 60 px; margin: 25px; 
            border-radius: 40px; background-color:#000000; border:1px solid #000000;" src='china.png'/>
            <h3 style= "margin-top: 30px;"> China </h3>
            <p style="margin: 10px; overflow: hidden;"> Yao Ming has been amazing this year! Scoring 30 points, 5 rebounds, 9 assists!
            Can't wait to see what else he has to offer this season! </p>
        </div>
        <div style="background-color:#3DFDC7; width:638px; height:178px; border: 1px solid #000000;">
            <img style="float: left; width: 60px; height: 60 px; margin: 25px; 
            border-radius: 40px; background-color:#000000; border:1px solid #000000;" src='argentina.png'/>
            <h3 style= "margin-top: 30px;"> Argentina </h3>
            <p style="margin: 10px; overflow: hidden;"> Lionel Messi! What a score! Leading Barcelona to the Championships! Hat Trick! </p>
        </div>
        <div style="background-color:#f7db5e; width:638px; height:178px; border: 1px solid #000000;">
            <img style="float: left; width: 60px; height: 60 px; margin: 25px; 
            border-radius: 40px; background-color:#000000; border:1px solid #000000;" src='japan.png'/>
            <h3 style= "margin-top: 30px;"> Japan </h3>
            <p style="margin: 10px; overflow: hidden;"> Yuji Hishida with the amazing ace! Has won the series! He is the MVP of the JTEKT Stings!
            </p>
        </div>
        <div style="background-color:#5557ff; width:638px; height:178px; border: 1px solid #000000;">
            <img style="float: left; width: 60px; height: 60 px; margin: 25px; 
            border-radius: 40px; background-color:#000000; border:1px solid #000000;" src='korea.png'/>
            <h3 style= "margin-top: 30px;"> Korea </h3>
            <p style="margin: 10px; overflow: hidden;"> Bonchan Ku! Wow! All three shots were 10! This is his 3rd gold medal in the 2016 Olympics for 
            Archery!
            </p>
        </div>
        <div style="background-color:#f30d0d; width:638px; height:178px; border: 1px solid #000000;">
            <img style="float: left; width: 60px; height: 60 px; margin: 25px; 
            border-radius: 40px; background-color:#000000; border:1px solid #000000;" src='singapore.png'/>
            <h3 style= "margin-top: 30px;"> Singapore </h3>
            <p style="margin: 10px; overflow: hidden;"> Joseph Schooling! What a sensational race! This man beat his idol in the 100m
            butterfly race, securing Singapore's first ever gold medal in Olympic swimming!
            </p>
        </div>
    </div>

</body>
</html>
"""
f.write(template)

f.close()

# webbrowser.open('testingbase.html')

os.system('wkhtmltoimage --width 1920 --disable-smart-width --height 1080 --enable-local-file-access testing.html testing.png')

# os.system('c:/ffmpeg -i videos/flame.avi videos/flame.mp4')


# first frame

# new comment
"""
<div style="background-color:#f30d0d; width:638px; height:2.4px; border: 1px solid #000000;">
            <img style="float: left; width: 60px; height: 60 px; margin: 25px; 
            border-radius: 40px; background-color:#000000; border:1px solid #000000;" src='jamaica.jpg'/>
            <h3 style= "margin-top: 30px;"> Jamaica </h3>
            <p style="margin: 10px; overflow: hidden;"> Usain Bolt! This man is absolutely insane! A 9.58 second 100m dash! He has set the 
            world record!
            </p>
</div>
"""


