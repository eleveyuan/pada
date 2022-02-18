import logging

import kada

TRACE = 7
SIMPLE_LOG_FORMAT = r'%(levelname)s - %(message)s'
DETAIL_LOG_FORMAT = r'[%(asctime)s] {%(name)s: %(filename)s:%(lineno)d} %(levelname)s - %(message)s'  # noqa E501


logging.addLevelName(TRACE, 'TRACE')
logger = logging.getLogger(kada.__name__)
_handler = None