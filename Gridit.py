from farmware_tools import app
from farmware_tools import device
from farmware_tools import env
from farmware_tools import get_config_value

# Values for testing
# rows = 4
# cols = 7 
# spaceBetweenRows = 47
# spaceBetweenColumns = 45 
# startX = 310.2
# startY = 563.8
# startZ = 210.96
# sequenceBeforeMove = 'PickUpSeed' 
# sequenceAfterMove = 'PlantSeed'
try:
    device.log(message='Setting variables', message_type='success')
    rows = get_config_value(farmware_name='Gridit', config_name='rows', value_type=int)
    cols = get_config_value(farmware_name='Gridit', config_name='cols', value_type=int)
    spaceBetweenRows = get_config_value(farmware_name='Gridit', config_name='spaceBetweenRows', value_type=float)
    spaceBetweenCols = get_config_value(farmware_name='Gridit', config_name='spaceBetweenCols', value_type=float)
    startX = get_config_value(farmware_name='Gridit', config_name='startX', value_type=float)
    startY = get_config_value(farmware_name='Gridit', config_name='startY', value_type=float)
    startZ = get_config_value(farmware_name='Gridit', config_name='startZ', value_type=float)
    sequenceBeforeMove = get_config_value(farmware_name='Gridit', config_name='sequenceBeforeMove', value_type=str)
    sequenceAfterMove = get_config_value(farmware_name='Gridit', config_name='sequenceAfterMove', value_type=str)


    device.log(message='Setting sequenceId variables', message_type='success')
    if sequenceBeforeMove != "":
        sequenceBeforeMoveId = app.find_sequence_by_name(name=sequenceBeforeMove)
    else :
        sequenceBeforeMoveId = 0

    if sequenceAfterMove != "":
        sequenceAfterMoveId = app.find_sequence_by_name(name=sequenceAfterMove)
    else :
        sequenceAfterMoveId = 0

    # *** Start Test Move ***

    # Initialise or increment x, z position
    xPos = startX + (spaceBetweenRows * r)
    zPos = startZ

    # Set y position back to the begining of the row
    yPos = startY

    # moveAbsolute(xPos, yPos, startZ)
    device.log('Moving to ' + str(xPos) + ', ' + str(yPos) + ', ' + str(zPos), 'success', ['toast'])

    device.move_absolute(
        device.assemble_coordinate(xPos, yPos, zPos),
        100,
        device.assemble_coordinate(0, 0, 0))

    # *** End Test Move ***
except Exception as error:
    device.log(repr(error))