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
startZ = 210.96
sequenceBeforeMove = 'PickUpSeed'
sequenceAfterMove = 'PlantSeed'

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
            try:
                device.log(message='Find sequence by name: ' + sequenceBeforeMove, message_type='success')
                sequence_id = app.find_sequence_by_name('name=' + sequenceBeforeMove)
                device.log(message='Execute sequence: ' + sequenceBeforeMove, message_type='success')
                device.execute(sequence_id)
                pass
            except Exception as e:
                device.log(message=e.message, message_type='success')
                raise e

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
            device.log(message='Find sequence by name: ' + sequenceAfterMove, message_type='success')
            sequence_id = app.find_sequence_by_name('name=' + sequenceAfterMove)
            device.log(message='Execute sequence: ' + sequenceAfterMove, message_type='success')
            device.execute(sequence_id)

        # Increment y position
        yPos = yPos + spaceBetweenColumns
