import os
import sys
import signal
import argparse
import threading

import sarge
    
phantom_bin = 'vendor/phantomjs-1.6.0/bin/phantomjs'
js_path = 'load.js'
target_url = os.path.join(os.path.dirname(os.path.realpath( __file__ )), 
    'index.html')


def shoot():
    cmd = ' '.join([phantom_bin, js_path, target_url])
    sarge.run(cmd, stdout=sys.stdout, stderr=sys.stderr, async=True)


def main(n):
    for i in range(0, n):
        print "Spawing process %d" % i
        shoot()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a web page n times')
    parser.add_argument('--number', dest='number', type=int, default=2,
                   help='number of times that we run the web page')

    args = parser.parse_args()
    main(args.number)

    def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)

    print 'Press Ctrl+C'
    while True:
        pass