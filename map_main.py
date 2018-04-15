import map_html
import map_opp

def get_input_dest()-> list:
    '''
    retrieve the number of destinations, and the names of the destinations from the user
    '''
    dest_num=int(input())
    destinations=[]
    for num in range(dest_num):
        destinations.append(input().replace(' ','+'))
    return destinations

def get_input_steps()->list:
    '''
    retrieve the number of steps, and the steps from the user
    '''
    steps=int(input())
    step_list=[]
    for num in range(steps):
        step_list.append(input())
    return step_list
    
def get_dir(destinations:list)->str:
    '''
    takes in a list of destinations, returns a string of directions
    '''
    dir_str=''
    for pos in range(len(destinations)-1):
        start_end=destinations[pos],destinations[pos+1]
        dir_str+=map_opp.directions().generate(start_end)
    return dir_str


def get_time(destinations:list)->float:
    '''
    takes in a list of destinations, returns a float representing the total time
    '''
    total_time=0
    for pos in range(len(destinations)-1):
        start_end=destinations[pos],destinations[pos+1]
        total_time+=float(map_opp.time().generate(start_end))
    return total_time

def get_dist(destinations:list)->str:
    '''
    takes in a list of destinations, returns a float representing the total distance
    '''
    total_dist=0
    for pos in range(len(destinations)-1):
        start_end=destinations[pos],destinations[pos+1]
        total_dist+=float(map_opp.distance().generate(start_end))
    return total_dist

def get_elv(destinations:list)->str:
    '''
    takes in a list of destinations, returns a string of elevations
    '''
    elv_str=''
    for pos in range(len(destinations)):
        loc=destinations[pos]
        start_end=loc,loc
        elv_str+=map_opp.elevation().generate(start_end)
    return elv_str

def get_latlong(destinations:list)->str:
    '''
    takes in a list of destinations, returns a string of latitudes and longitudes
    '''
    latlong_str=''
    for pos in range(len(destinations)):
        loc=destinations[pos]
        start_end=loc,loc
        latlong_str+=map_opp.latlong().generate(start_end)
    return latlong_str

def execute_steps(step_list: list, dir_str: str, latlong_str: str,
                  total_time: str, total_dist: str, elv_str: str)->None:
    '''
    executes the steps that were inputed by the user
    '''
    for step in step_list:
        print()
        if step=='LATLONG':
            print('LATLONGS')
            print(latlong_str)
     
            
        elif step=='STEPS':
            print('DIRECTIONS')
            print(dir_str)
        
            
        elif step=='TOTALTIME':
            print('TOTAL TIME: {:.0f} minutes'.format(total_time))
  
            
        elif step=='TOTALDISTANCE':
            print('TOTAL DISTANCE: {:.0f} miles'.format(total_dist))
  
            
        elif step=='ELEVATION':
            print('ELEVATIONS')
            print(elv_str)

def main():
    '''
    The main function that executes the mapquest program
    '''
    try:
        destinations=get_input_dest()
        step_list=get_input_steps()
    
    
        dir_str=get_dir(destinations)
        latlong_str=get_latlong(destinations)
        total_time=get_time(destinations)
        total_dist=get_dist(destinations)
        elv_str=get_elv(destinations)

        execute_steps(step_list,dir_str,latlong_str,total_time,total_dist,elv_str)

    except map_html.NoRouteFoundError:
        print()
        print('No Route Found')

    except:
        print()
        print('MAPQUEST ERROR')
        
if __name__ == '__main__':
    main()
