from PIL import Image, ImageDraw
import random
import math

# todo: generate multiple lines starting from varying Y values

imgX = 1000
imgY = 1000

BLACK_A = (0, 0, 0, 255)
WHITE_A = (255, 255, 255, 255)

MAX_SEGMENT_LENGTH = 10
MAX_TOTAL_SEGMENT_LENGTH = 1000

MAX_NUM_LINES = 10
Y_THESHOLD = 50

LINE_WIDTH = 1


for i in range(10):
    f = open(str(i) + ".txt", "w")

    # Generates random distances for each line in the X axis up until the max distance is reached
    distancesX = []
    total = 0
    while (total < MAX_TOTAL_SEGMENT_LENGTH):
        rand = random.randint(0, MAX_SEGMENT_LENGTH)
        total += rand
        distancesX.append(rand)
    
    # Generates random distances for each line in the Y axis up until the max distance is reached
    distancesY = []
    total = 0
    for _ in range(len(distancesX)):
        rand = random.randint(0, MAX_SEGMENT_LENGTH)
        total += rand
        distancesY.append(rand)

    # Generates starting Y positions for each line
    startingY = []
    for _ in range(MAX_NUM_LINES):
        rand = random.randint(Y_THESHOLD, imgY - Y_THESHOLD)
        startingY.append(rand)

    # Initialize image and draw instances
    img = Image.new(mode='RGBA', size=(imgX, imgY))
    draw = ImageDraw.Draw(img)

    # Circle outline
    draw.ellipse((0, 0, 1000, 1000), BLACK_A, BLACK_A)

    # Draws lines from distances generated
    for n in startingY:
        newX = 0
        newY = n
        for x, y in zip(distancesX, distancesY):
            ###
            # Finds the chord of the circle based on the pythagorean theorem
            # Figure out the distance on the Y axis from the center of the cirlce
            # and using the radius figure out the length of the horizontal chord
            ###
            distanceFromCenter = math.pow(math.fabs(newY + y - (imgY / 2)), 2) # a^2, account for next Y position
            radius = math.pow(imgY / 2, 2) # cb^2
            try:
                chordLength = math.sqrt(radius - distanceFromCenter) * 2 # b^2, solved
            except ValueError:
                print("This doesn't seem to affect it... and I have no idea what's causing the distance from the center to be >500.")

            extraDistance = (imgX - chordLength) / 2 # Accounts for distance fron edge of image

            # Starts line from edge of circle
            if (newX == 0):
                newX += extraDistance
                f.write("LINE START:\n")
                f.write("Chord: " + str(chordLength) + "\n")
                print("Chord: " + str(chordLength))
                f.write("Y: " + str(n) + "\n")
                print("Y: " + str(n))
    
            # Checks if next line would go over, if yes then draw line to edge
            if (newX + x > chordLength + extraDistance):
                lastX = (chordLength + extraDistance) - newX 
                f.write("lastX: " + str(lastX))
                print("lastX: " + str(lastX))
                draw.line((newX, newY, newX + lastX, newY + y), WHITE_A, LINE_WIDTH)
                break;

                # Randomizes up or down
            if random.choice([True, False]):
                y = -y
            draw.line((newX, newY, newX + x, newY + y), WHITE_A, LINE_WIDTH)
            newX += x
            newY += y

    del draw

    img.save(str(i) + ".png")
    f.close()