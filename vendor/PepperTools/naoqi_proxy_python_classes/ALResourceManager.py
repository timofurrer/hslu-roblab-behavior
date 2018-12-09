#!/usr/bin/env python
# Class autogenerated from /home/sam/Downloads/aldebaran_sw/nao/naoqi-sdk-2.1.4.13-linux64/include/alproxies/alresourcemanagerproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running

from naoqi import ALProxy



class ALResourceManager(object):
    def __init__(self, session):
        self.proxy = None 
        self.session = session

    def force_connect(self):
        self.proxy = self.session.service("ALResourceManager")

    def acquireResource(self, resourceName, moduleName, callbackName, timeoutSeconds):
        """Wait and acquire a resource

        :param str resourceName: Resource name
        :param str moduleName: Module name
        :param str callbackName: callback name
        :param int timeoutSeconds: Timeout in seconds
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.acquireResource(resourceName, moduleName, callbackName, timeoutSeconds)

    def acquireResourcesTree(self, resourceName, moduleName, callbackName, timeoutSeconds):
        """Wait for resource tree. Parent and children are not in conflict. Local function

        :param std::vector<std::string> resourceName: Resource name
        :param str moduleName: Module name
        :param str callbackName: callback name
        :param int timeoutSeconds: Timeout in seconds
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.acquireResourcesTree(resourceName, moduleName, callbackName, timeoutSeconds)

    def areResourcesFree(self, resourceNames):
        """True if all resources are free

        :param std::vector<std::string> resourceNames: Resource names
        :returns bool: True if all the specify resources are free
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.areResourcesFree(resourceNames)

    def areResourcesOwnedBy(self, resourceNameList, ownerName):
        """True if all the specified resources are owned by the owner

        :param std::vector<std::string> resourceNameList: Resource name
        :param str ownerName: Owner pointer with hierarchy
        :returns bool: True if all the specify resources are owned by the owner
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.areResourcesOwnedBy(resourceNameList, ownerName)

    def checkStateResourceFree(self, resourceName):
        """check if all the state resource in the list are free

        :param std::vector<std::string> resourceName: Resource name
        :returns bool: 
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.checkStateResourceFree(resourceName)

    def createResource(self, resourceName, parentResourceName):
        """Create a resource

        :param str resourceName: Resource name to create
        :param str parentResourceName: Parent resource name or empty string for root resource
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.createResource(resourceName, parentResourceName)

    def createResourcesList(self, resourceGroupName, resourceName):
        """True if a resource is in another parent resource

        :param std::vector<std::string> resourceGroupName: Group name. Ex: Arm
        :param str resourceName: Resource name
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.createResourcesList(resourceGroupName, resourceName)

    def deleteResource(self, resourceName, deleteChildResources):
        """Delete a root resource

        :param str resourceName: Resource name to delete
        :param bool deleteChildResources: DEPRECATED: Delete child resources if true
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.deleteResource(resourceName, deleteChildResources)

    def enableStateResource(self, resourceName, enabled):
        """Enable or disable a state resource

        :param str resourceName: The name of the resource that you wish enable of disable. e.g. Standing
        :param bool enabled: True to enable, false to disable
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.enableStateResource(resourceName, enabled)

    def getResources(self):
        """Get tree of resources

        :returns AL::ALValue: 
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.getResources()

    def isInGroup(self, resourceGroupName, resourceName):
        """True if a resource is in another parent resource

        :param str resourceGroupName: Group name. Ex: Arm
        :param str resourceName: Resource name
        :returns bool: 
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.isInGroup(resourceGroupName, resourceName)

    def isResourceFree(self, resourceNames):
        """True if the resource is free

        :param str resourceNames: Resource name
        :returns bool: True if the specify resources is free
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.isResourceFree(resourceNames)

    def ownersGet(self):
        """The tree of the resources owners.

        :returns AL::ALValue: 
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.ownersGet()

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.ping()

    def releaseResource(self, resourceName, ownerName):
        """Release resource

        :param str resourceName: Resource name
        :param str ownerName: Existing owner name
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.releaseResource(resourceName, ownerName)

    def releaseResources(self, resourceNames, ownerName):
        """Release  resources list

        :param std::vector<std::string> resourceNames: Resource names
        :param str ownerName: Owner name
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.releaseResources(resourceNames, ownerName)

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.version()

    def waitForOptionalResourcesTree(self, arg1, arg2, arg3, arg4, arg5):
        """Wait resource

        :param std::vector<std::string> arg1: arg
        :param str arg2: arg
        :param str arg3: arg
        :param int arg4: arg
        :param std::vector<std::string> arg5: arg
        :returns std::vector<std::string>: 
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.waitForOptionalResourcesTree(arg1, arg2, arg3, arg4, arg5)

    def waitForResource(self, resourceName, ownerName, callbackName, timeoutSeconds):
        """Wait resource

        :param str resourceName: Resource name
        :param str ownerName: Module name
        :param str callbackName: callback name
        :param int timeoutSeconds: Timeout in seconds
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.waitForResource(resourceName, ownerName, callbackName, timeoutSeconds)

    def waitForResourcesTree(self, resourceName, moduleName, callbackName, timeoutSeconds):
        """Wait for resource tree. Parent and children are not in conflict. Local function

        :param std::vector<std::string> resourceName: Resource name
        :param str moduleName: Module name
        :param str callbackName: callback name
        :param int timeoutSeconds: Timeout in seconds
        """
        if not self.proxy:
            self.proxy = self.session.service("ALResourceManager")
        return self.proxy.waitForResourcesTree(resourceName, moduleName, callbackName, timeoutSeconds)
