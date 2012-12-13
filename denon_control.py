#!/usr/bin/python
import telnetlib
import sys
import argparse
import time
from rsonlite import loads

HOST = '192.168.1.130'
cmd = sys.argv[1]

class Receiver:
    def __cmd__(self, cmd):
        pass

    def __query__(self, cmd):
        pass

    def cmd_with_status(self, cmd, arg):
        self.__cmd(cmd, arg)	
        time.sleep(2)
        state = self.__query(cmd)
        print 'state: %s' % state
        return state

    def verified_cmd(self, cmd, arg):
        print 'verifying %s%s' % (cmd, arg)
        state = self.cmd_with_status(cmd, args)
        return cmd + arg in state 

    def construct_cmd(self, cmd, arg):
        raw_cmd = self.command_lut[cmd]['cmd']
        try:
            raw_arg = self.command_lut[cmd]['arg'][arg]
        except:
            raw_arg = arg
        return (raw_cmd, raw_cmd)

    def power_on(self):
        pass

    def power_standby(self):
        pass

    def power_status(self):
        pass

class Denon(Receiver):
    command_lut = {}

    def __init__(self, host, port=23):
        self.tn = telnetlib.Telnet(host, port)
        command_lut = loads('denon.rson')
        #command_lut['power'] = {'cmd': 'PW', 'argument': {'on': 'ON', 'off': 'STANDBY'}} 
        #command_lut['volume'] = {'cmd': 'MV', 'argument': {'up': 'UP', 'down': 'DOWN'}} 
        
    def __cmd(self, cmd, arg):
        print 'running command %s%s' % (cmd, arg)
        self.tn.write("%s%s\r" % (cmd, arg))

    def __query(self, cmd):
        print 'running query %s' % cmd
        output = ''
        self.tn.read_eager()
        self.tn.write("%s?\r" % cmd)
        time.sleep(1)
        out = self.tn.read_eager()
        return out

    def __construct
        
    def power_on(self):
        return self.verified_cmd('PW', 'ON')

    def power_standby(self):
        return self.verified_cmd('PW', 'STANDBY')

    def power_status(self):
        return self.__query('PW')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('cmd', type=str)
    parser.add_argument('arg', type=str)
    parser.add_argument('--power', '-p', type=str, nargs='?', default='status')
    parser.add_argument('--host',        type=str, default='192.168.1.130')
    parser.add_argument('--port',        type=str, default='23')

    args = parser.parse_args()
    
    receiver = Denon(args.host, args.port)

    print 'args.power:\'%s\'' % args.power

    if args.power:
        if args.power == 'on':
            print 'cmd on'
            if receiver.power_on():
                print 'powered on'
            else:
                print 'power on failed'
        if args.power == 'off':
            print 'cmd off'
            receiver.power_standby()
        if args.power == 'status':
            print 'cmd standby'
            print 'Power Status: %s' % receiver.power_status()

