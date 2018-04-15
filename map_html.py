import http.client
import urllib.request
import urllib.error
import json
import urllib.parse

key='h9l8GngD4qpZ2qCfrc1KuGcx09tOELvt'


class NoRouteFoundError(Exception):
    '''
    error class for NO ROUTE FOUND
    '''
    pass

def handle_api_dir(start_end: tuple)->'json text':
    '''
    Function that handles the directions api. Takes in a tuple with the start and
    end point, and returns the json text
    '''
    start_point,end_point=start_end
    http='http://open.mapquestapi.com/directions/v2/route?key='+key+'&ambiguities=ignore&from='+start_point+'&to='+end_point
    response = urllib.request.urlopen(http)
    json_text = response.read().decode(encoding = 'utf-8')
    json_text_fin=json.loads(json_text)

    if json_text_fin['info']['messages']==['We are unable to route with the given locations.']:
        raise NoRouteFoundError

    return json_text_fin

def handle_api_elv(latlong: dict)->'json text':
    '''
    Function that handles the elevation api. Takes in a dictionary with the latitude and
    and longitude, and returns the json text
    '''
    elivation_http='http://open.mapquestapi.com/elevation/v1/profile?key=h9l8GngD4qpZ2qCfrc1KuGcx09tOELvt&shapeFormat=raw&unit=f&latLngCollection='+str(latlong['lat'])+','+str(latlong['lng'])
    response_elv = urllib.request.urlopen(elivation_http)
    json_text_elv = response_elv.read().decode(encoding = 'utf-8')
    json_text_fin_elv=json.loads(json_text_elv)
    return json_text_fin_elv









