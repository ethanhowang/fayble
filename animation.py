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
<div style="background-color:#BFC0C2; width:1920px; height:1080px; border:2px solid #5D6063;"> 
    <div style="display:flex; justify-content:flex-start; width:1280px;">
        <div style="display: flex;">
            <div style="background-color:#63B0FD;  width:1280px; height:360px; text-align:center">SCORES</div>
        </div>
        <div style="display:flex; justify-content:flex-start;">
            <div style="background-color:#FDD963;  width:640px; height:360px; text-align:center;">Influencer Here </div>
            <div style="background-color:#F248FE;  width:640px; height:360px; text-align:center;">Influencer Here </div>
        </div>
        <div style="justify-content:flex-start; width:1280px; height:360px; background-color:#66F836; text-align:center;">
        FAYBLE
        </div>
    </div>
    <div style="display:flex; justify-content:flex-end; width:

</div>

</body>
</html>
"""
f.write(template)

f.close

webbrowser.open('testing.html')

# os.system('ffmpeg -i videos/flame.avi videos/flame.mp4')



