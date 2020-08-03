# pyIRIS-template

This simple repository that uses InterSystems IRIS as a database and python container which communicates with the IRIS via IRIS Native API.
 
This examples runs the globals.py code repeatedly (first couple of times it runs to error because it just does not want to wait for IRIS to load, but as soon as it is loaded it performs successfully)
 
  git clone https://github.com/renesto/pyIRIS-template.git
  cd pyIRIS-template/
  docker-compose up

It loads IRIS and then afterwards the python container sets a global (in native IRIS language called Objectscript, command SET creates the global).
 
Once you see it is done, you can also look at the global in graphical interface:

http://localhost:52773/csp/sys/exp/UtilExpGlobalView.csp?$ID2=testglobal&$NAMESPACE=USER&$NAMESPACE=USER

 
