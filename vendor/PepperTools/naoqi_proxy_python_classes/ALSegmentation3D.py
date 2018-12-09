#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alsegmentation3dproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy



class ALSegmentation3D(object):
    def __init__(self, session):
        self.proxy = None 
        self.session = session

    def force_connect(self):
        self.proxy = ALProxy("ALSegmentation3D")

    def getActiveCamera(self):
        """

        :returns int: 
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.getActiveCamera()

    def getBlobTrackingDistance(self):
        """Gets the distance (in meters) for the blob tracker

        :returns float: 
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.getBlobTrackingDistance()

    def getCurrentPeriod(self):
        """Gets the current period.

        :returns int: Refresh period (in milliseconds).
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.getCurrentPeriod()

    def getCurrentPrecision(self):
        """Gets the current precision.

        :returns float: Precision of the extractor.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.getCurrentPrecision()

    def getDeltaDepthThreshold(self):
        """Gets the value of the depth threshold (in meters) used for the segmentation

        :returns float: Current depth threshold (in meters)
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.getDeltaDepthThreshold()

    def getEventList(self):
        """Get the list of events updated in ALMemory.

        :returns std::vector<std::string>: Array of events updated by this extractor in ALMemory
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.getEventList()

    def getFrameRate(self):
        """

        :returns int: 
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.getFrameRate()

    def getMemoryKeyList(self):
        """Get the list of events updated in ALMemory.

        :returns std::vector<std::string>: Array of events updated by this extractor in ALMemory
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.getMemoryKeyList()

    def getMyPeriod(self, name):
        """Gets the period for a specific subscription.

        :param str name: Name of the module which has subscribed.
        :returns int: Refresh period (in milliseconds).
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.getMyPeriod(name)

    def getMyPrecision(self, name):
        """Gets the precision for a specific subscription.

        :param str name: name of the module which has subscribed
        :returns float: precision of the extractor
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.getMyPrecision(name)

    def getOutputNames(self):
        """Get the list of values updated in ALMemory.

        :returns std::vector<std::string>: Array of values updated by this extractor in ALMemory
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.getOutputNames()

    def getResolution(self):
        """

        :returns int: 
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.getResolution()

    def getSubscribersInfo(self):
        """Gets the parameters given by the module.

        :returns AL::ALValue: Array of names and parameters of all subscribers.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.getSubscribersInfo()

    def getTopOfBlob(self, distance, frame, applyVerticalOffset):
        """Returns the position of the top of the blob most in the center of the depth image, at the given distance, in the given frame.

        :param float distance: Estimation of the distance (in meters) of the blob or -1 for the nearest blob
        :param int frame: Frame in which to return the position (-1: FRAME_IMAGE, 0: FRAME_TORSO, 1: FRAME_WORLD, 2: FRAME_ROBOT
        :param bool applyVerticalOffset: True to apply the VerticalOffset when computing the position, False otherwise
        :returns AL::ALValue: Position of the top of the corresponding blob (if one is found) in the given frame (Format: [yaw,pitch,distance] in FRAME_IMAGE, [x,y,z] in the other frame).
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.getTopOfBlob(distance, frame, applyVerticalOffset)

    def getVerticalOffset(self):
        """Sets the value of vertical offset (in meters) for the blob tracker

        :returns float: Current vertical offset of the blob tracker
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.getVerticalOffset()

    def isBlobTrackingEnabled(self):
        """Gets the current status of the blob tracker. When the blob tracker is running, events containing the position of the top of the tracked blob are raised.

        :returns bool: True if the blob tracker is enabled, False otherwise.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.isBlobTrackingEnabled()

    def isPaused(self):
        """

        :returns bool: 
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.isPaused()

    def isProcessing(self):
        """

        :returns bool: 
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.isProcessing()

    def pause(self, status):
        """

        :param bool status: 
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.pause(status)

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.ping()

    def setActiveCamera(self, cameraID):
        """

        :param int cameraID: 
        :returns bool: 
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.setActiveCamera(cameraID)

    def setBlobTrackingDistance(self, distance):
        """Sets the distance (in meters) for the blob tracker

        :param float distance: New value (in meters)
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.setBlobTrackingDistance(distance)

    def setBlobTrackingEnabled(self, status):
        """Turn the blob tracker on or off. When the blob tracker is running, events containing the position of the top of the tracked blob are raised.

        :param bool status: True to turn it on, False to turn it off.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.setBlobTrackingEnabled(status)

    def setDeltaDepthThreshold(self, value):
        """Sets the value of the depth threshold (in meters) used for the segmentation

        :param float value: New depth threshold (in meters) for the segmentation
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.setDeltaDepthThreshold(value)

    def setFrameRate(self, value):
        """

        :param int value: 
        :returns bool: 
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.setFrameRate(value)

    def setResolution(self, resolution):
        """

        :param int resolution: 
        :returns bool: 
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.setResolution(resolution)

    def setVerticalOffset(self, value):
        """Sets the value of vertical offset (in meters) for the blob tracker

        :param float value: New vertical offset (in meters), added if positive, substracted if negative
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.setVerticalOffset(value)

    def subscribe(self, name, period, precision):
        """Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.

        :param str name: Name of the module which subscribes.
        :param int period: Refresh period (in milliseconds) if relevant.
        :param float precision: Precision of the extractor if relevant.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.subscribe(name, period, precision)

    def subscribe2(self, name):
        """Subscribes to the extractor. This causes the extractor to start writing information to memory using the keys described by getOutputNames(). These can be accessed in memory using ALMemory.getData("keyName"). In many cases you can avoid calling subscribe on the extractor by just calling ALMemory.subscribeToEvent() supplying a callback method. This will automatically subscribe to the extractor for you.

        :param str name: Name of the module which subscribes.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.subscribe(name)

    def unsubscribe(self, name):
        """Unsubscribes from the extractor.

        :param str name: Name of the module which had subscribed.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.unsubscribe(name)

    def updatePeriod(self, name, period):
        """Updates the period if relevant.

        :param str name: Name of the module which has subscribed.
        :param int period: Refresh period (in milliseconds).
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.updatePeriod(name, period)

    def updatePrecision(self, name, precision):
        """Updates the precision if relevant.

        :param str name: Name of the module which has subscribed.
        :param float precision: Precision of the extractor.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.updatePrecision(name, precision)

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = ALProxy("ALSegmentation3D")
        return self.proxy.version()