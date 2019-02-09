import sys

import pdb; pdb.set_trace()  # breakpoint 9c23e2cd //
if __name__ == "__main__":
    import pdb; pdb.set_trace()  # breakpoint 7b00e119 //
    farmwareName = "gridit"
    reload(sys)
    sys.setdefaultencoding('utf8')  # force utf8 for celerypy return code

    try:
        farmware = main.gridit()
    except Exception as e:
        raise Exception(e)
        raise Exception(e)
    else:
        try:
            farmware.run()
        except Exception as e:
                raise Exception(e)
