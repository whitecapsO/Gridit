from farmware_tools import app
from farmware_tools import device
from farmware_tools import env
from farmware_tools import get_config_value

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

    # *** Start Test Move ***

    # Initialise or increment x, z position
    xPos = startX + (spaceBetweenRows)
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