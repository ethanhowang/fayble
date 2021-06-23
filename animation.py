import os
import webbrowser
from functions import createsequence

# create a for loop, length with number of frames, 75
# decrease upper box height by 2.4
# increase total bottom box height by 2.4
# iterate 75 times, each creating an image to sequence folder
# end frame, upper box completely gone, and bottom box completely uploaded


# first frame
def animate(frames):

    imagelist = createsequence(frames)

    for i in range(frames):

        if i < 25:

            if i == 0:

                f = open('testing.html', 'w')

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
                    </div>
                </div>
                """
                f.write(template)

                f.close()




        elif i < 37:

            f = open('testing.html', 'w')

            top_height = 178 - ((i - 25) + 1) * 15
            bottom_height = 0.4 + (i - 25) * 15

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

            

            # formatting the html template
            template.format(toph = top_height, bottomh = bottom_height)

            f.write(template)

            f.close()

        else:

            f = open('testing.html', 'w')

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
                    <div style="background-color:#10CE42; width:638px; height:178px; border: 1px solid #000000;">
                    </div>
                </div>
            </div>
            """

            f.write(template)

            f.close()

        # setting the command

        command = 'wkhtmltoimage --width 1920 --disable-smart-width --height 1080 --enable-local-file-access testing.html ' + 'sequence/' + imagelist[i]

        os.system(command)

    os.system('c:/ffmpeg -r 25 -s 1920x1080 -i sequence/%04d.png -pix_fmt yuv420p animation.mp4')

animate(75)

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