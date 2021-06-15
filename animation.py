import os
import webbrowser
import codecs
import subprocess



f = open('testing.html', 'w')

template = """
<html>
<head>
    <title>Animation</title>
</head>
</body>
<div style="background-color:#BFC0C2; width:1920px; height:1080px;"> 
    <div style="float: left; width:1280px;">
        <div style="background-color:#62affc;  width:1280px; height:360px; text-align:center">SCORES</div> 
        <div style="width: 1280px;">
            <div style="background-color:#FDD963;  width:640px; height:360px; text-align:center; float: left;">Influencer Here </div>
            <div style="background-color:#F248FE;  width:640px; height:360px; text-align:center; float: right;">Influencer Here </div>
        </div>
        <div style="width:1280px; height:360px; background-color:#66F836; text-align:center;">FAYBLE</div>
    </div>
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
        <div style="background-color:#A45EF7; width:638px; height:178px; border: 1px solid #000000;"> Country 1 </div>
        <div style="background-color:#A45EF7; width:638px; height:178px; border: 1px solid #000000;"> Country 1 </div>
        <div style="background-color:#A45EF7; width:638px; height:178px; border: 1px solid #000000;"> Country 1 </div>
    </div>

</div>
</body>
</html>
"""
f.write(template)

f.close

# webbrowser.open('testing.html')

os.system('wkhtmltoimage --width 1920 --disable-smart-width --height 1080 --enable-local-file-access testing.html testing.png')

# os.system('c:/ffmpeg -i videos/flame.avi videos/flame.mp4')



