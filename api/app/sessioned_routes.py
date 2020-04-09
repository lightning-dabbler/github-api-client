from flask import session,Blueprint,jsonify,request

import logging
logger = logging.getLogger(__name__)

session_bp = Blueprint('session_bp',__name__)

@session_bp.route('/api/session/test',methods=['GET'])
def test():
    logger.info(f'Route = {request.url}')

    increment = bool(request.args.get('increment',False))
    reset = bool(request.args.get('reset',False))
    val = int(request.args.get('val',0))
    exists = session.get('val',False)
    stored_val = exists
    exists = True if type(exists)!=bool else False
    delete = bool(request.args.get('delete',False))
    logger.debug(f'increment = {increment}, reset = {reset}, val = {val}, exists = {exists}, delete = {delete}')

    if reset:
        session['val'] = val
        # session.modified = True
        logger.debug(f'Val set = {val}')
    elif exists and increment:
        logger.debug(f'{type(exists)}, val = {stored_val}')
        stored_val+=1
        session['val'] = stored_val
        # session.modified = True
        logger.debug(f'New val = {exists}')
    elif not exists:
        session['val'] = val
    elif delete:
        deleted = session.pop('val',None)
        if deleted:
            logger.debug(f'val deleted = {deleted}')
        else:
            logger.debug(f"val doesn't exist to delete !")
    
    return jsonify({'val':session.get('val',None),'cookies':request.cookies})
