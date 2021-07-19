import os
import webbrowser
from functions import createsequence

# create a for loop, length with number of frames, 75
# decrease upper box height by 2.4
# increase total bottom box height by 2.4
# iterate 75 times, each creating an image to sequence folder
# end frame, upper box completely gone, and bottom box completely uploaded

# testing first frame

def simpleanimate():
    # images: scores.png, influencers.png, fayble.png, comments.png
    # parse into all images based on image names written above
    # create html document with open and write
    # parse the collection of the nine images into one final image

    # parsing score.png
    imagelist = ['scores.png', 'influencers.png', 'fayble.png', 
    'comments.png', 'middle.png']
    f = open('scores.html', 'w')

    template = """
    <div style="background-color:#62affc;  width:1280px; height:360px; text-align:center">Scores</div>
    """

    f.write(template)
    f.close()

    command = 'wkhtmltoimage --width 1280 --disable-smart-width --height 360 --enable-local-file-access scores.html ' + imagelist[0]

    os.system(command)

    # parsing influencers.png
    f = open('influencers.html', 'w')

    template = """
    <div style="width: 1280px;">
        <div style="background-color:#FDD963;  width:640px; height:360px; text-align:center; float: left;">Influencer Here </div>
        <div style="background-color:#F248FE;  width:640px; height:360px; text-align:center; float: right;">Influencer Here </div>
    </div>
    """

    f.write(template)
    f.close()

    command = 'wkhtmltoimage --width 1280 --disable-smart-width --height 360 --enable-local-file-access influencers.html ' + imagelist[1]

    os.system(command)

    # parsing fayble.png
    f = open('fayble.html', 'w')

    template = """
    <div style="width:1280px; height:360px; background-color:#66F836; text-align:center;">FAYBLE</div>
    """

    f.write(template)
    f.close()

    command = 'wkhtmltoimage --width 1280 --disable-smart-width --height 360 --enable-local-file-access fayble.html ' + imagelist[2]

    os.system(command)

    # parsing all comments
    
    f = open('comments.html', 'w')

    template = """
        <div style="background-color:#A45EF7; width:638px; height:178px; border: 1px solid #000000;">
            <img style="float: left; width: 60px; height: 60 px; margin: 25px; 
            border-radius: 40px; background-color:#000000; border:1px solid #000000;" src='countries/usa.png'/>
            <h3 style= "margin-top: 30px;"> USA </h3>
            <p style="margin: 10px; overflow: hidden;"> He did it again! The series is now tied 3-3! Next game will be held at Staples
                center! Come and see the final round at the NBA playoffs! </p>
        </div>
        <div style="background-color:#FF5E1D; width:638px; height:178px; border: 1px solid #000000;">
            <img style="float: left; width: 60px; height: 60 px; margin: 25px; 
            border-radius: 40px; background-color:#000000; border:1px solid #000000;" src='countries/china.png'/>
            <h3 style= "margin-top: 30px;"> China </h3>
            <p style="margin: 10px; overflow: hidden;"> Yao Ming has been amazing this year! Scoring 30 points, 5 rebounds, 9 assists!
            Can't wait to see what else he has to offer this season! </p>
        </div>
        <div style="background-color:#3DFDC7; width:638px; height:178px; border: 1px solid #000000;">
            <img style="float: left; width: 60px; height: 60 px; margin: 25px; 
            border-radius: 40px; background-color:#000000; border:1px solid #000000;" src='countries/argentina.png'/>
            <h3 style= "margin-top: 30px;"> Argentina </h3>
            <p style="margin: 10px; overflow: hidden;"> Lionel Messi! What a score! Leading Barcelona to the Championships! Hat Trick! </p>
        </div>
        <div style="background-color:#f7db5e; width:638px; height:178px; border: 1px solid #000000;">
            <img style="float: left; width: 60px; height: 60 px; margin: 25px; 
            border-radius: 40px; background-color:#000000; border:1px solid #000000;" src='countries/japan.png'/>
            <h3 style= "margin-top: 30px;"> Japan </h3>
            <p style="margin: 10px; overflow: hidden;"> Yuji Hishida with the amazing ace! Has won the series! He is the MVP of the JTEKT Stings!
            </p>
        </div>
        <div style="background-color:#5557ff; width:638px; height:178px; border: 1px solid #000000;">
            <img style="float: left; width: 60px; height: 60 px; margin: 25px; 
            border-radius: 40px; background-color:#000000; border:1px solid #000000;" src='countries/korea.png'/>
            <h3 style= "margin-top: 30px;"> Korea </h3>
            <p style="margin: 10px; overflow: hidden;"> Bonchan Ku! Wow! All three shots were 10! This is his 3rd gold medal in the 2016 Olympics for 
            Archery!
            </p>
        </div>
        <div style="background-color:#f30d0d; width:638px; height:178px; border: 1px solid #000000;">
            <img style="float: left; width: 60px; height: 60 px; margin: 25px; 
            border-radius: 40px; background-color:#000000; border:1px solid #000000;" src='countries/singapore.png'/>
            <h3 style= "margin-top: 30px;"> Singapore </h3>
            <p style="margin: 10px; overflow: hidden;"> Joseph Schooling! What a sensational race! This man beat his idol in the 100m
            butterfly race, securing Singapore's first ever gold medal in Olympic swimming!
            </p>
        </div>
        <div style="background-color:#fa9df2; width:638px; height:178px; border: 1px solid #000000;">
            <img style="float: left; width: 60px; height: 60 px; margin: 25px; 
            border-radius: 40px; background-color:#000000; border:1px solid #000000;" src='countries/jamaica.jpg'/>
            <h3 style= "margin-top: 30px;"> Jamaica </h3>
            <p style="margin: 10px; overflow: hidden;"> Usain Bolt! This man is absolutely insane! A 9.58 second 100m dash! He has set the 
            world record!
            </p>
        </div>
    """

    f.write(template)
    f.close()

    command = 'wkhtmltoimage --width 640 --disable-smart-width --height 1260 --enable-local-file-access comments.html ' + imagelist[3]

    os.system(command)

    # cropping the image using imagemagick
    # convert image.png -gravity South -chop 0x20 result.png
    command1 = 'magick convert comments.png -gravity South -chop 0x90 comments.png'
    command2 = 'magick convert comments.png -gravity North -chop 0x90 comments.png'

    os.system(command1)
    os.system(command2)

    # final composition of all images
    f = open('final.html', 'w')

    template = """
    <html>
        <head>
            <title>Animation</title>
        </head>
        <body>
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
                <img src='comments.png'/>
                
            </div>
        </div>
        </body>
    """
    f.write(template)
    f.close()

    command = 'wkhtmltoimage --width 1920 --disable-smart-width --height 1080 --enable-local-file-access final.html ' + imagelist[4]

    os.system(command)




# first frame
def animate():

    # naming for image list

    imagelist = ['scores.png', 'influencers.png', 'fayble.png', 
    'comments.png', 'middle.png']
    
    # cropping comments
    croptop = 0
    cropbottom = 0
    command1 = 'magick convert comments.png -gravity South -chop 0x{0} comments.png'.format(croptop)
    command2 = 'magick convert comments.png -gravity North -chop 0x{0} comments.png'.format(cropbottom)
    

    f = open('final.html', 'w')

    template = """
    <html>
        <head>
            <title>Animation</title>
        </head>
        <body>
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
                <img src='comments.png'/>
                
            </div>
        </div>
        </body>
    """
    f.write(template)
    f.close()

    command = 'wkhtmltoimage --width 1920 --disable-smart-width --height 1080 --enable-local-file-access final.html ' + imagelist[4]

    os.system(command)
    


simpleanimate()

if False:
    f = open('testing.html', 'w')

    top_height = 178 - (10 + 1) * 2.4
    bottom_height = 0.4 + 10 * 2.4

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
            <div style="background-color:#A45EF7; width:638px; height:{0}px; border: 1px solid #000000;">
            </div>
            <div style="background-color:#FF5E1D; width:638px; height:178px; border: 1px solid #000000;">
            </div>
            <div style="background-color:#3DFDC7; width:638px; height:178px; border: 1px solid #000000;">
            </div>
            <div style="background-color:#f7db5e; width:638px; height:178px; border: 1px solid #000000;">
            </div>
            <div style="background-color:#5557ff; width:638px; height:178px; border: 1px solid #000000;">
            </div>
            <div style="background-color:#f30d0d; width:638px; height:178px; border: 1px solid #000000;">
            </div>
            <div style="background-color:#10CE42; width:638px; height:{1}px; border: 1px solid #000000;">
            </div>
        </div>
    </div>
    """.format(top_height, bottom_height)

    # setting new heights

    # formatting the html template


    f.write(template)

    f.close()

    webbrowser.open('testing.html')

    command = 'wkhtmltoimage --width 1920 --disable-smart-width --height 1080 --enable-local-file-access testing.html ' + 'sequence/test.png'

    os.system(command)