# ============================================================================= #
#                                   BACKEND                                     #
# ============================================================================= #
import logging
from fastapi import FastAPI
import constants

# ============================================================================= #

logger = logging.getLogger('uvicorn.info')

app = FastAPI()

logger.info('Loading Router ...')
for (name, module) in constants.GAMES:
    try:
        app.include_router(module.router)
        logger.info('    > Loaded {}-Router'.format(name.capitalize()))
    except AttributeError as err:
        logger.error('    > Couldn\'t load {}-Router : Module {} has no attribute \'router\''.format(name.capitalize(), name))

    except Exception as ex:
        logger.error('    > Couldn\'t load {}-Router because of an unexpected error: {}'.format(name.capitalize(), str(ex)))

# ============================================================================= #

