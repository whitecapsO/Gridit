from farmware_tools import *


def runSequence(sequenceName):
    sequence_id = app.find_sequence_by_name('name=' + sequenceName)
    device.execute(sequence_id)


def moveAbsolute(x, y, z):
    device.log('Moving to ' + str(x) + ', ' + str(y) + ', ' + str(z), 'success', ['toast'])
    device.move_absolute(
        {
            'kind': 'coordinate',
            'args': {'x': x, 'y': y, 'z': z}
        },
        100,
        {
            'kind': 'coordinate',
            'args': {'x': 0, 'y': 0, 'z': 0}
        }
    )


rows = 4
cols = 7
spaceBetweenRows = 47
spaceBetweenColumns = 45
startX = 310.2
startY = 563.8
startZ = 200.96
sequenceBeforeMove = ''
sequenceAfterMove = ''

# Start the grid movement
for r in range(rows):

    # Initialise or increment x position
    xPos = startX + (spaceBetweenRows * r)

    # Set y position back to the begining of the row
    yPos = startY

    for c in range(cols):
        # Run the before move sequence
        if sequenceBeforeMove != "":
            runSequence(sequenceBeforeMove)
            moveAbsolute(xPos, yPos, startZ)

        # Run after move sequence
        if sequenceAfterMove != "":
            runSequence(sequenceAfterMove)

        # Increment y position
        yPos = yPos + spaceBetweenColumns

