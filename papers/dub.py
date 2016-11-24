#define dominate
#input dim list: dim used
scale =  [ 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85 ]



def dominate( p1, p2, dim_list ):
    flag = True
    for i in dim_list:
        if p1[i] < p2[i]:
            flag = False
            break
    return flag



#compute distance between points
def distance( p1, p2, dim_list ):
    dist = 0
    for i in dim_list:
        dist = dist + ( p1[i] - p2[i] )**2
    dist = math.sqrt( dist )
    #print( p1, p2, dist)
    return dist



#compute density
#input deci
def density( point, r, dim_list ):
    p = point
    p_density = 0

    for each_point in allpoint_set:
        #print each_point, p, dim_list
        if ( distance( each_point, p, dim_list ) <= r ):
            p_density = p_density + 1

    return p_density


#binary search
def find_density( point, t, dim_list ):
    p = copy.copy( point )
    low = 0
    high = 0

    for i in dim_list:
        j = 1
        for each in scale:
            j += 1
            if each > p[i]:
                low = j - 1
                break
            
        high = k - 5
        
        while ( 1 < high - low ):
            #print p, low, high
            mid  = int( (low + high)/2 )
            
            #print low, high
            p[i] = scale[mid]
            
            if( density( p, r, dim_list ) >= t ):
                low = mid
            else:
                high = mid                
            #print low, high                                                   
        #low or high
        p[i] = scale[high]
        if density( p, r, dim_list ) < t:
            p[i] = scale[low]
        #print "c",p[i]
    
    return p

#update
def candidate_update(C, p_bound, t, dim_list ):
    C_new = []
    for each in C:        
        if dominate( p_bound, each, dim_list ):           
            #print p_bound, each           
            for i in dim_list :
                p_ = copy.copy( each )                
                p_ [i] =  p_bound[i] + 1.0/k               
                p_[i] = round( p_[i], 2 )  
                #print "s", each, p_[i], p_bound[i]             
                #print p_,  density (p_, r, dim_list )
                if ( density (p_, r, dim_list ) >= t ) and scale[-1] + 1.0/k != p_[i]:
                    C_new.append(p_)
        else:
            C_new.append(each)
    return C_new

# input data







from decimal import *

T = 500
R = 0.05
init_p = [ 0.1, 0.1, 0, 0, 0 ] #0.3*k1



#list_dim_list = [[ 0,1,2,3,4 ]]
#initial comittee
def find_boundary( init_p, list_dim_list, rr ):
    SetMaxBound = []
    for dim_list in list_dim_list:
        MaxBound = []
        Candidate = []
        Candidate.append( init_p )
        r = rr*math.sqrt( len(dim_list) )
        print r
        while( len(Candidate) > 0 ):
            p_c = Candidate[0]
            p_bound = find_density( p_c, T, dim_list )   
            MaxBound.append(p_bound)
            Candidate = candidate_update( Candidate, p_bound, T, dim_list )
        MaxBound = [x + [0] for x in MaxBound]
        SetMaxBound.append( MaxBound )    
        print dim_list, MaxBound
    return SetMaxBound



SetMaxBound = find_boundary( init_p, list_dim_list, R )




