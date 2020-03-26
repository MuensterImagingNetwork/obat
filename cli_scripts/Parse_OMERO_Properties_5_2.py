#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:16:53 2017

@author: evenhuis
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2015 University of Dundee & Open Microscopy Environment.
#                    All Rights Reserved.
# Use is subject to license terms supplied in LICENSE.txt
#

"""
FOR TRAINING PURPOSES ONLY!
"""

import omero

#client = omero.client('midata.research.uts.edu.au')
client = omero.client('omero-app.research.uts.edu.au')
omeroProperties = client.getProperties().getPropertiesForPrefix('omero')

# Configuration
# =================================================================
# These values will be imported by all the other training scripts.
HOST = omeroProperties.get('omero.host', 'omero-app.research.uts.edu.au')
PORT = omeroProperties.get('omero.port', 4064)
USERNAME = omeroProperties.get('omero.user','')  # staff ID here
PASSWORD = omeroProperties.get('omero.pass','')  # LDAP passwors here
OMERO_WEB_HOST = omeroProperties.get('omero.webhost')
