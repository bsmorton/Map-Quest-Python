import map_html


class directions:
    '''
    directions class, generates a string of directions
    '''
    def generate(self,start_end:tuple)->str:
        routedict=map_html.handle_api_dir(start_end)
        dir_str=''
        for item in routedict['route']['legs'][0]['maneuvers']:
             dir_str+=item['narrative']+'\n'
        return dir_str

class latlong:
    '''
    latlong class, generates a string of latlongs
    '''
    def generate(self,start_end:tuple)->str:
        routedict=map_html.handle_api_dir(start_end)
        latlong_dict=routedict['route']['legs'][0]['maneuvers'][0]['startPoint']
        l_string=''
        if latlong_dict['lat']>=0:
            str_temp='{:.2f}'.format(latlong_dict['lat'])
            l_string+=str_temp+'N '
        else:
            str_temp='{:.2f}'.format(latlong_dict['lat'])
            l_string+=str_temp[1:]+'S '
        if latlong_dict['lng']>=0:
            str_temp='{:.2f}'.format(latlong_dict['lng'])
            l_string+=str_temp+'E'
        else:
            str_temp='{:.2f}'.format(latlong_dict['lng'])
            l_string+=str_temp[1:]+'W'
        return l_string+'\n'

class time:
    '''
    time class, generates a string representation of the total time
    '''
    def generate(self,start_end:tuple)->str:
        routedict=map_html.handle_api_dir(start_end)
        return str(routedict['route']['time']/60)

class distance:
    '''
    distance class, generates a string representation of the total distance
    '''
    def generate(self,start_end:tuple)->str:
        routedict=map_html.handle_api_dir(start_end)
        return str(routedict['route']['distance'])

class elevation:
    '''
    elevation class, generates a string of elevations
    '''
    def generate(self,start_end:tuple)->str:
        routedict=map_html.handle_api_dir(start_end)
        latlong_dict=routedict['route']['legs'][0]['maneuvers'][0]['startPoint']
        routedict_elv=map_html.handle_api_elv(latlong_dict)
        return str('{:.0f}'.format(routedict_elv["elevationProfile"][0]['height']))+'\n'
