#!/usr/bin/env python

import os, sys
sys.path.insert ( 0, os.path.dirname(os.path.abspath(__file__) ) + "/../" )
import gepard

def on_ABLARM ( event ):
	print ( event )

gepard.Client.getInstance().on ( ["ALARM","BLARM"], on_ABLARM )

gepard.util.exitWithSIGINT()

