# TODO change repository name from Farmware to gridit

from Farmware import *

APP_NAME = ((__file__.split(os.sep))[len(__file__.split(os.sep)) - 3]).replace('-master', '')


class gridit(Farmware):
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        Farmware.__init__(self, ((__file__.split(os.sep))[len(__file__.split(os.sep)) - 3]).replace('-master', '').replace('-dev', ''))

    # ------------------------------------------------------------------------------------------------------------------
    def load_config(self):

        super(gridit, self).load_config()

        # TODO initialise row and column args to default values
        self.get_arg('rows', 4)
        self.get_arg('cols', 2)
        self.get_arg('spaceBetweenRows', 1)
        self.get_arg('spaceBetweenColumns', 1)
        self.get_arg('startX', 0)
        self.get_arg('startY', 0)
        self.get_arg('startZ', 0)
        self.get_arg('sequenceBeforeMove', "")
        self.get_arg('sequenceAfterMove', "")

        if self.args['rows'] < 0 or self.args['rows'] > 20 or self.args['cols'] < 0 or self.args['cols'] > 20:
            raise ValueError('Invalid rows {} or columns {}. Expecting a number 0-20'.format(self.args['rows'], self.args['cols']))
        # if self.args['operation']=='log': self.debug=True

        self.log(str(self.args))

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

    def runSequence(sequenceName):
        sequence_id = app.find_sequence_by_name(name=sequenceName)
        device.execute(sequence_id)

    # ------------------------------------------------------------------------------------------------------------------
    def run(self):

        # Start the grid movement
        for r in range(self.args['rows']):

            # Initialise or increment x position
            xPos = self.args['startX'] + (self.args['spaceBetweenRows'] * r)

            # Set y position back to the begining of the row
            yPos = self.args['startY']

            for c in range(self.args['cols']):
                # Run the before move sequence
                if self.args['sequenceBeforeMove'] != "":
                    self.runSequence(self.args['sequenceBeforeMove'])
                    self.moveAbsolute(xPos, yPos, self.args['startZ'])

                # Run after move sequence
                if self.args['sequenceAfterMove'] != "":
                    self.runSequence(self.args['sequenceAfterMove'])

                # Increment y position
                yPos = yPos + self.args['spaceBetweenColumns']

# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    app = gridit()
    try:
        app.load_config()
        app.run()
        sys.exit(0)

    except NameError as error:
        app.log('SYNTAX!: {}'.format(str(error)), 'error')
        raise
    except requests.exceptions.HTTPError as error:
        app.log('HTTP error {} {} '.format(error.response.status_code, error.response.text[0:100]), 'error')
    except Exception as e:
        app.log('Something went wrong: {}'.format(str(e)), 'error')
    sys.exit(1)
