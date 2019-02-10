from farmware_tools import device, app

device.log(message='Hello Farmware!', message_type='success')


# def runSequence(sequenceName):
#     sequence_id = app.find_sequence_by_name('name=' + sequenceName)
#     device.execute(sequence_id)


# def moveAbsolute(x, y, z):
#     device.log('Moving to ' + str(x) + ', ' + str(y) + ', ' + str(z), 'success', ['toast'])
#     device.move_absolute(
#         {
#             'kind': 'coordinate',
#             'args': {'x': x, 'y': y, 'z': z}
#         },
#         100,
#         {
#             'kind': 'coordinate',
#             'args': {'x': 0, 'y': 0, 'z': 0}
#         }
#     )

device.log(message='Setting variables', message_type='success')

rows = 4
cols = 7
spaceBetweenRows = 47
spaceBetweenColumns = 45
startX = 310.2
startY = 563.8
startZ = 200.96
sequenceBeforeMove = ''
sequenceAfterMove = ''

device.log(message='Starting row loop', message_type='success')

# Start the grid movement
for r in range(rows):

    # Initialise or increment x position
    xPos = startX + (spaceBetweenRows * r)

    # Set y position back to the begining of the row
    yPos = startY

    zPos = startZ

    device.log(message='Set positions', message_type='success')

    for c in range(cols):
        # Run the before move sequence
        if sequenceBeforeMove != "":
            # runSequence(sequenceBeforeMove)
            sequence_id = app.find_sequence_by_name('name=' + sequenceBeforeMove)
            device.execute(sequence_id)

        # moveAbsolute(xPos, yPos, startZ)
        device.log('Moving to ' + str(xPos) + ', ' + str(yPos) + ', ' + str(zPos), 'success', ['toast'])
        device.move_absolute(
            {
                'kind': 'coordinate',
                'args': {'x': xPos, 'y': yPos, 'z': zPos}
            },
            100,
            {
                'kind': 'coordinate',
                'args': {'x': 0, 'y': 0, 'z': 0}
            }
        )

        # Run after move sequence
        if sequenceAfterMove != "":
            # runSequence(sequenceAfterMove)
            sequence_id = app.find_sequence_by_name('name=' + sequenceAfterMove)
            device.execute(sequence_id)

        # Increment y position
        yPos = yPos + spaceBetweenColumns
