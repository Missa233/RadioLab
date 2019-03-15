
import numpy as np
import time
import ugradio
import ugradio.interf_delay
def track(Ra,Dec):
    ifm = ugradio.interf.Interferometer()

    while True:
        AltAz = ugradio.coord.get_altaz(Ra,Dec)
        alt = AltAz[0]
        az = AltAz[1]
        ifm.point(alt,az)
        time.sleep(60)
            

def track_collect(Ra,Dec):
    ifm = ugradio.interf.Interferometer()
    hpm = ugradio.hp_multi.HP_Multimeter()
    i = 0
    dt = 1
    
    AltAz = ugradio.coord.get_altaz(Ra,Dec)
    alt = AltAz[0]
    az = AltAz[1]
    ifm.point(alt,az)
    time.sleep(60)
    hpm.start_recording(dt)
    while True:
        i+=1
        AltAz = ugradio.coord.get_altaz(Ra,Dec)
        alt = AltAz[0]
        az = AltAz[1]
        ifm.point(alt,az) 
        if( i == 4):
            hpm.end_recording()
            data = hpm.get_recording_data()
            np.savez('Mars_test.npz',data=data)
            ifm.stow()
            break
        time.sleep(60)
        
        
def observation_run(Ra,Dec,dur,inter,data_file_name):
    '''
    Arguments:
    Ra is your object's right ascension in degrees
    Dec is your object's declination in degrees
    dur is the duration of your capture run in seconds
    inter is the interval between data samples (in seconds)
    data_file_name is your data file's name :o
    
    Returns:
    a data file, 'data_file_name.npz' containing the data 
    from your observation run.
    '''
    
    d = ugradio.interf_delay.DelayClient()
    d.delay_ns(0)
    ifm = ugradio.interf.Interferometer()
    hpm = ugradio.hp_multi.HP_Multimeter()
    i = 0
    
    RAdecp = ugradio.coord.precess(Ra,Dec)
    AltAz = ugradio.coord.get_altaz(RAdecp[0], RAdecp[1])
    alt = AltAz[0]
    az = AltAz[1]
    ifm.point(alt,az)
    time.sleep(60)
    hpm.start_recording(inter)
    try:
        while True:
        
            i+=1
            RAdecp = ugradio.coord.precess(Ra,Dec)
            AltAz = ugradio.coord.get_altaz(RAdecp[0], RAdecp[1])
            alt = AltAz[0]
            az = AltAz[1]
            ifm.point(alt,az) 
            if (i%10 == 0):
                intermediate_data = hpm.get_recording_data()
                np.savez(data_file_name + str(i) + '.npz', volts = intermediate_data[0], time = intermediate_data[1]) 
            if(i*60>dur):
                data = hpm.get_recording_data()
                np.savez(data_file_name+'.npz',volts = data[0], time = data[1])
                break
            time.sleep(60)
    except:
        print('an error occurred but at least your data was saved! yeet')
    finally:
        final_data = hpm.get_recording_data()
        np.savez(data_file_name + 'final.npz', volts=final_data[0], time=final_data[1])
        hpm.end_recording()
        ifm.stow()


        
def observe_moon(Ra,Dec,dur,inter,data_file_name):
    '''
    Arguments:
    Ra is your object's right ascension in degrees
    Dec is your object's declination in degrees
    dur is the duration of your capture run in seconds
    inter is the interval between data samples (in seconds)
    data_file_name is your data file's name :o
    
    Returns:
    a data file, 'data_file_name.npz' containing the data 
    from your observation run.
    '''
    d = ugradio.interf_delay.DelayClient()
    d.delay_ns(0)
    ifm = ugradio.interf.Interferometer()
    hpm = ugradio.hp_multi.HP_Multimeter()
    i = 0
    
    AltAz = ugradio.coord.get_altaz(Ra, Dec, equinox='J2019')
    alt = AltAz[0]
    az = AltAz[1]
    ifm.point(alt,az)
    time.sleep(60)
    hpm.start_recording(inter)
    try:
        while True:
        
            i+=1
            AltAz = ugradio.coord.get_altaz(Ra, Dec, equinox='J2019')
            alt = AltAz[0]
            az = AltAz[1]
            ifm.point(alt,az) 
            if (i%10 == 0):
                intermediate_data = hpm.get_recording_data()
                np.savez(data_file_name + str(i) + '.npz', volts = intermediate_data[0], time = intermediate_data[1]) 
            if(i*60>dur):
                data = hpm.get_recording_data()
                np.savez(data_file_name+'.npz',volts = data[0], time = data[1])
                break
            time.sleep(60)
    except:
        print('an error occurred but at least your data was saved! yeet')
    finally:
        final_data = hpm.get_recording_data()
        np.savez(data_file_name + 'final.npz', volts=final_data[0], time=final_data[1])
        hpm.end_recording()
        ifm.stow()






